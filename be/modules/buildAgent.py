import sys
import threading
import time
import datetime
from modules import cliProvider
from api.services.project import projectDao
from api.services.build import buildDao
from modules.eventBus import EVENT_BUS as EventBus
from constants.events import EVENTS

_cliProvider = None

if sys.platform == 'linux' or sys.platform == 'linux2':
	_cliProvider = cliProvider.createCli("terminal-cli")
elif sys.platform == 'win32' or sys.platform == 'win64':
	#_cliProvider = cliProvider.createCli("win32_COM")
	_cliProvider = cliProvider.createCli("terminal-cli")




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

		EventBus.publish(EVENTS['NEW_OUTPUT_LINE'], data)
		
	def startPolling(self):
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
			self.build(lastCommit)


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
			commit = output.replace('\n', '').encode('utf-8')
			return commit
		except ValueError as e:
			print ('Cound not get last commit hash. Uncaught exception {e}'.format(e=e))
			return e

	def getLastCommitMessage(self):
		try:
			output = _cliProvider.run('git log -1 --pretty=%B', self.repoPath)
			message = output.replace('\n', '').encode('utf-8')
			return message
		except ValueError as e:
			print ('Could not get last commit message. Uncaught exception {e}'.format(e=e))
			return e

	def getLastCommitAuthor(self):
		try:
			output = _cliProvider.run('git log -1 --pretty=format:"%an (%ae)"', self.repoPath)
			author = output.replace('\n', '').encode('utf-8')
			return author
		except ValueError as e:
			print ('Could not get last commit author. Uncaught exception {e}'.format(e=e))
			return e

	def getLastSavedCommit(self):
		commit = projectDao.getProjectsLastCommit(self.key)

		return commit

	def saveLastCommit(self, lastCommit):
		projectDao.saveLastCommit(self.key, lastCommit)

	def saveBuildResults(self, build):
		_id = build['_id']
		output = build['output']
		status = build['status']
		startTime = buildDao.getBuildById(_id).startTime
		endTime = datetime.datetime.now()
		duration = (endTime - startTime).total_seconds() * 1000

		buildDao.setBuildStatus(buildId, status)
		buildDao.setBuildEndTime(buildId, datetime.datetime.utcnow)
		buildDao.setBuildDuration(buildId, duration)
		buildDao.setBuildOutput(buildDao, output)

	def build(self, lastCommit):
		message = self.getLastCommitMessage()
		author = self.getLastCommitAuthor()

		buildId = build = {
			commitId: lastCommit,
			commitMessage: message,
			commitAuthor: author
		}

		projectDao.addBuild(self.key, build)

		output = '';

		def appendOutput(line):
			output += line

		EventBus.subscribe(EVENTS['NEW_OUTPUT_LINE'], appendOutput)

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
				self.saveBuildResults({
					_id: buildId,
					output: output,
					status: 'fail'
				})
				EventBus.unsubscribe(EVENTS['NEW_OUTPUT_LINE'], appendOutput)
				self.printStepFail(step, e)
				return e

			i += 1
		self.saveBuildResults({
			_id: buildId,
			output: output,
			status: 'success',
		})
		EventBus.unsubscribe(EVENTS['NEW_OUTPUT_LINE'], appendOutput)
		print ('Build successful!')
		return 0
