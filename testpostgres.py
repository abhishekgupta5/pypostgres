import psycopg2

#This script only insures whether the connection to postgres is established or not
try:
    connect_str = "dbname='testdb' user='postgres' host='localhost'"+ "password=''"
#Ensure that you have a 'user' and 'database' created before executing above command. See 'createuser' and 'createdb' postgres commands for details
    conn = psycopg2.connect(connect_str)
    cursor = conn.cursor()
    cursor.execute(""" CREATE TABLE student (name char(40)); """)
    cursor.execute("""select * from student""")
    rows = cursor.fetchall()
    print(rows)
except Exception as e:
    print("Can't connect. Invalid db, user, or password ?")
    print(e)
