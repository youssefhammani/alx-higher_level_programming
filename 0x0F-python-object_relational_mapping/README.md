# Object-Relational Mapping with Python

## Overview

This repository is dedicated to showcasing the implementation of Object-Relational Mapping (ORM) in Python, specifically focusing on connecting to a MySQL database. ORM enables a seamless abstraction of storage details from the code, facilitating the manipulation of data using Python objects. The primary library used for ORM in this project is SQLAlchemy.

## Prerequisites

### Ensure that the following dependencies are met:

* Python 3.8.5
* MySQL server 8.0
* MySQLdb version 2.0.x
* SQLAlchemy version 1.4.x

## Setup Guide

1. **Install the Python virtual environment:**

```bash
$ sudo apt-get install python3.8-venv
$ python3 -m venv venv
$ source venv/bin/activate
```

2. **Install MySQLdb:**

```bash
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
```

3. **Install SQLAlchemy:**

```bash
$ sudo pip3 install SQLAlchemy
```

4. **Clone the repository:**

```bash
$ git clone https://github.com/your_username/your_repository.git
$ cd your_repository/0x0F-python-object_relational_mapping
```

## Project Structure

* `0-select_states.py:`			Lists all states from the database.
* `1-filter_states.py:` 		Lists states with a name starting with 'N'.
* `2-my_filter_states.py:` 		Lists states based on user input safely.
* `3-my_safe_filter_states.py:`		Lists states based on user input, preventing SQL injection.
* `4-cities_by_state.py:` 		Lists all cities from the database along with their respective states.
* `5-filter_cities.py:` 		Lists all cities of a specific state based on user input.
* `6-model_state.py:` 			Defines the State class and creates the corresponding table in the database.
* `7-model_state_fetch_all.py:` 	Lists all State objects from the database.
* `8-model_state_fetch_first.py:` 	Prints the first State object from the database.
* `9-model_state_filter_a.py:` 		Lists all State objects containing the letter 'a'.
* `10-model_state_my_get.py:` 		Prints the ID of a State object based on user input.
* `11-model_state_insert.py:` 		Adds a new State object to the database.
* `12-model_state_update_id_2.py:` 	Updates the name of a State object with ID 2.
* `13-model_state_delete_a.py:` 	Deletes all State objects with a name containing the letter 'a'.
* `model_state.py:`			Contains the definition of the State class and Base instance.
* `model_city.py:`			Contains the definition of the City class.

## Usage

- To execute any script, utilize the following format:

```bash
$ ./script_name.py <mysql_username> <mysql_password> <database_name> [additional_arguments]
```

* Replace the placeholders with actual values.

## Conclusion

- This project provides a comprehensive exploration of utilizing Python and SQLAlchemy for Object-Relational Mapping, offering an effective approach to interact with a MySQL database.
