# SQL Introduction Project

## Introduction
This project is designed to introduce you to the fundamentals of SQL using MySQL. It covers various concepts, including databases, SQL statements, and basic queries. The goal is to help you understand key aspects of working with databases and MySQL.

## Learning Objectives
By the end of this project, you should be able to:

- Explain what a database is
- Understand the concept of a relational database
- Define SQL and its role
- Familiarize yourself with MySQL
- Create and manipulate databases and tables
- Execute SQL statements for data retrieval, insertion, updating, and deletion
- Work with subqueries and MySQL functions

## Project Structure
The project is organized into several tasks, each focusing on a specific aspect of SQL. The tasks are as follows:

1. **List Databases**
   - Script: `0-list_databases.sql`
   - Description: Lists all databases on the MySQL server.

2. **Create a Database**
   - Script: `1-create_database_if_missing.sql`
   - Description: Creates the database 'hbtn_0c_0' if it doesn't already exist.

3. **Delete a Database**
   - Script: `2-remove_database.sql`
   - Description: Deletes the database 'hbtn_0c_0' if it exists.

4. **List Tables**
   - Script: `3-list_tables.sql`
   - Description: Lists all tables in a specified database.

5. **First Table**
   - Script: `4-first_table.sql`
   - Description: Creates a table called 'first_table' with specified columns.

6. **Full Description**
   - Script: `5-full_table.sql`
   - Description: Prints the full description of 'first_table'.

7. **List All in Table**
   - Script: `6-list_values.sql`
   - Description: Lists all rows of 'first_table'.

8. **First Add**
   - Script: `7-insert_value.sql`
   - Description: Inserts a new row into 'first_table'.

9. **Count 89**
   - Script: `8-count_89.sql`
   - Description: Displays the number of records with id = 89 in 'first_table'.

10. **Full Creation**
   - Script: `9-full_creation.sql`
   - Description: Creates a table 'second_table' and adds multiple rows.

11. **List by Best**
   - Script: `10-top_score.sql`
   - Description: Lists all records in 'second_table' ordered by score.

12. **Select the Best**
   - Script: `11-best_score.sql`
   - Description: Lists records with a score >= 10 in 'second_table'.

13. **Cheating is Bad**
   - Script: `12-no_cheating.sql`
   - Description: Updates the score of 'Bob' to 10 in 'second_table'.

14. **Score Too Low**
   - Script: `13-change_class.sql`
   - Description: Removes records with a score <= 5 in 'second_table'.

15. **Average**
   - Script: `14-average.sql`
   - Description: Computes the score average of all records in 'second_table'.

16. **Number by Score**
   - Script: `15-groups.sql`
   - Description: Lists the number of records for each score in 'second_table'.

17. **Say My Name**
   - Script: `16-no_link.sql`
   - Description: Lists all records in 'second_table' with names and scores.

## Getting Started
To execute these scripts, make sure you have MySQL 8.0 installed on Ubuntu 20.04 LTS. Use the provided commands to connect to the MySQL server and run the scripts.

```bash
$ cat script.sql | mysql -hlocalhost -uroot -p
```
