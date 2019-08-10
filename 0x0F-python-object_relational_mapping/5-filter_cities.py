#!/usr/bin/python3
#  takes in the name of a state as an argument and lists all cities
# of that state,
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
    cur.execute("SELECT cities.name " +
                "FROM cities JOIN states " +
                "ON cities.state_id = states.id " +
                "WHERE states.name = %s ORDER BY cities.id ASC;", (statename,))
    query_rows = cur.fetchall()
    for i, row in enumerate(query_rows):
        row = row[0]
        if i < len(query_rows) - 1:
            print(row + ", ", end='')
    else:
        print(row)
        cur.close()
        conn.close()
