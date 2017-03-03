#!/usr/bin/python3

import psycopg2

#Connecting to db
conn = psycopg2.connect(database="testdb", user="postgres", password="", host="localhost", port="5432")
print("Opened database successfully!")

#Creating a table
cur = conn.cursor()
cur.execute('''CREATE TABLE STARTUP(ID INT PRIMARY KEY NOT NULL, NAME TEXT NOT NULL, TYPE CHAR(50));''')

print('Table created successfully')
conn.commit()
conn.close()

