# -*- coding: utf-8 -*-
import scrapy


class SpiderpibSpider(scrapy.Spider):
    name = "spiderpib"
    allowed_domains = [
        "www.pt.wikipedia.org/wiki/Lista_de_pa%C3%ADses_por_taxa_de_crescimento_real_de_PIB"
    ]
    start_urls = [
        "https://http://pt.wikipedia.org/wiki/Lista_de_pa%C3%ADses_por_taxa_de_crescimento_real_de_PIB/"
    ]

    def parse(self, response):
        pib = response.xpath("//table")

        yield {"pip_wiki": pib}
