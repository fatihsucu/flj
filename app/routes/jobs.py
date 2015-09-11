# -*- coding: utf8 -*-
from flask import Blueprint, jsonify
from app.libraries import response
from app.libraries.routerDecorators import jsonizeRequest
from app.modules.accounts import Accounts
from app.modules.jobs import Jobs
from bson.objectid import ObjectId


def getBlueprint(config):
    app = Blueprint("jobs", __name__)

    def toggleJobStar(accountId, data, method):
        try:
            jobId = ObjectId(data["job"]["id"])
        except Exception, e:
            raise WrongArgumentException(
                "job id not found in the request body")

        accounts = Accounts(config)
        account = accounts.getOne(accountId)
        if method == "insertStarredJob":
            if jobId in account.get("jobs", {}).get("starred", []):
                return
        getattr(accounts, method)(account["id"], jobId)

    @app.route("/jobs/<accountId>/starred/", methods=["PUT"])
    @jsonizeRequest
    def putStarredJobs(accountId, data):
        toggleJobStar(accountId, data, "insertStarredJob")
        return jsonify(response.make(20).__json__())

    @app.route("/jobs/<accountId>/starred/", methods=["DELETE"])
    @jsonizeRequest
    def deleteStarredJobs(accountId, data):
        toggleJobStar(accountId, data, "removeStarredJob")
        return jsonify(response.make(20).__json__())

    @app.route("/jobs/<accountId>/starred/", methods=["GET"])
    def getStarredJobs(accountId):
        account = Accounts(config).getOne(accountId)
        starredIds = account.get("jobs", {}).get("starred", [])
        if starredIds:
            jobs = list(Jobs(config).get(filtering={"ids": starredIds}))
        else:
            jobs = []
        return jsonify(response.make(20, {"jobs": jobs}).__json__())

    @app.route("/jobs", methods=["GET"])
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
                    "long": 121
                    },
                "salary": "Competitive + Benefits",
                "jobType": "Contract/Interim",
                "stats": {
                  "viewed": 10,
                  "starred": 4
                }
              }
            ]})

    return app
