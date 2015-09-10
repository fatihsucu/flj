# -*- coding: utf8 -*-
from flask import Blueprint
from app.libraries import response
from app.modules.accounts import Accounts
from app.modules.errors import BaseException, NotFoundException


def getBlueprint(config):
    app = Blueprint('accounts', __name__)

    @app.route('/accounts/<gcmId>', methods=['GET'])
    def getByGcm(gcmId):
        try:
            account = Accounts(config).getByGcm(gcmId)
            result = response.make(20, {"account": account})
        except Exception, e:
            result = response.makeRaw(30, e.message)

        return result

    @app.route('/dummies/accounts', methods=['GET'])
    def getDummies():
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
