# -*- coding: utf8 -*-
'''
Bu kod dosyasında widget ile ilgili fonksiyonlar tanımlanır.

Hata kodları için bkz: 'https://github.com/botego/livechat/wiki/api_errors'
'''
from app.libraries import loggerFactory
from app.libraries.mongodb import getDb
from bson.objectid import ObjectId
from app.modules.errors import (NotFoundException,
                                WrongArgumentException)
import arrow


class Jobs(object):
    """This module handles operations related to job entries"""

    def __init__(self, config):
        super(Jobs, self).__init__()
        self.db = getDb()
        self.storage = self.db['jobs']
        self.logger = loggerFactory.get()

    def insert(self, job):
        raise NotImplementedError()

    def get(self, filter, length=100):
        raise NotImplementedError()

    def getOne(self, jobId):
        raise NotImplementedError()

    def delete(self, jobId):
        raise NotImplementedError()

    def increaseView(self, jobId):
        raise NotImplementedError()

    def increaseStar(self, jobId):
        raise NotImplementedError()

    def decreaseStar(self, jobId):
        raise NotImplementedError()
