# -*- coding: utf8 -*-
import unittest
from basetest import BaseTest
from bson.objectid import ObjectId
import arrow
from app.modules.jobs import Jobs


class TestWidget(BaseTest, unittest.TestCase):
    """docstring for TestHistory"""

    JOBS = [{
        "date": "2014-04-12 15:30:12",
        "title": "Receptionist - Fluent French Speaker",
        "description": "At XYZ Hotels, we are looking for experienced French speakers to work at one ...",
        "company": "1X Hotels",
        "salary": "Competitive + Benefits",
        "jobType": "Contract/Interim",
        "location": {
          "country": "United Kingdom",
          "state": "",
          "city": "London",
          "region": "Westcost",
          "lat": 412,
          "long": 121
        },
        "stats": {
          "viewed": 10,
          "starred": 4
        }
    }, {
        "date": "2014-04-12 18:00:12",
        "title": "Waitress Fluent German Speaker",
        "description": "Office & Accounts Administrator - Construction",
        "company": "Tenders",
        "salary": "£21,000 to £23,000 p.a. plus some fantastic benefit",
        "jobType": "Permanent",
        "location": {
          "country": "Ireland",
          "state": "",
          "city": "Dublin",
          "region": "central",
          "lat": 212,
          "long": 321
        },
        "stats": {
          "viewed": 64,
          "starred": 14
        }
    }, {
        "date": "2014-04-14 20:00:12",
        "title": "Payroll and Benefits Administrator",
        "description": "One of my top London based Media clients urgently seeks a talented Payroll and Benefits Administrator ",
        "company": "Harriet Rawlinson",
        "salary": "£10 - £15 p hour",
        "jobType": "PART TIME",
        "location": {
          "country": "United Kingdom",
          "state": "",
          "city": "Manchester",
          "region": "North",
          "lat": 312,
          "long": 21
        },
        "stats": {
          "viewed": 82,
          "starred": 2
        }
    }
    ]

    @classmethod
    def setUpClass(cls):
        cls.jobsModule = Jobs(cls.config)

    def test_00_insert(self):
        for job in self.JOBS:
            job = self.jobsModule.insert(job)
            self.assertIsInstance(job['id'], ObjectId)

    def test_01_getWithoutFilter(self):
        jobsFound = self.jobsModule.get()
        self.assertEqual(jobsFound.count(), len(self.JOBS))

    def test_02_getOne(self):
        job = self.jobsModule.insert(self.JOBS[0])
        jobFound = self.jobsModule.getOne(job['id'])
        self.assertEqual(job['id'], jobFound['id'])

    def test_03_increaseViewed(self):
        job = self.JOBS[1]
        jobId = job['id']
        self.jobsModule.increaseView(jobId)
        jobFound = self.jobsModule.getOne(jobId)

        self.assertEqual(
            job['stats']['viewed'] + 1, jobFound['stats']['viewed'])

    def test_03_increaseStarred(self):
        job = self.JOBS[1]
        jobId = job['id']
        self.jobsModule.increaseStar(jobId)
        jobFound = self.jobsModule.getOne(jobId)
        self.assertEqual(
            job['stats']['starred'] + 1, jobFound['stats']['starred'])

    def test_03_decreaseStarred(self):
        job = self.JOBS[0]
        jobId = job['id']
        self.jobsModule.decreaseStar(jobId)
        jobFound = self.jobsModule.getOne(jobId)
        self.assertEqual(
            job['stats']['starred'] - 1, jobFound['stats']['starred'])


unittest.main()
