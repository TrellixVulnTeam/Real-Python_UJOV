# HOMEWORK

import sqlite3


# Create a new database called cars
conn = sqlite3.connect("cars.db")

# get a cursor object used to execute SQL commands
cursor = conn.cursor()

# create table
cursor.execute("""CREATE TABLE inventory(
                Make TEXT, Model TEXT, Quantity INT)
                """)

# close the db connection
conn.close()
