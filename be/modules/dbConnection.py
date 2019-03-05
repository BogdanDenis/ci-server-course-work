import sqlite3
from sqlite3 import Error

def createConnection(file):
	try:
		conn = sqlite3.connect(file)
		conn.text_factory = str
		conn.row_factory = sqlite3.Row
		return conn
	except Error as e:
		print (e)

	return None

DB_CONNECTION = createConnection('./ciserver.db')
