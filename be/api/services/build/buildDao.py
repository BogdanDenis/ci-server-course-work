import datetime
from mongoengine import *
from modules.helpers import mongoToDict

class Build(Document):
	commitId = StringField(max_length=120, required=True)
	commitMessage = StringField(max_length=500, required=True)
	commitAuthor = StringField(max_length=255, required=True)
	status = StringField(default='pending')
	startTime = DateTimeField(default=datetime.datetime.utcnow)
	endTime = DateTimeField()
	duration = FloatField(min_value=0)
	output = StringField()


def getBuilds():
	return Build.objects()

def getBuildById(_id):
	res = Build.objects(id=_id)

	if len(res) > 0:
		return res[0]
	return None

def setBuildStatus(_id, status):
	build = getBuildById(_id)

	if build == None:
		return

	build.status = status
	build.save()

def setBuildEndTime(_id, endTime):
	build = getBuildById(_id)

	if build == None:
		return

	build.endTime = endTime
	build.save()

def setBuildDuration(_id, duration):
	build = getBuildById(_id)

	if build == None:
		return

	build.duration = duration
	build.save()

def setBuildOutput(_id, output):
	build = getBuildById(_id)

	if build == None:
		return

	build.output = output
	build.save()