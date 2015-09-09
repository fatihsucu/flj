# -*- coding: utf8 -*-
import unittest
import sys
from bson.objectid import ObjectId
import os

sys.path.insert(
    0, os.path.join(
        os.path.abspath(os.path.dirname(__file__)) + '/../'))

import configs
from app.libraries import mongodb


configs.enforcingEnv = "default.test"


class BaseTest(object):
    """Config alan tüm nesneler unittest için bu
    sınıfta üretilip test sınıflarına import edilebilir."""
    config = configs.get()
    db = mongodb.getDb(config)

    @classmethod
    def tearDownClass(cls):
        cls.db.jobs.remove()
        #cls.db.accounts.remove()
