# -*- coding: utf-8 -*-
import scrapy


class SpecialOffersSpider(scrapy.Spider):
    name = 'special_offers'
    allowed_domains = ['www.tinydeal.com/pt/specials.html']
    start_urls = ['http://www.tinydeal.com/pt/specials.html/']

    def parse(self, response):
        pass
