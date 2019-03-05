from sqlite3 import Error

def createTable(conn, sqlStatement):
	try :
		c = conn.cursor()
		c.execute(sqlStatement)
	except Error as e:
		print (e)

def select(conn, sqlStatement):
	try:
		cur = conn.cursor()
		cur.execute(sqlStatement)

		rows = cur.fetchall()

		result = [dict(row) for row in rows]

		return result
	except Error as e:
		print (e)

	return None

def insert(conn, sqlStatement):
	try:
		cur = conn.cursor()
		cur.execute(sqlStatement)

		conn.commit()

		return cur.lastrowid
	except Error as e:
		print (e)
	
	return None

def update(conn, sqlStatement):
	try:
		cur = conn.cursor()
		cur.execute(sqlStatement)

		conn.commit()
	except Error as e:
		print (e)