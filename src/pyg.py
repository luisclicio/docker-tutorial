import psycopg2
import sys


class Pyg:
	'''
		Pyg: Simple Postgres Python ORM
	'''
	def __init__(self, database, port, user, password, host='localhost'):
		try:
			self._db = psycopg2.connect(
				host=host,
				port=port,
				database=database,
				user=user,
				password=password,
			)
			self._cursor = self._db.cursor()
		except Exception as error:
			sys.exit(error)

	@property
	def cursor(self):
		return self._cursor

	def close(self):
		try:
			self._cursor.close()
			self._db.close()
			return True
		except:
			return False

	def run_query(self, sql, params=[]):
		try:
			self._cursor.execute(sql, params)
			return self._cursor.fetchall()
		except Exception as error:
			print(error)
			return None
		finally:
			self._db.commit()
