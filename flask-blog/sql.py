# MODEL - SQLite3 table

import sqlite3

# create a new db if db doesnt exist
with sqlite3.connect("blog.db") as connection:

    # get cursor object used to execute SQL commands
    c = connection.cursor()

    # create table
    c.execute("""CREATE TABLE posts(title TEXT, post TEXT)""")

    # insert dummy data into the table
    c.execute('INSERT INTO posts VALUES("Good", "I\'m good.")')
    c.execute('INSERT INTO posts VALUES("Well", "I\'m well.")')
    c.execute('INSERT INTO posts VALUES("Excellent", "I\'m excellent.")')
    c.execute('INSERT INTO posts VALUES("Okay", "I\'m okay.")')
