import os
from modules.dbConnection import DB_CONNECTION as conn
from modules import db
from modules import buildAgent
import api
from api.services.project import projectDao

def initDB():
	file = './ciserver.db'

	createProjectTable = """
		CREATE TABLE IF NOT EXISTS project (
			id integer PRIMARY KEY AUTOINCREMENT,
			key text UNIQUE,
			repoPath text,
			branch text,
			pollTimeout integer,
			steps text,
			lastCommit text
		);
	"""

	if conn is not None:
		db.createTable(conn, createProjectTable)
	else:
		print ('Error! Cannot create the database connection.')

	return conn

def initBuildAgents(conn):
	projects = projectDao.getProjects(conn)
	for project in projects:
		#with open("config.yml", 'r') as ymlfile:
		#	cfg = yaml.load(ymlfile)
		
		#projects = cfg['projects']
		#for project in projects:
		steps = project['steps']
		print (steps)
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

		if projectDao.checkProjectSavedInDB(conn, project['key']) != True:
			print ('Saving project {key}...'.format(key=project['key']))
			projectDao.saveProject(conn, project)

		agent.init()

if __name__ == "__main__":
	print ('main')
	conn = initDB()

	initBuildAgents(conn)

	host = os.environ.get('HOST') or '0.0.0.0'
	port = os.environ.get('PORT') or 8080

	api.app.run(host=host, port=port)
