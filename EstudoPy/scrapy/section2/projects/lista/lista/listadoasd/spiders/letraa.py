# -*- coding: utf-8 -*-
import scrapy
letras = ['z','d','e','f','g','h','i','j','k','l','m','o','p','q','r','s','t','u','v','x','z']

class LetraaSpider(scrapy.Spider):
    #letras = ['a','b','c','d','e','f','g','h','i','j','k','l','m','o','p','q','r','s','t','u','v','x','z']
    name = 'letraa'
    allowed_domains = ['www.yellowpages.ae']
    start_urls = [f"https://www.yellowpages.ae/companies-by-alphabet/z.html"]

    def parse(self, response):
        for letra in letras:
            start_urls = [f"https://www.yellowpages.ae/companies-by-alphabet/{letra}.html"]

            for empresa in response.xpath("//h2"):
                yield  {
                    'title': empresa.xpath(".//a/text()").get()
                }

            next_page = response.xpath("//a[@id='ContentPlaceHolder1_lnkNext']/@href").get()
            if next_page:
                yield scrapy.Request(url=next_page, callback=self.parse, dont_filter = True)
