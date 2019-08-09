#!/usr/bin/python3
# a script that lists all states from the database hbtn_0e_0_usa
import MySQLdb
import sys

username = sys.argv[1]
password = sys.argv[2]
dbname = sys.argv[3]
conn = MySQLdb.connect(host="localhost",
                       port=3306,
                       user=username,
                       passwd=password,
                       db=dbname,
                       charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
