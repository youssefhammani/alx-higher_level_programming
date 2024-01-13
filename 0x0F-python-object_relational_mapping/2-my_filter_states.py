#!/usr/bin/python3
"""
Displays all values in the states table of
hbtn_0e_0_usa where name matches the argument
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Check if the number of arguments is correct
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> \
                <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    # Connection parameters
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server at localhost:3306
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database, charset="utf8")

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Use format to create the SQL query with user input
    query = "SELECT * FROM states\
            WHERE states.name = '{}'\
            ORDER BY states.id ASC;".format(state_name)
    cursor.execute(query)

    # Fetch all the rows and display the results
    results = cursor.fetchall()
    for row in results:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
