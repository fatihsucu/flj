from app.crawlers.jobs.spiders import job_spider
from app.libraries.celerySetter import getCelery
import configs
from scrapy.crawler import CrawlerProcess

config = configs.get()
app = getCelery(config)


@app.task(name="app.proxies.crawler.crawl")
def crawl():
    process = CrawlerProcess({
            'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
        })
    process.crawl(job_spider.JobSpider)
    process.start()