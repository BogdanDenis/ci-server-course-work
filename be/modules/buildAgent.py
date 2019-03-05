import sys
import threading
import time
from modules import cliProvider, db, dbConnection
from modules.eventBus import EVENT_BUS as EventBus
from constants.events import EVENTS

_cliProvider = None

if sys.platform == 'linux' or sys.platform == 'linux2':
	_cliProvider = cliProvider.createCli("terminal-cli")
elif sys.platform == 'win32' or sys.platform == 'win64':
	_cliProvider = cliProvider.createCli("win32_COM")




supportedCommands = {
	'COPY': 'COPY',
	'WORKDIR': 'WORKDIR',
	'RUN': 'RUN'
}

_id = 0

class BuildAgent:
	def __init__(self, configuration):
		self.id = ++_id
		self.key = configuration['key']
		self.repoPath = configuration['repoPath']
		self.branch = configuration['branch']
		self.pollTimeout = configuration['pollTimeout']
		self.steps = configuration['steps']

		_cliProvider.setOutputListener(self.notifyAboutOutputLine)

		for step in self.steps:
			command = step.split()[0]

			if not supportedCommands[command]:
				raise ValueError('Command ' + command + ' not supported!')

	def notifyAboutOutputLine(self, line):
		data = {
			'projectKey': self.key,
			'line:': line
		}

		EventBus.publish(EVENTS.NEW_OUTPUT_LINE, data)
		
	def startPolling(self):
		self.dbConnection = dbConnection.createConnection('./ciserver.db')

		while True:
			time.sleep(self.pollTimeout)

			self.fetchChanges()
			exitCode = self.checkoutBranch()
			if exitCode != 0:
				continue

			lastCommit = self.getLastCommit()
			lastSavedCommit = self.getLastSavedCommit()

			print (lastCommit, lastSavedCommit)

			if (lastCommit == lastSavedCommit):
				print ('Branch {branch} is up to date'.format(branch=self.branch))
				continue

			print ('Changes in {branch}'.format(branch=self.branch))
			print ('Running steps...')

			self.saveLastCommit(lastCommit)
			self.build()


	def init(self):
		thread = threading.Thread(target=self.startPolling, args=())
		thread.start()

	def printStepFail(self, step, exception):
		outputTemplate = 'Build step "{step}" failed. Uncaught exception {exception}'
		output = outputTemplate.format(step=step, exception=exception)

		print (output)
		print ('Build failed!')

	def printCurrentStep(self, index, step):
		stepsCount = len(self.steps)

		messageTemplate = 'Step {index} of {stepsCount}: {step}'
		message = messageTemplate.format(index=index, stepsCount=stepsCount, step=step)

		print (message)

	def fetchChanges(self):
		print ('Fetching changes...')

		try:
			_cliProvider.run('git fetch', self.repoPath)

			return 0
		except ValueError as e:
			print ('Cound not fetch changes. Uncaught exception {e}'.format(e=e))
			return e

	def pullChanges(self):
		print ('Pulling changes from branch {branch}...'.format(branch=self.branch))

		try:
			_cliProvider.run('git pull', self.repoPath)

			return 0
		except ValueError as e:
			print ('Cound not pull changes from {branch}. Uncaught exception {e}'.format(branch=self.branch, e=e))
			return e

	def checkoutBranch(self):
		print ('Checking out branch {branch}...'.format(branch=self.branch))

		try:
			_cliProvider.run('git checkout origin/{branch}'.format(branch=self.branch), self.repoPath)

			return 0
		except ValueError as e:
			print ('Cound not check out {branch}. Uncaught exception {e}'.format(branch=self.branch, e=e))
			return e

	def getLastCommit(self):
		try:
			output = _cliProvider.run('git rev-parse HEAD', self.repoPath)
			commit = output.replace('\n', '')
			return commit
		except ValueError as e:
			print ('Cound not get last commit hash. Uncaught exception {e}'.format(e=e))
			return e

	def getLastSavedCommit(self):
		sqlStatement = """
			SELECT lastCommit
			FROM project
			WHERE key = '{key}'
		""".format(key=self.key)

		res = db.select(self.dbConnection, sqlStatement)

		return res[0]['lastCommit']

	def saveLastCommit(self, lastCommit):
		sqlStatement = """
			UPDATE project
			SET lastCommit = '{commit}'
			WHERE key = '{key}'
		""".format(key=self.key, commit=lastCommit)

		db.update(self.dbConnection, sqlStatement)		

	def build(self):
		i = 1
		for step in self.steps:
			self.printCurrentStep(i, step)
			stepParts = step.split()

			command = stepParts[0]
			arguments = stepParts[1:]

			try:
				if command == "COPY":
					_cliProvider.copy(arguments[0], arguments[1], self.repoPath)
				elif command == "WORKDIR":
					_cliProvider.workdir(arguments[0], self.repoPath)
				elif command == "RUN":
					_cliProvider.run(" ".join(arguments), self.repoPath)
			except ValueError as e:
				self.printStepFail(step, e)
				return e

			i += 1

		print ('Build successful!')
		return 0
