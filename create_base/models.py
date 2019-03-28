from create_base.config import db


class Person(db.Model):
    __tablename__ = 'person'
    person_id = db.Column(db.Integer, primary_key=True)
    fio = db.Column(db.String(32))
    birthday = db.Column(db.DateTime)
    office = db.Column(db.String(32))
    employment = db.Column(db.DateTime)