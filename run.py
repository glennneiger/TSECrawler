from scrapy.crawler import CrawlerProcess
from TSECrawler.spiders.tse_spider import TSESpider

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(TSESpider)
process.start()