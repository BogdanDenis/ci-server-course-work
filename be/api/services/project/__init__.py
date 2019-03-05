from flask import jsonify, request
from api import app
from api.services.project import projectDao
from modules import dbConnection


@app.route('/project', methods=['GET'])
def getProjects():
	conn = dbConnection.createConnection('./ciserver.db')
	projects = projectDao.getProjects(conn)
	conn.close()
	return jsonify(projects)

@app.route('/project/<_id>', methods=['GET'])
def getProjectById(_id):
	conn = dbConnection.createConnection('./ciserver.db')
	project = projectDao.getProjectById(conn, _id)
	conn.close()
	return jsonify(project)

@app.route('/project/<key>', methods=['GET'])
def getProjectByKey(key):
	conn = dbConnection.createConnection('./ciserver.db')
	project = projectDao.getProjectByKey(conn, key)
	conn.close()	
	return jsonify(project)

@app.route('/project', methods=['POST'])
def createProject():
	conn = dbConnection.createConnection('./ciserver.db')
	project = request.get_json()

	newId = projectDao.createProject(conn, project)
	createdProject = projectDao.getProjectById(conn, newId)
	conn.close()

	return jsonify(createdProject)