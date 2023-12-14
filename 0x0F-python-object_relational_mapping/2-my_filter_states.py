#!/usr/bin/python3
"""  script that display all table in a state where name matched the arg """
import MySQLdb
from sys import argv


if __name__ == "__main__":
    connect = MySQLdb.connect(
        user=argv[1], passwd=argv[2], db=argv[3], host="localhost", port=3306
        )

    cur = connect.cursor()

    cmd = "SELECT * FROM states WHERE name='{}' ORDER BY id ASC"
    cur.execute(cmd.format(argv[4],))
    rows = cur.fetchall()
    for row in rows:
        if row[1] == argv[4]:
            print(row)
    cur.close()
    connect.close()
