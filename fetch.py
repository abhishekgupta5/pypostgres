#!/usr/bin/python3
import psycopg2

conn = psycopg2.connect(database="testdb", user="postgres", password="", host="127.0.0.1", port="5432")
print("Opened database successfully")

cur = conn.cursor()

cur.execute("SELECT name, type FROM STARTUP");
rows=cur.fetchall()

for row in rows:
    print("Name = ", row[0], end=' , ')
    print("Type = ", row[1])

print("Operation done successfully")
conn.close()
