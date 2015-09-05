# -*- coding: utf8 -*-
from flask import Blueprint


def getBlueprint(config):
    app = Blueprint('jobs', __name__)

    @app.route('/jobs', methods=['GET'])
    def get():
        return str({"var": "foo"})

    return app
