# HOMEWORK - insert into cars db

# import the sqlite3 library
import sqlite3

# create the connection object
conn = sqlite3.connect("cars.db")

# get a cursor object used to execute SQL commands
cursor = conn.cursor()

# insert data
cursor.execute("INSERT INTO inventory VALUES('Ford', 'Focus', 8600)")
cursor.execute("INSERT INTO inventory VALUES('Ford', 'Mondeo', 23400)")
cursor.execute("INSERT INTO inventory VALUES('Ford', 'Fiesta', 77800)")
cursor.execute("INSERT INTO inventory VALUES('Honda', 'Civic', 239)")
cursor.execute("INSERT INTO inventory VALUES('Honda', 'Accord', 12234)")

# commit the changes
conn.commit()

# close the database connection
conn.close()
