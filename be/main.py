import os
from modules import buildAgent, dbConnection, helpers
from modules.eventBus import EVENT_BUS as EventBus
from constants.events import EVENTS

import api
from api.services.project import projectDao

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
	projects = projectDao.getProjects()
	projects = map(lambda proj: helpers.mongoToDict(proj), projects)
	for project in projects:
		initBuildAgent(project)

if __name__ == "__main__":
	print ('main')

	initBuildAgents()

	EventBus.subscribe(EVENTS['NEW_PROJECT_CREATED'], initBuildAgent)

	host = os.environ.get('HOST') or '0.0.0.0'
	port = os.environ.get('PORT') or 8080

	api.app.run(host=host, port=port)
