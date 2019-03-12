from datetime import datetime, date
from config import db, ma


class Person(db.Model):
    __tablename__ = 'person'
    person_id = db.Column(db.Integer, primary_key=True)
    fio = db.Column(db.String(32))
    birthday = db.Column(db.DateTime)
    office = db.Column(db.String(32))
    employment = db.Column(db.DateTime)
#'%Y-%m-%d'

class PersonSchema(ma.ModelSchema):
    class Meta:
        model = Person
        sqla_session = db.session
