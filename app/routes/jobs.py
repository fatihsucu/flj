# -*- coding: utf8 -*-
from flask import Blueprint
from app.libraries import response


def getBlueprint(config):
    app = Blueprint('jobs', __name__)

    @app.route('/jobs', methods=['GET'])
    def get():
        return response.make(20, {"jobs": [
              {
                "date": "2015-04-25 15:30:12",
                "title": "Receptionist - Fluent French Speaker",
                "description": """
At Snowcoach Holidays, we are looking for experienced French speakers to work at one of our Club Hotels in the French Alps. Friendly, warm and relatable are all key words to best describe you. This position has the potential to be year round for the right applicant so if you are looking to live the French lifestyle, then apply right now""",
                "company": "Snowcoach Holidays",
                "location": {
                    "country": "United Kingdom",
                    "state": "",
                    "city": "London",
                    "region": "Westcost",
                    "lat": 412,
                    "long": 121,
                    },
                "salary": "Competitive + Benefits",
                "jobType": "Contract/Interim",
                "stats": {
                  "view": 10,
                  "starred": 4
                }
              }
            ]})

    return app
