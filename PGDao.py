import psycopg2

class PGDao:

	def __init__(self, host, database, port, user, password):
		self.conn = psycopg2.connect(host=host, database=database, user=user, password=password, port=port);
		self.cursor = self.conn.cursor()

	def run_query(self, query):
		self.cursor.execute(query)
		return self.cursor

def main():
	host = 'host-redshift'
	database = 'banco-redshift'
	port = 5439
	user = 'liz.zorzo'
	password = 'senhaSecretaDaLiz'
	dao = PGDao(host=host, database=database, user=user, password=password, port=port)

	cursor = dao.run_query('SELECT 1 as x UNION SELECT 2 as x')
	
	row = cursor.fetchone()
	while row:
		print(row)
		row = cursor.fetchone()

	cursor = dao.run_query('SELECT 3 as x UNION SELECT 4')
	rows = cursor.fetchall()
	print(rows)


if __name__ == '__main__':
	main()
