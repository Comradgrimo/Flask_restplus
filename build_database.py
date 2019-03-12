# -*- coding: utf-8 -*-
from datetime import datetime, date
import os
from config import db
from models import Person

# Data to initialize database with
PEOPLE = [
    {"fio": "Иванов И.И", "birthday": datetime.strptime('11-01-1965', '%d-%m-%Y'), "office": "Инженер",  "employment": datetime.strptime('10-10-2001', '%d-%m-%Y')},
    {"fio": "Петров П.П", "birthday": datetime.strptime('06-10-1985', '%d-%m-%Y'), "office": "Уборщик", "employment": datetime.strptime('12-07-2003', '%d-%m-%Y')},
    {"fio": "Сидоров С.С", "birthday": datetime.strptime('21-07-1991', '%d-%m-%Y'), "office": "Главбух", "employment": datetime.strptime('21-09-2005', '%d-%m-%Y')},
]

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
