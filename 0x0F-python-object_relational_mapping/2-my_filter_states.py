#!/usr/bin/python3
"""takes in an argument and displays all values in the states table """
import MySQLdb
import sys


def filter_states(username, password, database, state_name):
    """
    A script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.
    

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): MySQL database name.
        state_name (str): The name of the state to search for.
    

    Returns:
        None
    """
    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Define the SQL query with placeholders and execute it
    query = "SELECT * FROM states WHERE name = %s ORDER BY states.id ASC LIMIT 1"
    cursor.execute(query, (state_name,))
    # Fetch the result and print it
    states = cursor.fetchall()

    for state in states:
        print(state)

    # Close the cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 5:
        print("Usage: python script.py <username> <password> <database>"
              "<state_name>")
        sys.exit(1)

    # Extract command-line arguments
    username, password, database, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    # Call the filter_states function with the provided arguments
    filter_states(username, password, database, state_name)
