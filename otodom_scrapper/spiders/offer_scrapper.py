# -*- coding: utf-8 -*-
import scrapy

class Offer(scrapy.Item):
    link           = scrapy.Field()
    price          = scrapy.Field()
    sq_metre       = scrapy.Field()
    no_rooms       = scrapy.Field()
    market         = scrapy.Field()
    build_type     = scrapy.Field()
    floor          = scrapy.Field()
    build_floors   = scrapy.Field()
    windows        = scrapy.Field()
    heating        = scrapy.Field()
    year_constr    = scrapy.Field()
    build_material = scrapy.Field()
    condition      = scrapy.Field()
    own_form       = scrapy.Field()
    balcony        = scrapy.Field()
    garage         = scrapy.Field()
    storage        = scrapy.Field()
    elevator       = scrapy.Field()
    garden         = scrapy.Field()
    longitude      = scrapy.Field()
    latitude       = scrapy.Field()
    

class OffersSpider(scrapy.Spider):
    name = 'offer_scrapper'
    allowed_domains = ['www.otodom.pl']
    
    try: 
        with open("links.csv", "rt") as f:
                start_urls = [url.strip() for url in f.readlines()][1:]

        def parse(self, response):
            o = Offer()

            link_xpath           = '/html/head/link[@rel="canonical"]//@href'
            price_xpath          = '//strong[@aria-label="Cena"]//text()'
            sq_metre_xpath       = '//div[@aria-label="Powierzchnia"]//div[2]//text()'
            no_rooms_xpath       = '//div[@aria-label="Liczba pokoi"]//div[2]//text()'
            market_xpath         = '//div[@aria-label="Rynek"]//div[2]//text()'
            build_type_xpath     = '//div[@aria-label="Rodzaj zabudowy"]//div[2]//text()'
            floor_xpath          = '//div[@aria-label="Piętro"]//div[2]//text()'
            build_floors_xpath   = '//div[@aria-label="Liczba pięter"]//div[2]//text()'
            windows_xpath        = '//div[@aria-label="Okna"]//div[2]//text()'
            heating_xpath        = '//div[@aria-label="Ogrzewanie"]//div[2]//text()'
            year_constr_xpath    = '//div[@aria-label="Rok budowy"]//div[2]//text()'
            build_material_xpath = '//div[@aria-label="Materiał budynku"]//div[2]//text()'
            condition_xpath      = '//div[@aria-label="Stan wykończenia"]//div[2]//text()'
            own_form_xpath       = '//div[@aria-label="Forma własności"]//div[2]//text()'
            balcony_xpath        = '//div[@data-cy="ad.ad-features.categorized-list"]//text()[.="balkon"]'
            garage_xpath         = '//div[@data-cy="ad.ad-features.categorized-list"]//text()[.="garaż/miejsce parkingowe"]'
            storage_xpath        = '//div[@data-cy="ad.ad-features.categorized-list"]//text()[.="piwnica" or .="pom. użytkowe"]'
            elevator_xpath       = '//div[@data-cy="ad.ad-features.categorized-list"]//text()[.="winda"]'
            garden_xpath         = '//div[@data-cy="ad.ad-features.categorized-list"]//text()[.="ogródek"]' 
            coords_xpath         = '//script//text()'    
            
            o['link']            = response.xpath(link_xpath).getall()
            o['price']           = response.xpath(price_xpath).get()
            o['sq_metre']        = response.xpath(sq_metre_xpath).get()
            o['no_rooms']        = response.xpath(no_rooms_xpath).getall()
            o['market']          = response.xpath(market_xpath).getall()
            o['build_type']      = response.xpath(build_type_xpath).getall()
            o['floor']           = response.xpath(floor_xpath).getall()
            o['build_floors']    = response.xpath(build_floors_xpath).getall()
            o['windows']         = response.xpath(windows_xpath).getall()
            o['heating']         = response.xpath(heating_xpath).getall()
            o['year_constr']     = response.xpath(year_constr_xpath).getall()
            o['build_material']  = response.xpath(build_material_xpath).getall()
            o['condition']       = response.xpath(condition_xpath).getall()
            o['own_form']        = response.xpath(own_form_xpath).getall()
            o['balcony']         = response.xpath(balcony_xpath).getall()
            o['garage']          = response.xpath(garage_xpath).getall()
            o['storage']         = response.xpath(storage_xpath).getall()
            o['elevator']        = response.xpath(elevator_xpath).getall()
            o['garden']          = response.xpath(garden_xpath).getall()

            # Takes whole script part from page, then merges list into one string
            # and searches for coordinates in that string
            text                 =  response.xpath(coords_xpath).getall()
            text                 = ''.join(text)
            
            o['longitude']       = text[text.find("latitude")+10 : text.find("latitude")+19]
            o['latitude']        = text[text.find("longitude")+11 : text.find("longitude")+20]

            yield o

    except Exception:
        pass


