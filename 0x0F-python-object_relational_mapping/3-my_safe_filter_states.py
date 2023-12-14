#!/usr/bin/python3
""" query that matches arges but safe SQL injection """
import MySQLdb
from sys import argv


if __name__ == "__main__":
    connect = MySQLdb.connect(
        user=argv[1], passwd=argv[2], db=argv[3], host="localhost", port=3306
        )

    cur = connect.cursor()
    cmd = "SELECT * FROM states WHERE name = %s ORDER BY id"
    cur.execute(cmd, (argv[4],))
    rows = cur.fetchall()

    for row in rows:
        print(row)
    cur.close()
    connect.close()
