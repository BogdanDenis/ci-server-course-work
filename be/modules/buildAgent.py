import sys
import threading
import time
import datetime
import traceback
import os
import json
from modules import cliProvider, helpers
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
		self.output = []
		self.buildId = None

		_cliProvider.setOutputListener(self.notifyAboutOutputLine)

		for step in self.steps:
			command = step.split()[0]

			if not supportedCommands[command]:
				raise ValueError('Command ' + command + ' not supported!')

		def handleNewBuildAdded(data):
			if data['projectId'] != self.key:
				return

			self.rebuild(data['build'])

		EventBus.subscribe(EVENTS['NEW_BUILD_ADDED'], handleNewBuildAdded)
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

		if self.buildId == None:
			return

		EventBus.publish(EVENTS['WS_NOTIFY'], json.dumps({
			'type': 'NEW_OUTPUT_LINE',
			'payload': {
				'buildId': self.buildId,
				'line': line
			}
		}))
		
	def startPolling(self):
		while True:
			try:
				time.sleep(self.pollTimeout)

				build = projectDao.getProjectsLastBuild(self.key)

				if build != None:
					if build['status'] == 'pending':
						continue

				self.fetchChanges()
				exitCode = self.checkoutBranch()
				if exitCode != 0:
					continue

				lastCommit = self.getLastCommit()
				lastSavedCommit = self.getLastSavedCommit()

				print (lastCommit, lastSavedCommit)

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


				buildId, handleNewLine = self.prebuild(lastCommit)
				res = self.build(lastCommit)

				if res == 0:
					self.postbuild(buildId, 'success', handleNewLine)
				else:
					self.postbuild(buildId, 'fail', handleNewLine)
			except Exception as e:
				print (e)
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
			commit = output.replace('\n', '')
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
		self.output = []
		self.buildId = None

	def rebuild(self, build):
		commit = build['commitId']

		code = self.checkoutCommit(commit)
		if code != 0:
			return
		
		buildId, handleNewLine = self.prebuild(commit)

		def runBuild():
			res = self.build(commit)

			if res == 0:
				self.postbuild(buildId, 'success', handleNewLine)
			else:
				self.postbuild(buildId, 'fail', handleNewLine)

		thread = threading.Thread(target=runBuild, args=())
		thread.start()

	def prebuild(self, commit):
		def appendOutput(data, output):
			if data['projectKey'] != self.key:
				return

			self.output.append(data['line'])
			buildDao.setBuildOutput(buildId, '\n'.join(self.output))

		outputAppender = lambda line : appendOutput(line, self.output)

		def handleNewLine(data):
			outputAppender(data)

		message = self.getLastCommitMessage()
		author = self.getLastCommitAuthor()

		_build = {
			'commitId': commit,
			'commitMessage': message,
			'commitAuthor': author
		}

		buildId = projectDao.addBuild(self.key, _build)
		buildDict = helpers.mongoToDict(buildDao.getBuildById(buildId))
		self.buildId = buildDict['id']
		

		EventBus.subscribe(EVENTS['NEW_OUTPUT_LINE'], handleNewLine)

		EventBus.publish(EVENTS['WS_NOTIFY'], json.dumps({
			'type': 'NEW_BUILD_STARTED',
			'payload': {
				'projectKey': self.key,
				'build': buildDict
			}
		}))

		return buildId, handleNewLine

	def postbuild(self, buildId, status, handleNewLine):
		self.saveBuildResults({
			'_id': buildId,
			'output': '\n'.join(self.output),
			'status': status
		})
		projectDao.setProjectStatus(self.key, status)


		EventBus.publish(EVENTS['WS_NOTIFY'], json.dumps({
			'type': 'BUILD_STATUS_CHANGE',
			'payload': {
				'projectKey': self.key,
				'buildId': self.buildId,
				'status': status
			}
		}))
		self.resetAfterBuild()

		EventBus.unsubscribe(EVENTS['NEW_OUTPUT_LINE'], handleNewLine)
		
		

	def build(self, lastCommit):
		try:
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
					self.printStepFail(step, e)
					return e

				i += 1
			print ('Build successful!')
			return 0
		except Exception as e:
			print ('Build failed! Exception {e}'.format(e=e))
			traceback.print_exc()
			return e
