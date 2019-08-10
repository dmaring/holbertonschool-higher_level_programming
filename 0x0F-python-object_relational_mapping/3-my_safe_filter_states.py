#!/usr/bin/python3
# a script that lists all states with a name starting
# the name input
import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    statename = sys.argv[4]
    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=username,
                           passwd=password,
                           db=dbname,
                           charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY " +
                "name = %s" +
                "ORDER BY id ASC;", (statename,))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
