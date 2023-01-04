from flask import Flask

from models.models import db
from utils.configuration_utils import ConfigurationUtils
from validations import page_not_found, method_not_allowed
from views.alarm import alarm_routes


sqlalchemy_database_uri =\
    ConfigurationUtils.get_config("POSTGRESQL_DB_ALARM")
sqlalchemy_track_modifications =\
    ConfigurationUtils.get_config("NOTIFICATIONS_SQLALCHEMY")
debug = ConfigurationUtils.get_config("DEBUG")
port = ConfigurationUtils.get_config("PORT")

app = Flask(__name__)
app.register_blueprint(alarm_routes)

app.config['SQLALCHEMY_DATABASE_URI'] = sqlalchemy_database_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = sqlalchemy_track_modifications

db.init_app(app)


if __name__ == '__main__':
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(405, method_not_allowed)
    app.run(debug=debug, port=port)
