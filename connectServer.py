import pymysql


def connectServer(database_name="Library2"):
	print("connecting server...", end=" ")
	user = "root"
	password = "963.8520Mm"
	database = database_name
	host = "localhost"
	con = pymysql.connect(host=host, user=user, password=password, database=database)
	cur = con.cursor()
	print("done.")
	return con, cur


def create_new_db(name, books_table_name="books", books_issued_table_name="books_issued"):
	user = "root"
	password = "963.8520Mm"
	database = name
	host = "localhost"
	con = pymysql.connect(host=host, user=user, password=password)
	cr = con.cursor()
	query = "SHOW DATABASES"
	cr.execute(query)
	database_list = cr.fetchall()
	database_list = [x[0] for x in database_list]

	if name in database_list:
		print(f"database {name} already present")
	else:
		query = "CREATE DATABASE " + database
		cr.execute(query)

	con.select_db(name)
	query_table = lambda x : f"SHOW TABLES LIKE '"+x+"'"


# create a table books if not present already
	query = query_table(books_table_name)
	cr.execute(query)
	result = cr.fetchone()

	if not result:
		query = f"create table {books_table_name} (bid varchar(20) primary key, title varchar(30), author varchar(30), status varchar(30))"
		cr.execute(query)
		con.commit()

		query = "DESC books"
		cr.execute(query)
		results = cr.fetchone()
		print(results)

	else:
		print(f"{books_table_name} table already exits. { result }")

	# create a table books if not present already
	query = query_table(books_issued_table_name)
	cr.execute(query)
	result = cr.fetchone()

	if not result:
		query = f"create table {books_issued_table_name}(bid varchar(20) primary key, issuedto varchar(30))"
		cr.execute(query)
		con.commit()

		query = "DESC books_issued"
		cr.execute(query)
		results = cr.fetchall()
		print(results)
	else:
		print(f"{books_issued_table_name} table already exits. {result}")



if __name__ == "__main__":
	create_new_db(name="Library3")
