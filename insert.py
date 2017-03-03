#!/usr/bin/python3
import psycopg2

conn = psycopg2.connect(database="testdb", user="postgres", host="localhost", password="", port="5432")

print("Opened database successfully")

cur = conn.cursor()

cur.execute("""INSERT INTO STARTUP (ID, NAME, TYPE) VALUES (1, 'AWS', 'IaaS/Paas');""")

cur.execute("""INSERT INTO STARTUP (ID, NAME, TYPE) VALUES (2, 'Heroku', 'Paas');""")

cur.execute("""INSERT INTO STARTUP (ID, NAME, TYPE) VALUES (3, 'Digital Ocean', 'IaaS/Paas');""")

conn.commit()
print("Records successfully added")
conn.close()
