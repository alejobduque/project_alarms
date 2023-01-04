from flask import jsonify


def page_not_found(error):
    return jsonify({'Message': 'Page not found!'}), 404


def method_not_allowed(error):
    return jsonify({'Message': 'Method not allowed!'}), 405
