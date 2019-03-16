import datetime
from flask import jsonify, request
from api import app
from api.services.build import buildDao
from modules.helpers import mongoToDict
from modules.eventBus import EVENT_BUS as EventBus
from constants.events import EVENTS


@app.route('/build', methods=['GET'])
def getBuilds():
	builds = buildDao.getBuilds()
	return jsonify(list(map(lambda build: mongoToDict(build), builds)))

@app.route('/build/<_id>', methods=['GET'])
def getBuildById(_id):
	build = buildDao.getBuildById(_id)
	return jsonify(mongoToDict(build))

@app.route('/build/<_id>/restart', methods=['POST'])
def restartBuild(_id):
	build = buildDao.getBuildById(_id)

	if build['status'] == 'pending':
		return 'Build is already in progress!', 412, {'Content-Type': 'text/plain'}

	_build = build.copy()

	_build['id'] = ''
	_build['_id'] = ''
	EventBus.publish(EVENTS['NEW_BUILD_ADDED'], _build)

	return '', 200

@app.route('/build/<_id>/kill', methods=['POST'])
def killBuild(_id):
	buildDao.setBuildEndTime(_id, datetime.datetime.utcnow)
	buildDao.setBuildStatus(_id, 'fail')

	return '', 200