from flask import jsonify, request
from api import app
from api.services.project import projectDao
from modules.helpers import mongoToDict


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

	return jsonify(builds)