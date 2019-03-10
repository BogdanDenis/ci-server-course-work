from mongoengine import *

from api.services.build.buildDao import Build
from modules.eventBus import EVENT_BUS as EventBus
from constants.events import EVENTS
from modules.helpers import mongoToDict

class Project(Document):
	key = StringField(max_length=120, required=True, unique=True)
	name = StringField(max_length=120, required=True)
	repoPath = StringField(max_length=1000, required=True)
	branch = StringField(max_length=120, required=True)
	pollTimeout = IntField(min_value=1)
	lastCommit = StringField(max_length=120)
	steps = StringField()
	builds = ListField(ReferenceField(Build))
	status = StringField(default='pending')


def getProjects():
	return Project.objects()

def getProjectById(_id):
	res = Project.objects(id=_id)

	if len(res) > 0:
		return res[0]
	return None

def getProjectByKey(key):
	res = Project.objects(key=key)

	if len(res) > 0:
		return res[0]
	return None

def createProject(project):
	_project = Project(**project)
	_project.save()

	EventBus.publish(EVENTS['NEW_PROJECT_CREATED'], _project)

	return _project.id

def getProjectsLastCommit(key):
	project = getProjectByKey(key)

	if project == None:
		return None
	return project.lastCommit.encode('utf-8')

def saveLastCommit(key, commit):
	project = getProjectByKey(key)

	if project == None:
		return
	
	project.lastCommit = commit
	project.save()

def addBuild(key, build):
	_build = Build(**build)
	_build.save()

	project = getProjectByKey(key)
	project.update(push__builds=_build)
	project.save()

	return _build.id

def getProjectsBuilds(_id):
	project = getProjectById(_id)

	builds = map(lambda b : mongoToDict(Build.objects(id=b.id)[0]), project.builds)

	return builds

def getProjectsLastBuild(key):
	project = getProjectByKey(key)
	builds = getProjectsBuilds(project['id'])

	lastBuild = builds[len(builds) - 1]

	return lastBuild

def setProjectStatus(key, status):
	project = getProjectByKey(key)

	if project == None:
		return
	
	project.status = status
	project.save()