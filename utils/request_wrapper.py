from flask import jsonify


class RequestWrapper(object):

    def __init__(self, function):
        self.function = function

    def __call__(self):
        response = {}
        DATA_KEY = "data"
        DETAIL_KEY = "details"
        fail = False

        try:
            result = self.function()
        except Exception as e:
            fail = True
            detail = {
                "error": e
            }

        if isinstance(result, dict) and not fail:
            if DATA_KEY in result:
                response[DATA_KEY] = result[DATA_KEY]

            if DETAIL_KEY in result:
                response[DETAIL_KEY] = result[DETAIL_KEY]
        elif not fail:
            response[DATA_KEY] = result

        if fail:
            response = {
                DATA_KEY: [],
                DETAIL_KEY: list(detail)
            }

        return jsonify(response)
