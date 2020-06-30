#import pdb
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from special_offers import SpecialOffersSpider
from random import Random




process = CrawlerProcess(settings=get_project_settings())
process.crawl(SpecialOffersSpider)
process.start()
