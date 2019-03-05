from modules import db

def getProjects(conn):
	sqlStatement = """
		SELECT *
		FROM project;
	"""

	res = db.select(conn, sqlStatement)

	return res

def getProjectById(conn, _id):
	sqlStatement = """
		SELECT *
		FROM project
		WHERE id = '{id}';
	""".format(id=_id)

	res = db.select(conn, sqlStatement)
	if len(res) > 0:
		return res[0]
	return None

def getProjectByKey(conn, key):
	sqlStatement = """
		SELECT *
		FROM project
		WHERE key = '{key}';
	""".format(key=key)

	res = db.select(conn, sqlStatement)[0]
	return res

def createProject(conn, project):
	sqlStatement = """
		INSERT INTO project(key, repoPath, branch, pollTimeout, steps, lastCommit)
		VALUES ('{key}', '{repoPath}', '{branch}', {pollTimeout}, '{steps}', '');
	""".format(key=project['key'],
		repoPath=project['repoPath'],
		branch=project['branch'],
		pollTimeout=project['pollTimeout'],
		steps=project['steps'])

	_id = db.insert(conn, sqlStatement)

	return _id

def checkProjectSavedInDB(conn, key):
	sqlStatement = """
		SELECT *
		FROM project
		WHERE key = "{key}";
	""".format(key=key)

	res = db.select(conn, sqlStatement)

	return len(res) > 0

def saveProject(conn, project):
	sqlStatement = """
		INSERT INTO project(key, lastCommit)
		VALUES ('{key}', '');
	""".format(key=project['key'])
