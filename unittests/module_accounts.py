# -*- coding: utf8 -*-
import unittest
from basetest import BaseTest
from bson.objectid import ObjectId
import arrow
from app.modules.accounts import Accounts


class TestAccount(BaseTest, unittest.TestCase):

    ACCOUNTS = [{
        "id": None,
        "createdAt": "2015-04-22 12:30:12",
        "lastLogin": "2015-04-25 15:41:27",
        "fname": "Mustafa",
        "lname": "Atik",
        "email": "mm@aasscsaccccmm.com",
        "gcmId": "code1",
        "alarms": [
            {
                "createdAt": "2015-04-23 15:30:12",
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
      }, {
        "id": None,
        "createdAt": "2015-05-11 11:34:22",
        "lastLogin": "2015-04-12 21:31:62",
        "fname": "John",
        "lname": "Smith",
        "email": "jmm@jaasscsaccccmm.com",
        "gcmId": "code2",
        "alarms": [
            {
                "createdAt": "2015-05-11 14:30:12",
                "location": {
                    "country": "Ireland",
                    "state": "",
                    "city": "Dublin",
                    },
                "keywords": [
                    "waiter",
                    "repair"
                ]
            }
        ]
      }, {
        "id": None,
        "createdAt": "2015-05-02 02:04:21",
        "lastLogin": "2015-05-06 08:18:35",
        "fname": "George",
        "lname": "Mich",
        "email": "gmm@gaasscsaccccmm.com",
        "gcmId": "code3",
        "alarms": [
            {
                "createdAt": "2015-05-03 12:32:22",
                "location": {
                    "country": "United Kingdom",
                    "state": "",
                    "city": "London",
                    },
                "keywords": [
                    "developer"
                ]
            }, {
                "createdAt": "2015-05-03 12:40:42",
                "location": {
                    "country": "United Kingdom",
                    "state": "",
                    "city": "Manchester",
                    },
                "keywords": [
                    "developer"
                ]
            }
        ]
      }
    ]

    @classmethod
    def setUpClass(cls):
        cls.accounts = Accounts(cls.config)

    def test_00_insert(self):
        for account in self.ACCOUNTS:
            record = self.accounts.insert(account)
            account['id'] = record['id']
            self.assertIsInstance(record['id'], ObjectId)

    def test_01_getWithoutFilter(self):
        accountsFound = self.accounts.get(filtering={})
        self.assertEqual(accountsFound.count(), len(self.ACCOUNTS))

    def test_02_getOne(self):
        account = self.ACCOUNTS[0]
        accountFound = self.accounts.getOne(account['id'])
        self.assertEqual(account['id'], accountFound['id'])

    def test_0401_getByLocationFilter(self):
        for i in self.accounts.get(filtering={}):
            print i["_id"], i["email"], i['alarms']

        def doFilter(account, count, countWithRegion):
            location = account["alarms"][0]["location"]
            filtering = {
                "location": {
                    "country": location["country"].upper(),
                    "city": location["city"].lower(),
                }
            }

            accountsFound = self.accounts.get(filtering=filtering)
            self.assertEqual(count, accountsFound.count())

            filtering['location']['region'] = location["region"].upper()
            accountsFound = self.accounts.get(filtering=filtering)
            self.assertEqual(countWithRegion, accountsFound.count())

        doFilter(self.ACCOUNTS[0], 2, 1)  # 3 london accounts
    #     doFilter(self.ACCOUNTS[1], 1, 1)  # 1 dublin account, 1 central account

    # def test_0402_getByKeywordFilter(self):
    #     def doFilter(keyword, count):
    #         filtering = {
    #             "title": keyword
    #         }
    #         accountsFound = self.accounts.get(filtering=filtering)
    #         self.assertEqual(count, accountsFound.count())
    #     doFilter("geRM", 1)  # 1 greman account
    #     doFilter("speak", 3)  # 3 accounts containg *speak* in title

    # def test_0403_getByaccountTypeFilter(self):
    #     def doFilter(keyword, count):
    #         filtering = {
    #             "accountType": keyword
    #         }
    #         accountsFound = self.accounts.get(filtering=filtering)
    #         self.assertEqual(count, accountsFound.count())
    #     doFilter("part", 2)  # 2 part time accounts
    #     doFilter("peRManent", 1)  # 1 permanent account

    # def test_0403_getBySinceMaxFilter(self):
    #     accountsFound = list(self.accounts.get(filtering={}))
    #     sinceaccount = accountsFound[1]
    #     maxaccount = accountsFound[3]
    #     targetaccount = accountsFound[2]

    #     filtering = {
    #         "sinceId": sinceaccount["_id"],
    #         "maxId": maxaccount["_id"]
    #     }

    #     accountsFound = list(self.accounts.get(filtering=filtering))
    #     self.assertEqual(accountsFound[0]["_id"], targetaccount["_id"])

    # def test_0405_getByCombinedFilter(self):
    #     def doFilter(account, keyword, accountType, count):
    #         filtering = {
    #             "location": {
    #                 "country": account["location"]["country"].upper(),
    #                 "city": account["location"]["city"].lower(),
    #             },
    #             "title": keyword,
    #             "description": keyword,
    #             "accountType": accountType
    #         }
    #         accountsFound = self.accounts.get(filtering=filtering)
    #         self.assertEqual(count, accountsFound.count())

    #     account = self.ACCOUNTS[1]
    #     doFilter(account, "speak", account['accountType'], 1)  # 1 speaker in Dublin
    #     doFilter(account, "speak", "naaa", 0)  # 0 speaker account with type naaa in Dublin

    #     account = self.ACCOUNTS[0]
    #     doFilter(account, "speak", account['accountType'], 2)  # 2 part time accounts
    #     doFilter(account, "one of my", "permanent", 1)  # 2 part time accounts


unittest.main()
