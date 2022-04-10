from db import db
from datetime import datetime
import re

class PlateModel(db.Model):
    __tablename__ = 'plates'

    id = db.Column(db.Integer, primary_key=True)
    plate = db.Column(db.String(20))
    owner = db.Column(db.String(40), default="")
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)

    def __init__(self, plate, owner, start_date, end_date):
        self.plate = plate
        if owner is None:
            self.owner = ""
        else:
            self.owner = owner
        self.start_date = start_date
        self.end_date = end_date

    def json(self):
        return {'plate': self.plate, 'owner': self.owner, 'start_date': self.start_date, 'end_date': self.end_date}

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns if not c.name == 'id'}

    @classmethod
    def find_by_plate(cls, plate):
        return cls.query.filter_by(plate=plate).first()

    @classmethod
    def find_by_owner(cls, owner):
        return cls.query.filter_by(owner=owner).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def is_valid(self):
        if self.plate.strip():
            return True
        else:
            return False

    def check_chars(self, chars, max_length):
        if chars.isalpha() and len(chars) <= max_length:
            return True
        else:
            return False

    def check_digits(self, digits, max_length):
        if digits.isnumeric() and len(digits) <= max_length and not digits[0] == '0':
            return True
        else:
            return False

class PlateValidation(PlateModel, db.Model):

    def is_valid(self):
        splits = re.split('(\d+|-)', self.plate)

        if not splits and len(splits) > 4:
            return False

        else:
            return self.check_chars(splits[0], 3) and splits[1] == "-" and self.check_chars(splits[2], 2) and self.check_digits(splits[3], 4)