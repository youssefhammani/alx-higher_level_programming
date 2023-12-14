# Project Title: SQL Mastery

## Overview

Welcome to SQL Mastery, a comprehensive project focused on advanced SQL queries using MySQL. Whether you're a beginner looking to enhance your SQL skills or an experienced developer seeking to master complex database queries, this project is designed to guide you through the intricacies of SQL.

## Learning Objectives

By completing this project, you will:

- Develop proficiency in user management and database creation with MySQL.
- Understand and implement various constraints, including PRIMARY KEY, FOREIGN KEY, NOT NULL, and UNIQUE.
- Master the art of retrieving data from multiple tables using JOIN and UNION operations.
- Learn to write subqueries for handling complex database queries.
- Gain expertise in managing privileges for MySQL users.

## Technologies Used

- SQL
- MySQL

# More Info

## Comments for your SQL file:

```bash
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
```

## Install MySQL 8.0 on Ubuntu 20.04 LTS

```bash
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$
```

_**Connect to your MySQL server:**_

```bash
$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
mysql> quit
Bye
$
```

## Use “container-on-demand” to run MySQL

_**In the container, credentials are `root/root`**_

- Ask for container `Ubuntu 20.04`
- Connect via SSH
- OR connect via the Web terminal
- In the container, you should start MySQL before playing with it:

```bash
$ service mysql start                                                   
 * Starting MySQL database server mysqld 
$
$ cat 0-list_databases.sql | mysql -uroot -p                               
Database                                                                                   
information_schema                                                                         
mysql                                                                                      
performance_schema                                                                         
sys                      
$
```

In the container, credentials are `root/root`

## How to import a SQL dump

```bash
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password: 
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$
```

## Table of Contents

0. [My Privileges](#0-my-privileges)
   - Lists all privileges of MySQL users user_0d_1 and user_0d_2 on the localhost.
1. [Root User](#1-root-user)
    - Creates the MySQL server user user_0d_1 with all privileges.
2. [Read User](#2-read-user)
    - Creates the database hbtn_0d_2 and the user user_0d_2 with SELECT privilege.
3. [Always a Name](#3-always-a-name)
    - Creates the table force_name with an ID and a non-null name in a specified database.
4. [ID Can't be Null](#4-id-cant-be-null)
    - Creates the table id_not_null with a default value for ID and a name in a specified database.
5. [Unique ID](#5-unique-id)
    - Creates the table unique_id with a unique ID and a name in a specified database.
6. [States Table](#6-states-table)
    - Creates the database hbtn_0d_usa and the table states with unique IDs and names.
7. [Cities Table](#7-cities-table)
    - Creates the table cities with unique IDs, state IDs as foreign keys, and names.
8. [Cities of California](#8-cities-of-california)
    - Lists all cities of California without using JOIN.
9.  [Cities by States](#9-cities-by-states)
    - Lists all cities and their states using JOIN.
10. [Genre ID by Show](#10-genre-id-by-show)
    - Lists shows with at least one linked genre.
11. [Genre ID for All Shows](#11-genre-id-for-all-shows)
    - Lists all shows and their linked genres.
12. [No Genre](#12-no-genre)
    - Lists shows without a linked genre.
13. [Number of Shows by Genre](#13-number-of-shows-by-genre)
    - Displays the number of shows linked to each genre.
14. [My Genres](#14-my-genres)
    - Lists all genres of the show Dexter.
15. [Only Comedy](#15-only-comedy)
    - Lists all Comedy shows.
16. [List Shows and Genres](#16-list-shows-and-genres)
    - Lists all shows and their linked genres.
17. [Not My Genre](#17-not-my-genre)
    - Lists genres not linked to the show Dexter.
18. [No Comedy Tonight!](#18-no-comedy-tonight)
    - Lists shows without the genre Comedy.
19. [Rotten Tomatoes](#19-rotten-tomatoes)
    - Lists shows from hbtn_0d_tvshows_rate by their rating.
20. [Rating Genres](#20-rating-genres)
    - Import the database dump from hbtn_0d_tvshows_rate to your MySQL server, then execute a script to list genres in hbtn_0d_tvshows_rate along with their rating sums. Results are sorted by rating.

## Getting Started

1. Install MySQL 8.0 on Ubuntu 20.04 LTS using the provided instructions.
2. Connect to your MySQL server using `sudo mysql`.

# SQL Scripts

## 0. [My Privileges](./0-privileges.sql)

Lists all privileges of MySQL users `user_0d_1` and `user_0d_2` on the localhost.

### Query Explanation

This SQL script retrieves and displays the privileges assigned to `user_0d_1` and `user_0d_2` on the localhost.

### Usage

Execute the script using the MySQL command-line tool:

```bash
$ cat 0-privileges.sql | mysql -hlocalhost -uroot -p
```

## 1. [Root User](./1-create_user.sql)

Creates the MySQL server user `user_0d_1` with all privileges.

### Query Explanation

This SQL script creates a MySQL user named `user_0d_1` with all privileges on the server. The user will have administrative access to the MySQL server.

### Usage

Execute the script using the MySQL command-line tool:

```bash
$ cat 1-create_user.sql | mysql -hlocalhost -uroot -p
```

## 2. [Read User](./2-create_read_user.sql)

Creates the database `hbtn_0d_2` and the user `user_0d_2` with SELECT privilege.

### Query Explanation

This SQL script performs two actions:
1. Creates the database `hbtn_0d_2`.
2. Creates a MySQL user named `user_0d_2` with the privilege to SELECT data from the specified database.

### Usage

Execute the script using the MySQL command-line tool:

```bash
$ cat 2-create_read_user.sql | mysql -hlocalhost -uroot -p
```

## 3. [Always a Name](./3-force_name.sql)

Creates the table `force_name` with an ID and a non-null name in a specified database.

### Query Explanation

This SQL script creates a table named `force_name` with the following attributes:
- `ID`: An identifier for each record.
- `name`: A non-null field to ensure that every record has a name.

### Usage

Execute the script using the MySQL command-line tool:

```bash
$ cat 3-force_name.sql | mysql -hlocalhost -uroot -p
```

## 4. [ID Can't be Null](./4-never_empty.sql)

Creates the table `id_not_null` with a default value for ID and a name in a specified database.

### Query Explanation

This SQL script creates a table named `id_not_null` with the following attributes:
- `ID`: An identifier for each record, set to a default value to ensure it is never null.
- `name`: A field for storing names.

### Usage

Execute the script using the MySQL command-line tool:

```bash
$ cat 4-never_empty.sql | mysql -hlocalhost -uroot -p
```

## 5. [Unique ID](./5-unique_id.sql)

Creates the table `unique_id` with a unique ID and a name in a specified database.

### Query Explanation

This SQL script creates a table named `unique_id` with the following attributes:
- `ID`: An identifier for each record, set to ensure its uniqueness within the table.
- `name`: A field for storing names.

### Usage

Execute the script using the MySQL command-line tool:

```bash
$ cat 5-unique_id.sql | mysql -hlocalhost -uroot -p
```

## 6. [States Table](./6-states.sql)

Creates the database `hbtn_0d_usa` and the table `states` with unique IDs and names.

### Query Explanation

This SQL script creates a database named `hbtn_0d_usa` and a table named `states` with the following attributes:
- `ID`: A unique identifier for each state.
- `name`: The name of the state.

### Usage

Execute the script using the MySQL command-line tool:

```bash
$ cat 6-states.sql | mysql -hlocalhost -uroot -p
```

## 7. [Cities Table](./7-cities.sql)

Creates the table `cities` with unique IDs, state IDs as foreign keys, and names.

### Query Explanation

This SQL script creates a table named `cities` with the following attributes:
- `ID`: A unique identifier for each city.
- `state_ID`: A foreign key referencing the `ID` column in the `states` table.
- `name`: The name of the city.

### Usage

Execute the script using the MySQL command-line tool:

```bash
$ cat 7-cities.sql | mysql -hlocalhost -uroot -p
```

## 8. [Cities of California](./8-cities_of_california_subquery.sql)

Lists all cities of California without using JOIN.

### Query Explanation

This SQL script retrieves and displays all cities located in California without utilizing the JOIN operation.

### Usage

Execute the script using the MySQL command-line tool:

```bash
$ cat 8-cities_of_california_subquery.sql | mysql -hlocalhost -uroot -p
```

## 9. [Cities by States](./9-cities_by_state_join.sql)

Lists all cities and their states using JOIN.

### Query Explanation

This SQL script retrieves and displays a list of all cities along with their corresponding states using the JOIN operation.

### Usage

Execute the script using the MySQL command-line tool:

```bash
$ cat 9-cities_by_state_join.sql | mysql -hlocalhost -uroot -p
```

## 10. [Genre ID by Show](./10-genre_id_by_show.sql)

Lists shows with at least one linked genre.

### Query Explanation

This SQL script retrieves and displays a list of shows that have at least one linked genre.

### Usage

Execute the script using the MySQL command-line tool:

```bash
$ cat 10-genre_id_by_show.sql | mysql -hlocalhost -uroot -p
```

## 11. [Genre ID for All Shows](./11-genre_id_all_shows.sql)

Lists all shows and their linked genres.

### Query Explanation

This SQL script retrieves and displays a list of all shows along with their linked genres.

### Usage

Execute the script using the MySQL command-line tool:

```bash
$ cat 11-genre_id_all_shows.sql | mysql -hlocalhost -uroot -p
```

## 12. [No Genre](./12-no_genre.sql)

Lists shows without a linked genre.

### Query Explanation

This SQL script retrieves and displays a list of shows that do not have a linked genre.

### Usage

Execute the script using the MySQL command-line tool:

```bash
$ cat 12-no_genre.sql | mysql -hlocalhost -uroot -p
```

## 13. [Number of Shows by Genre](./13-count_shows_by_genre.sql)

Displays the number of shows linked to each genre.

### Query Explanation

This SQL script retrieves and displays the count of shows linked to each genre.

### Usage

Execute the script using the MySQL command-line tool:

```bash
$ cat 13-count_shows_by_genre.sql | mysql -hlocalhost -uroot -p
```

## 14. [My Genres](./14-my_genres.sql)

Lists all genres of the show Dexter.

### Query Explanation

This SQL script retrieves and displays all genres associated with the show Dexter.

### Usage

Execute the script using the MySQL command-line tool:

```bash
$ cat 14-my_genres.sql | mysql -hlocalhost -uroot -p
```

## 15. [Only Comedy](./15-comedy_only.sql)

Lists all Comedy shows.

### Query Explanation

This SQL script retrieves and displays all shows categorized as Comedy.

### Usage

Execute the script using the MySQL command-line tool:

```bash
$ cat 15-comedy_only.sql | mysql -hlocalhost -uroot -p
```

## 16. [List Shows and Genres](./16-shows_by_genre.sql)

Lists all shows and their linked genres.

### Query Explanation

This SQL script retrieves and displays a list of all shows along with their linked genres.

### Usage

Execute the script using the MySQL command-line tool:

```bash
$ cat 16-shows_by_genre.sql | mysql -hlocalhost -uroot -p
```

## 17. [Not My Genre](./100-not_my_genres.sql)

Lists genres not linked to the show Dexter.

### Query Explanation

This SQL script retrieves and displays genres that are not linked to the show Dexter.

### Usage

Execute the script using the MySQL command-line tool:

```bash
$ cat 100-not_my_genres.sql | mysql -hlocalhost -uroot -p
```

## 18. [No Comedy Tonight!](./101-not_a_comedy.sql)

Lists shows without the genre Comedy.

### Query Explanation

This SQL script retrieves and displays shows that are not classified under the Comedy genre.

### Usage

Execute the script using the MySQL command-line tool:

```bash
$ cat 101-not_a_comedy.sql | mysql -hlocalhost -uroot -p
```

## 19. [Rotten Tomatoes](./102-rating_shows.sql)

Lists shows from `hbtn_0d_tvshows_rate` by their rating.

### Query Explanation

This SQL script retrieves and displays shows from the `hbtn_0d_tvshows_rate` table along with their ratings.

### Usage

Execute the script using the MySQL command-line tool:

```bash
$ cat 102-rating_shows.sql | mysql -hlocalhost -uroot -p
```

## 20. [Rating Genres](./103-rating_genres.sql)

Imports the database dump from `hbtn_0d_tvshows_rate` to your MySQL server and lists all genres by their rating.

### Prerequisites

[Download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows_rate.sql) the database dump file (same as 102-rating_shows.sql).

### Query Explanation

This SQL script imports the database dump to your MySQL server and lists all genres in the `hbtn_0d_tvshows_rate` database by their rating. Each record displays the genre name and the sum of ratings, sorted in descending order by rating.

### Usage

Execute the script using the MySQL command-line tool:

```bash
$ cat 103-rating_genres.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows_rate
```

# Connecting to MySQL Server

To connect to the MySQL server and access the database named "hbtn_0d_tvshows_rate" on the local machine, use the following command:

```bash
$ mysql -hlocalhost -uroot -p hbtn_0d_tvshows_rate
```

- **`-h :`** Specifies the host (in this case, "localhost").
- **`-u :`** Specifies the MySQL user (in this case, "root").
- **`-p :`** Prompts for the MySQL user's password.
- **`hbtn_0d_tvshows_rate :`** Specifies the name of the MySQL database you want to connect to.


After entering this command, you will be prompted to enter the password for the MySQL user specified with the -u flag. Once the correct password is provided, you will be connected to the MySQL server and have access to the "hbtn_0d_tvshows_rate" database.
