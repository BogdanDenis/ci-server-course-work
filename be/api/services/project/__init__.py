from flask import jsonify, request
from api import app
from api.services.project import projectDao
from modules.helpers import mongoToDict
from modules.eventBus import EVENT_BUS as EventBus
from constants.events import EVENTS


@app.route('/project', methods=['GET'])
def getProjects():
	projects = projectDao.getProjects()
	return jsonify(map(lambda proj: mongoToDict(proj), projects))

@app.route('/project/<_id>', methods=['GET'])
def getProjectById(_id):
	project = projectDao.getProjectById(_id)
	return jsonify(mongoToDict(project))

@app.route('/project', methods=['POST'])
def createProject():
	project = request.get_json()

	newId = projectDao.createProject(project)
	createdProject = projectDao.getProjectById(newId)

	return jsonify(mongoToDict(createdProject))

@app.route('/project/<_id>/builds', methods=['GET'])
def getProjectsBuilds(_id):
	builds = projectDao.getProjectsBuilds(_id)

	print(builds[len(builds) - 1])

	return jsonify(builds)

@app.route('/project/<_id>/builds/<buildId>', methods=['GET'])
def getProjectsBuild(_id, buildId):
	builds = projectDao.getProjectsBuilds(_id)

	build = next(build for build in builds if build['id'] == buildId)

	return jsonify(build)

@app.route('/project/<_id>/rebuild', methods=['POST'])
def rebuildProject(_id):
	builds = projectDao.getProjectsBuilds(_id)

	build = builds[len(builds) - 1]

	print (build)

	if build['status'] == 'pending':
		return 'Build is already in progress!', 412, {'Content-Type': 'text/plain'}

	_build = build.copy()

	_build['id'] = ''
	_build['_id'] = ''

	project = projectDao.getProjectById(_id)

	EventBus.publish(EVENTS['NEW_BUILD_ADDED'], {
		'projectId': project.key,
		'build': _build
	})

	return '', 200

@app.route('/project/<_id>/updateSteps', methods=['POST'])
def updateSteps(_id):
	body = request.get_json()

	res = projectDao.setProjectSteps(_id, body['steps'])

	if res == 404:
		return '', 404

	EventBus.publish(EVENTS['PROJECT_UPDATED'], mongoToDict(res))

	return jsonify(mongoToDict(res))
