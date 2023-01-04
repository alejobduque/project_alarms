import json
from flask import Blueprint, jsonify, request
from services.alarm_service import AlarmService

alarm_routes = Blueprint('alarm', __name__)


@alarm_routes.route('/get_alarms')
def get_alarms():
    body = request.json
    start_date = body.get("start_date")
    end_date = body.get("end_date")
    data = []
    if start_date and end_date:
        data = AlarmService().get_alarms(
            start_date=start_date,
            end_date=end_date
        )

    return jsonify(data)


@alarm_routes.route('/add_alarms', methods=['POST'])
def add_alarms():
    body = request.json
    data = []
    if body:
        data = AlarmService().add_alarms(alarms=body)

    return jsonify(data)


@alarm_routes.route('/delete_alarms', methods=['PUT'])
def delete_alarms():
    body = request.json
    date = body.get("date")
    oldest = body.get("oldest")
    data = False
    if date and oldest is not None:
        result = AlarmService().delete_alarms(date=date, oldest=oldest)

    return jsonify({"result": result})
