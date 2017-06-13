# sets and creates the database
from datetime import date

from project import db
from project.models import Task, User




# create the database and the db table
db.create_all()

#insert data
db.session.add(
    User("admin", "admin.com" "admin", "admin")
)
db.session.add(
    Task("Finish all assignments", date(2017, 8, 21), 10, date(2015, 2, 13), 1, 1)
)
db.session.add(
    Task("Go for a haircut", date(2017, 11, 12), 10, date(2015, 2, 13), 1, 1)
)

# commit the changes
db.session.commit()
