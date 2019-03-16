import os, time, threading, requests
from modules import buildAgent, dbConnection, helpers
from modules.eventBus import EVENT_BUS as EventBus
from constants.events import EVENTS

import api
from api.services.project import projectDao
from api.notifier import startServer as startWSserver

host = os.environ.get('HOST') or '0.0.0.0'
port = os.environ.get('PORT') or 8080

def initBuildAgent(project):
	steps = project['steps']

	if steps != None:
		steps = steps.split(';;')
	else:
		steps = []
	agent = buildAgent.BuildAgent({
		'key': project['key'],
		'repoPath': project['repoPath'],
		'branch': project['branch'],
		'pollTimeout': project['pollTimeout'],
		'steps': steps
	})

	agent.init()

def initBuildAgents():
	print ('init agents')
	projects = projectDao.getProjects()
	projects = list(map(lambda proj: helpers.mongoToDict(proj), projects))
	for project in projects:
		initBuildAgent(project)

def startFlask():
	api.app.run(host=host, port=port, use_reloader=False)

def main():
	initBuildAgents()

	EventBus.subscribe(EVENTS['NEW_PROJECT_CREATED'], initBuildAgent)

	wsServer = startWSserver()

	thread = threading.Thread(target=startFlask)
	thread.start()

	try:
		while True:
			time.sleep(1)
	except KeyboardInterrupt as e:
		print (e)
		requests.post('http://{host}:{port}/__kill__'.format(host=host, port=port))
		wsServer.close()

if __name__ == "__main__":
	main()
