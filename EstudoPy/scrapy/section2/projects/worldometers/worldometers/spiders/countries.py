# -*- coding: utf-8 -*-
import scrapy


class CountriesSpider(scrapy.Spider):
    name = "countries"
    allowed_domains = ["www.worldometers.info/"]
    start_urls = [
        "https://www.worldometers.info/world-population/population-by-country/"
    ]

    def parse(self, response):
        countries = response.xpath("//td/a")
        for country in countries:

            name = country.xpath(".//text()").get()
            link = country.xpath(".//@href").get()
            pop20 = country.xpath(".//").get()

            yield {
                    'country_name' : name,
                    'country_link' : link,
                    'country_pop20': pop20
                } #response.follow(url=link)
