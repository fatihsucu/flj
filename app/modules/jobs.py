# -*- coding: utf8 -*-
from app.libraries import loggerFactory
from app.libraries.mongodb import getDb
from bson.objectid import ObjectId
from app.modules.errors import (NotFoundException,
                                WrongArgumentException)
import arrow


def renameID(job):
    job['id'] = job["_id"]
    del job["_id"]
    return job


class Jobs(object):
    """This module handles operations related to job entries"""

    def __init__(self, config):
        super(Jobs, self).__init__()
        self.db = getDb()
        self.storage = self.db['jobs']
        self.logger = loggerFactory.get()

    def insert(self, job):
        # schema validation is needed here
        self.storage.insert(job)
        return renameID(job)

    def get(self, criteria=None, length=100):
        return self.storage.find(criteria).limit(100)

    def getOne(self, jobId):
        job = self.storage.find_one({"_id": ObjectId(jobId)})
        if not job:
            raise NotFoundException("job with id {} not found".format(jobId))
        return renameID(job)

    def delete(self, jobId):
        self.storage.remove({"_id": ObjectId(jobId)})

    def increaseView(self, jobId):
        return self.storage.update(
            {"_id": ObjectId(jobId)},
            {"$inc": {"stats.viewed": 1}})

    def increaseStar(self, jobId):
        return self.storage.update(
            {"_id": ObjectId(jobId)},
            {"$inc": {"stats.starred": 1}})

    def decreaseStar(self, jobId):
        return self.storage.update(
            {"_id": ObjectId(jobId)},
            {"$inc": {"stats.starred": -1}})
