# -*- coding: utf-8 -*-
import scrapy


class LetraaSpider(scrapy.Spider):
    name = 'letraa'
    #allowed_domains = ['www.yellowpages.ae/companies-by-alphabet/a.html']
    allowed_domains = ['www.yellowpages.ae']
    start_urls = ['https://www.yellowpages.ae/companies-by-alphabet/a.html/']

    def parse(self, response):
        for empresa in response.xpath("//h2"):

            yield  {
                'title': empresa.xpath(".//a/text()").get()
            }

        next_page = response.xpath("//a[@id='ContentPlaceHolder1_lnkNext']/@href").get()
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse,dont_filter = True)

