# -*- coding: utf-8 -*-
import scrapy

letras = [
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "x",
    "z",
]


class LetraaSpider(scrapy.Spider):

    letras = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "x",
        "z",
    ]
    name = "letraa"
    allowed_domains = ["www.yellowpages.ae"]
    start_urls = [f"https://www.yellowpages.ae/companies-by-alphabet/a.html"]

    def parse(self, response):
        start_urls = [f"https://www.yellowpages.ae/companies-by-alphabet/a.html"]
        for empresa in response.xpath("//h2"):
            yield {"title": empresa.xpath(".//a/text()").get()}
        next_page = response.xpath("//a[@id='ContentPlaceHolder1_lnkNext']/@href").get()
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse, dont_filter=True)
            # teste
            print(next_page)


#        else:
#            for letra in letras:
#                start_urls = [f"https://www.yellowpages.ae/companies-by-alphabet/{letra}.html"]
