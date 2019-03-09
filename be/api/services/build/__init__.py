from flask import jsonify, request
from api import app
from api.services.build import buildDao
from modules.helpers import mongoToDict


@app.route('/build', methods=['GET'])
def getBuilds():
	builds = buildDao.getBuilds()
	return jsonify(map(lambda build: mongoToDict(build), builds))

@app.route('/build/<_id>', methods=['GET'])
def getBuildById(_id):
	build = buildDao.getBuildById(_id)
	return jsonify(mongoToDict(build))
