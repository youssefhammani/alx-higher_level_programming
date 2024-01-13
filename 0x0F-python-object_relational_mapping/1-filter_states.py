#!/usr/bin/python3
"""
Lists all states with a name starting with N (upper N)
It takes 3 arguments: mysql username, mysql password and database name
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Connection parameters
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server at localhost:3306
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database, charset="utf8")

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the query to select states starting with 'N'
    query = "SELECT * FROM states\ 
             WHERE name LIKE 'N%' ORDER BY id ASC;"
    cursor.execute(query)

    # Fetch all the rows and display the results
    results = cursor.fetchall()
    for row in results:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
