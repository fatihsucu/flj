# -*- coding: utf8 -*-
from app.libraries import loggerFactory
from app.libraries.mongodb import getDb
from bson.objectid import ObjectId
from app.modules.errors import (NotFoundException,
                                WrongArgumentException)
import arrow


def renameID(record):
    record["id"] = record["_id"]
    del record["_id"]
    return record


class Accounts(object):
    """This module handles operations related to user accounts"""

    def __init__(self, config):
        super(Accounts, self).__init__()
        self.db = getDb()
        self.storage = self.db["accounts"]
        self.logger = loggerFactory.get()

    def insert(self, account):
        # schema validation is needed here
        self.storage.insert(account)
        for alarm in account['alarms']:
            alarm['location']['country'] = alarm['location']['country'].lower()
            alarm['location']['city'] = alarm['location']['city'].lower()
            alarm['location']['state'] = alarm['location']['state'].lower()
        return renameID(account)

    def get(self, filtering=None, length=100):
        return self.storage.find().limit(length)

    def getOne(self, accountId):
        account = self.storage.find_one({"_id": ObjectId(accountId)})
        if not account:
            raise NotFoundException(
                "account with id {} not found".format(accountId))
        return renameID(account)

    def get(self, filtering):
        flocation = filtering.get("location", None)
        fkeyword = filtering.get("keyword", [])
        query = {"$or": []}

        if flocation:
            query["alarms.$location.country"] = flocation["country"].lower()
            query["alarms.$location.city"] = flocation["city"].lower()
            if flocation.get("region", None):
                query["alarms.$location.region"] = flocation["region"].lower()

        if fkeyword:
            query["alarms.$keywords"] = {"$in": fkeyword}

        if not query["$or"]:
            del query["$or"]
        print str(query)
        self.logger.debug("account query: " + str(query))

        return self.storage.find(query)

    def delete(self, accountId):
        self.storage.remove({"_id": ObjectId(accountId)})
