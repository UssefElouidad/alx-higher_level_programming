import MySQLdb
import sys


def list_states_starting_with_N(username, password, database):
    """
     a script that connects to a MySQL server and retrieves states with names
     starting with 'N' from the 'states' table.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): MySQL database name.

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

    cursor.execute(
        "SELECT * FROM states"
        "WHERE name LIKE 'N%' "
        "ORDER BY states.id ASC"
    )
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    list_states_starting_with_N(username, password, database)
