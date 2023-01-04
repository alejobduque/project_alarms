from models.models import Alarm, db
from sqlalchemy import or_, and_

from constants import Constants
from utils.generals_utils import GeneralsUtils


class AlarmService:

    def get_alarms(self, start_date: str, end_date: str):
        try:
            result_query = db.session.query(Alarm).filter(or_(
                and_(start_date >= Alarm.start_date,
                     start_date <= Alarm.end_date),
                and_(end_date >= Alarm.start_date,
                     end_date <= Alarm.end_date),
                and_(start_date < Alarm.start_date,
                     end_date > Alarm.end_date)),
                and_(Alarm.is_delete == False)).all()

            data = GeneralsUtils.translate_response_query(
                Constants.COLUMNS_ALARM, result_query)
        except Exception as e:
            data = {
                "Message error": e
            }

        return data

    def add_alarms(self, alarms: list):
        if any(self.validate_alarm(alarm) for alarm in alarms):
            raise Exception("There are alarms within values requireds")

        names = []
        ids = []
        try:
            for alarm in alarms:
                alarm_name = alarm.get("alarm_name")
                if not self.get_ids_by_name(alarm_name):
                    names.append(alarm_name)
                    alarm_to_insert = Alarm(**alarm)
                    db.session.add(alarm_to_insert)
                    db.session.commit()
                    ids.append(alarm_to_insert.id)

        except:
            raise Exception("Fail to create alarms")

        return ids

    def delete_alarms(self, date: str, oldest: bool):
        data = True
        try:
            if oldest:
                result_query = db.session.query(Alarm).\
                    filter((Alarm.start_date <= date)).all()
            else:
                result_query = db.session.query(Alarm).\
                    filter((Alarm.start_date >= date)).all()

            for alarm in result_query:
                alarm.is_delete = True

            db.session.commit()
        except Exception as e:
            data = {
                "Message error": e
            }

        return data

    def validate_alarm(self, alarm: dict):
        if not alarm.get("alarm_name") or not alarm.get("start_date"):
            return True

        return False

    def get_ids_by_name(self, names: list):
        if not isinstance(names, list):
            names = [names]

        try:
            result_query = db.session.query(Alarm.id).\
                filter(Alarm.alarm_name.in_(names))
        except:
            raise Exception("Fail to get alarms ids")

        result = [row.id for row in result_query]

        return result
