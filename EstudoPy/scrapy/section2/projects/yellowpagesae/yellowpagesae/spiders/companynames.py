# -*- coding: utf-8 -*-
import scrapy


class CompanynamesSpider(scrapy.Spider):
    name = "companynames"
    allowed_domains = ["www.yellowpages.ae"]
    start_urls = ["https://www.yellowpages.ae/companies-by-alphabet/a.html"]

    def parse(self, response):
        pass
