#!/usr/bin/python3

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
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name ="
    "%s ORDER BY states.id ASC LIMIT 1"
    cursor.execute(query, (state_name,))
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py <username> <password> <database>"
              "<state_name>")
        sys.exit(1)

    username, password, database, state_name =
    sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    filter_states(username, password, database, state_name)
