import datetime
from flask import jsonify, request, send_from_directory
from api import app
from api.services.build import buildDao
from modules.reporters.excel import generateReport
from modules.helpers import mongoToDict


@app.route('/report', methods=['GET'])
def getReport():
    builds = buildDao.getBuilds()
    builds = list(map(lambda build: mongoToDict(build), builds))
    fileName = generateReport({
        "builds": builds
    })

    return send_from_directory("C:\\Users\\dbohdan\\Documents", fileName)
