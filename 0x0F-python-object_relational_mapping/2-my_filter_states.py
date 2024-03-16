#!/usr/bin/python3
"""takes in an argument and displays all values in the states table """
import MySQLdb
import sys


def filter_states(username, password, database, state_name):
    """
    A script that takes in an argument
    and displays all values in the states table
    of hbtn_0e_0_usa where name matches the argument.


    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): MySQL database name.
        state_name (str): The name of the state to search for.


    Returns:
        None
    """


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                   .format(sys.argv[4]))
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()
