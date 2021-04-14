# -*- coding: utf-8 -*-
import scrapy

class Link(scrapy.Item):
    link = scrapy.Field()

class LinksSpider(scrapy.Spider):
    name = 'link_scrapper'
    allowed_domains = ['https://www.otodom.pl/']
    
    standard_offers = [('https://www.otodom.pl/sprzedaz/mieszkanie/warszawa/?search%5Bregion_id%5D=7&search%5Bsubregion_id%5D=197&search%5Bcity_id%5D=26&page='
                    + str(page)) for page in range(1, 501)]

    promoted_offers = [('https://www.otodom.pl/sprzedaz/mieszkanie/warszawa/?search%5Bregion_id%5D=7&search%5Bsubregion_id%5D=197&search%5Bcity_id%5D=26&search%5Bpaidads_listing%5D=1&page='
                    + str(page)) for page in range(1, 78)]

    start_urls = standard_offers + promoted_offers

    def parse(self, response):
        
        link_xpath = '/html/body/div[3]/main/section[2]/div/div/div[1]/div/article/div[1]/header/h3//@href'
        selection = response.xpath(link_xpath)
        
        for s in selection:
            l = Link()
            l['link'] = s.get()
            yield l
