import json


class ConfigurationUtils:

    @staticmethod
    def get_config(config: str):
        data = None
        if not config:
            return data

        with open("config.json", "r") as file:
            data = json.load(file)

        data = data[config]

        return data
