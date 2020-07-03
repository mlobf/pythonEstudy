from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from spiders.letraa import LetraaSpider


process = CrawlerProcess(settings=get_project_settings())
process.crawl(LetraaSpider)
process.start()


