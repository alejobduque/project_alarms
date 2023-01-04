from constants import Constants
from datetime import datetime


class GeneralsUtils:

    @staticmethod
    def translate_response_query(entity: dict, result: list):
        data = []
        for row in result:
            try:
                data.append({
                    column["name"]: GeneralsUtils.
                    format_date(getattr(row, column["name"]))
                    if column["type"] == "date" else
                    getattr(row, column["name"])

                    for column in entity
                })
            except:
                continue

        return data

    @staticmethod
    def format_date(value):
        result = ""
        if value:
            try:
                result = datetime.strftime(value, Constants.FORMAT_DATE)
            except:
                print("Not's possible to format date")
                pass

        return result
