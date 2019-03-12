import sys
import threading
import time
import datetime
import traceback
import os
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
		self.cwd = configuration['repoPath']
		self.branch = configuration['branch']
		self.pollTimeout = configuration['pollTimeout']
		self.steps = configuration['steps']

		_cliProvider.setOutputListener(self.notifyAboutOutputLine)

		for step in self.steps:
			command = step.split()[0]

			if not supportedCommands[command]:
				raise ValueError('Command ' + command + ' not supported!')

		EventBus.subscribe(EVENTS['NEW_BUILD_ADDED'], self.rebuild)
		EventBus.subscribe(EVENTS['PROJECT_UPDATED'], self.reconfigureAfterProjectChange)

	def reconfigureAfterProjectChange(self, project):
		if project['key'] != self.key:
			return

		self.repoPath = project['repoPath']
		self.branch = project['branch']

		stepsString = project['steps']
		if stepsString != None:
			steps = stepsString.split(';;')
		else:
			steps = []
		self.steps = steps

	def notifyAboutOutputLine(self, line):
		data = {
			'projectKey': self.key,
			'line': line
		}

		EventBus.publish(EVENTS['NEW_OUTPUT_LINE'], data)
		
	def startPolling(self):
		while True:
			try:
				time.sleep(self.pollTimeout)

				build = projectDao.getProjectsLastBuild(self.key)

				if build['status'] == 'pending':
					continue

				self.fetchChanges()
				exitCode = self.checkoutBranch()
				if exitCode != 0:
					continue

				lastCommit = self.getLastCommit()
				lastSavedCommit = self.getLastSavedCommit()

				if (lastCommit == lastSavedCommit):
					msg = 'Branch {branch} is up to date'.format(branch=self.branch)
					self.notifyAboutOutputLine(msg)
					print (msg)
					continue

				changesMsg = 'Changes in {branch}'.format(branch=self.branch)
				self.notifyAboutOutputLine(changesMsg)
				print (changesMsg)

				stepsMsg = 'Running steps...'
				self.notifyAboutOutputLine(stepsMsg)
				print (stepsMsg)

				self.saveLastCommit(lastCommit)
				self.build(lastCommit)
			except Exception as e:
				print e
				traceback.print_exc()


	def init(self):
		thread = threading.Thread(target=self.startPolling, args=())
		thread.start()

	def printStepFail(self, step, exception):
		outputTemplate = 'Build step "{step}" failed. Uncaught exception {exception}'
		output = outputTemplate.format(step=step, exception=exception)

		print (output)
		self.notifyAboutOutputLine(output)

		failMsg = 'Build failed!'
		print (failMsg)
		self.notifyAboutOutputLine(failMsg)

	def printCurrentStep(self, index, step):
		stepsCount = len(self.steps)

		messageTemplate = 'Step {index} of {stepsCount}: {step}'
		message = messageTemplate.format(index=index, stepsCount=stepsCount, step=step)

		print (message)
		self.notifyAboutOutputLine(message)

	def fetchChanges(self):
		fetchMsg = 'Fetching changes...'
		print (fetchMsg)
		self.notifyAboutOutputLine(fetchMsg)

		try:
			_cliProvider.run('git fetch', self.repoPath)

			return 0
		except ValueError as e:
			excMsg = 'Cound not fetch changes. Uncaught exception {e}'.format(e=e)
			print (excMsg)
			self.notifyAboutOutputLine(excMsg)
			return e

	def pullChanges(self):
		pullMsg = 'Pulling changes from branch {branch}...'.format(branch=self.branch)
		print (pullMsg)
		self.notifyAboutOutputLine(pullMsg)

		try:
			_cliProvider.run('git pull', self.repoPath)

			return 0
		except ValueError as e:
			excMsg = 'Cound not pull changes from {branch}. Uncaught exception {e}'.format(branch=self.branch, e=e)
			print (excMsg)
			self.notifyAboutOutputLine(excMsg)
			return e

	def checkoutBranch(self):
		checkoutMsg = 'Checking out branch {branch}...'.format(branch=self.branch)
		print (checkoutMsg)
		self.notifyAboutOutputLine(checkoutMsg)

		try:
			_cliProvider.run('git checkout origin/{branch}'.format(branch=self.branch), self.repoPath)

			return 0
		except ValueError as e:
			excMsg = 'Cound not check out {branch}. Uncaught exception {e}'.format(branch=self.branch, e=e)
			print (excMsg)
			self.notifyAboutOutputLine(excMsg)
			return e

	def checkoutCommit(self, commit):
		checkoutMsg = 'Checking out commit {commit}...'.format(commit=commit)
		print (checkoutMsg)
		self.notifyAboutOutputLine(checkoutMsg)

		try:
			_cliProvider.run('git checkout {commit}'.format(commit=commit), self.repoPath)

			return 0
		except ValueError as e:
			excMsg = 'Cound not check out {commit}. Uncaught exception {e}'.format(commit=commit, e=e)
			print (excMsg)
			self.notifyAboutOutputLine(excMsg)
			return e

	def getLastCommit(self):
		try:
			output = _cliProvider.run('git rev-parse HEAD', self.repoPath)
			commit = output.replace('\n', '').encode('utf-8')
			return commit
		except ValueError as e:
			excMsg = 'Cound not get last commit hash. Uncaught exception {e}'.format(e=e)
			print (excMsg)
			self.notifyAboutOutputLine(excMsg)
			return e

	def getLastCommitMessage(self):
		try:
			output = _cliProvider.run('git log -1 --pretty=%B', self.repoPath)
			message = output.replace('\n', '').encode('utf-8')
			return message
		except ValueError as e:
			excMsg = 'Could not get last commit message. Uncaught exception {e}'.format(e=e)
			print (excMsg)
			self.notifyAboutOutputLine(excMsg)
			return e

	def getLastCommitAuthor(self):
		try:
			output = _cliProvider.run('git log -1 --pretty=format:"%an (%ae)"', self.repoPath)
			author = output.replace('\n', '').encode('utf-8')
			return author
		except ValueError as e:
			excMsg = 'Could not get last commit author. Uncaught exception {e}'.format(e=e)
			print (excMsg)
			self.notifyAboutOutputLine(excMsg)
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

		buildDao.setBuildStatus(_id, status)
		buildDao.setBuildEndTime(_id, datetime.datetime.utcnow)
		buildDao.setBuildDuration(_id, duration)
		buildDao.setBuildOutput(_id, output)

	def resetAfterBuild(self):
		self.cwd = self.repoPath

	def rebuild(self, build):
		commit = build['commitId']

		code = self.checkoutCommit(commit)
		if code != 0:
			return
		
		self.build(commit)

	def build(self, lastCommit):
		output = [];

		def appendOutput(data, output):
			if data['projectKey'] != self.key:
				return

			output.append(data['line'])

		outputAppender = lambda line : appendOutput(line, output)

		try:
			message = self.getLastCommitMessage()
			author = self.getLastCommitAuthor()

			_build = {
				'commitId': lastCommit,
				'commitMessage': message,
				'commitAuthor': author
			}

			buildId = projectDao.addBuild(self.key, _build)

			def handleNewLine(line):
				outputAppender(line, output)
				buildDao.setBuildOutput(buildId, '\n'.join(output))

			EventBus.subscribe(EVENTS['NEW_OUTPUT_LINE'], outputAppender)

			i = 1
			for step in self.steps:
				self.printCurrentStep(i, step)
				stepParts = step.split()

				command = stepParts[0]
				arguments = stepParts[1:]

				try:
					if command == "COPY":
						_cliProvider.copy(arguments[0], arguments[1], self.cwd)
					elif command == "WORKDIR":
						code = _cliProvider.workdir(arguments[0], self.cwd)
						print (code)
						if code == 0:
							self.cwd = os.path.normpath(os.path.join(self.cwd, arguments[0]))
					elif command == "RUN":
						_cliProvider.run(" ".join(arguments), self.cwd)
				except ValueError as e:
					self.saveBuildResults({
						'_id': buildId,
						'output': '\n'.join(output),
						'status': 'fail'
					})
					projectDao.setProjectStatus(self.key, 'fail')
					EventBus.unsubscribe(EVENTS['NEW_OUTPUT_LINE'], appendOutput)
					self.printStepFail(step, e)
					self.resetAfterBuild()
					return e

				i += 1
			self.saveBuildResults({
				'_id': buildId,
				'output': '\n'.join(output),
				'status': 'success',
			})
			projectDao.setProjectStatus(self.key, 'success')
			EventBus.unsubscribe(EVENTS['NEW_OUTPUT_LINE'], outputAppender)
			print ('Build successful!')
			self.resetAfterBuild()
			return 0
		except Exception as e:
			self.saveBuildResults({
				'_id': buildId,
				'output': '\n'.join(output),
				'status': 'fail',
			})
			projectDao.setProjectStatus(self.key, 'fail')
			EventBus.unsubscribe(EVENTS['NEW_OUTPUT_LINE'], outputAppender)
			print ('Build failed! Exception {e}'.format(e=e))
			traceback.print_exc()
			self.resetAfterBuild()
