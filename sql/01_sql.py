# Create a SQLite3 database and table


# import the sqlite3 library
import sqlite3

# create a new database if the db doesnt exist
conn = sqlite3.connect("new.db")

# get a cursor object used to execute SQL commands
cursor = conn.cursor()

# create table
cursor.execute("""CREATE TABLE population
                (city TEXT, state TEXT, population INT)
                """)

# close the db connection
conn.close()
