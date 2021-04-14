# -*- coding: utf-8 -*-
import scrapy

class test(scrapy.Item):
    latitude         = scrapy.Field()
    longitude        = scrapy.Field()
    
class LinksSpider(scrapy.Spider):
    name = 'test_scrapper'
    allowed_domains = ['www.otodom.pl']
    
    start_urls = ['https://www.otodom.pl/pl/oferta/piekne-mieszkanie-109m2-tarasy-ogrodki-bezposr-ID4auTW.html#dd1259a3c5']

    def parse(self, response):
        t = test()

        coord_xpath = '//script//text()'
        text =  response.xpath(coord_xpath).getall()
        text = ''.join(text)

        t['latitude'] = text[text.find("latitude")+9: text.find("latitude")+20]
        t['longitude'] = text[text.find("longitude")+10: text.find("longitude")+21]
        
        yield t



