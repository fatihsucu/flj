# -*- coding: utf8 -*-
from flask import Blueprint
from app.libraries import response


def getBlueprint(config):
    app = Blueprint('accounts', __name__)

    @app.route('/accounts', methods=['GET'])
    def get():
        return response.make(20, {"accounts": [
              {
                "createdAt": "2015-04-25 12:30:12",
                "lastLogin": "2015-04-25 15:41:27",
                "fname": "Mustafa",
                "lname": "Atik",
                "email": "mm@aasscsaccccmm.com",
                "gcmId": None,
                "alarms": [
                    {
                        "createdAt": "2015-04-25 15:30:12",
                        "location": {
                            "country": "United Kingdom",
                            "state": "",
                            "city": "London",
                            },
                        "keywords": [
                            "speaker",
                            "scientist",
                            "developer"
                        ]
                    }
                ]
              }
            ]})

    return app
