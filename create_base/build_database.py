# -*- coding: utf-8 -*-
import os
from create_base.config import db
from create_base.models import Person
from faker import Faker
fake = Faker('ru_Ru')
# Data to initialize database with
PEOPLE=[]
for i in range(30):
    fio = fake.name()
    birthday = fake.date_of_birth(tzinfo=None, minimum_age=20, maximum_age=65)
    employment = fake.date_this_century(before_today=True, after_today=False)
    office = fake.job()
    PEOPLE.append({'fio': fio,'birthday': birthday,'office': office,'employment': employment, })

# Delete database file if it exists currently
if os.path.exists("people.db"):
    os.remove("people.db")

# Create the database
db.create_all()

# iterate over the PEOPLE structure and populate the database
for person in PEOPLE:
    p = Person(fio=person.get("fio"), birthday=person.get("birthday"), office=person.get("office"), employment=person.get("employment") )
    db.session.add(p)

db.session.commit()
