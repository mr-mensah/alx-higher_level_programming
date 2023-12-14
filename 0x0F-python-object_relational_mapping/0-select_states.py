#!/usr/bin/python3
""" script that lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    dab = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], dab=sys.argv[3], port=3306)
    cu = dab.cursor()
    cu.execute("SELECT * FROM states")
    rows = cu.fetchall()
    for row in rows:
        print(row)
    cu.close()
    dab.close()
