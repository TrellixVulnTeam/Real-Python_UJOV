# EXAMPLE APPLICATION - INSERT RANDOM DATA

import sqlite3
import random

with sqlite3.connect("newnum.db") as connection:
    c = connection.cursor()

    # delete database if table exists
    c.execute("DROP TABLE if exists numbers")

    # create db table
    c.execute("CREATE TABLE numbers(num int)")

    # insert each number to the db
    for i in range(100):
        c.execute("INSERT INTO numbers VALUES(?)", (random.randint(0, 100), ))
    
