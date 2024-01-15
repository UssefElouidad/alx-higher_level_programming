#!/usr/bin/python3
""" a script to delete all records of a table…"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect("localhost", user=sys.arv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = db.cursor()
    match = sys.argv[4]
    cursor.execute("SELECT * FROM states WHERE name LIKE %s", (match, ))
    states.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()
