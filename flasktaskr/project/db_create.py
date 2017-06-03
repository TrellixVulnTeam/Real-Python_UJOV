# sets and creates the database

from views import db
from models import Task
from datetime import date



# create the database and the db table
db.create_all()

#insert data
# db.session.add(Task("Finish all assignments", date(2017, 8, 21), 10, 1))
# db.session.add(Task("Go for a haircut", date(2017, 11, 12), 10, 1))

# commit the changes
db.session.commit()
