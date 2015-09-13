from scrapy import Spider
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from scrapy.selector import Selector
from app.crawlers.jobs.items import JobsItem
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.item import Item, Field
# Modules insert
import sys
sys.path.append("../../")
from app.modules.jobs import Jobs as JobsModule

import configs
config = configs.get()

class JobSpider(CrawlSpider):
    """docstring for JobSpider"""
    name = "jobs"
    allowed_domain = "http://www.londonjobs.co.uk"
    start_urls = [
     "http://www.londonjobs.co.uk/"
        ]
    rules = (Rule(LinkExtractor(['http://www.londonjobs.co.uk/.*']), callback='parser', follow=True), )

    def content_extractor(self, selector, xpath):
        try:
            return selector.select(xpath).extract()[0].replace("  ", "").rstrip().lstrip()

        except:
            return " "

    def parser(self, response):
        job = JobsItem()
        jobs = Selector(response).xpath('//*[@id="semi_display"]/div[1]/div[3]')

        for _job in jobs:
            if not _job:
                continue
            job_title_xpath = '//*[@id="vacancyHeaderHolder"]/h1/text()'
            job_type_xpath = '//*[@id="extendedInfo"]/dd[1]/text()'
            salary_xpath = '//*[@id="extendedInfo"]/dd[3]/text()'
            location_xpath = '//*[@id="extendedInfo"]/dd[2]/text()'
            start_date_xpath = '//*[@id="extendedInfo"]/dd[4]/text()'
            duration_xpath = '//*[@id="extendedInfo"]/dd[5]/text()'
            vacancy_details = '//*[@id="vacancyDetails"]/text()'
            company_xpath = '//*[@id="vacPlacedBy"]/p[2]/text()'
            job['title'] = self.content_extractor(_job, job_title_xpath)
            job['salary'] = self.content_extractor(_job, salary_xpath)
            job['location'] = {
                "country": "United Kingdom",
                "city": self.content_extractor(_job, location_xpath),
                "region": ""
                }
            job['date'] = self.content_extractor(_job, start_date_xpath)
            job['jobType'] = self.content_extractor(_job, duration_xpath)
            job['description'] = self.content_extractor(_job, vacancy_details)
            job['company'] = self.content_extractor(_job, company_xpath)

            JobsModule(config).insert(dict(job))

