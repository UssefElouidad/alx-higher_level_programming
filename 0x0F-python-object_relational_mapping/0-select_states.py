#!/usr/bin/python3
"""
0-select_states.py - A script to connect to a MySQL server, retrieve and display states from the hbtn_0e_0_usa database.
Usage:
    python 0-select_states.py <username> <password> <database>
Arguments:
    username (str): MySQL username.
    password (str): MySQL password.
    database (str): MySQL database name.

Example:
    python 0-select_states.py root password hbtn_0e_0_usa
"""

import MySQLdb
import sys

def list_states(username, password, database):
    """
    Connects to a MySQL server and retrieves states from the 'states' table.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): MySQL database name.

    Returns:
        None
    """
    
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    cursor = db.cursor()

    # Execute SQL query to retrieve states
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    states = cursor.fetchall()

    # Display results
    for state in states:
        print(state)

    # Close the cursor and database connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    # Get MySQL credentials from command line arguments
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Call the function to list states
    list_states(username, password, database)
