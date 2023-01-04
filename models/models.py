from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_, and_
from sqlalchemy.sql import select

db = SQLAlchemy()


class Alarm(db.Model):
    __str__ = "alarm"

    id = db.Column(db.Integer, primary_key=True)
    alarm_name = db.Column(db.String(30), unique=True, nullable=False)
    comment = db.Column(db.String(40))
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date)
    start_date_utc = db.Column(db.DateTime)
    end_date_utc = db.Column(db.DateTime)
    is_delete = db.Column(db.Integer)

    def __init__(
            self,
            alarm_name: str,
            start_date: str,
            comment=None,
            end_date=None,
            start_date_utc=None,
            end_date_utc=None,
            is_delete=False):
        self.alarm_name = alarm_name
        self.start_date = start_date
        self.comment = comment
        self.end_date = end_date
        self.start_date_utc = start_date_utc
        self.end_date_utc = end_date_utc
        self.is_delete = is_delete
