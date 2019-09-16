# -*- coding: utf-8 -*-
import scrapy
from ..items import MaterielnetItem
import json

class MaterielnetSpiderSpider(scrapy.Spider):
    name = 'materiel'
    start_urls = [
    "https://www.materiel.net/carte-mere/l443/"
    ]

    def parse(self, response):
        items= MaterielnetItem()

        product_name = response.css('.c-product__title').css('::text').getall()
        product_description = response.css('.c-product__description::text').getall()
        #product_image = response.css('.o-btn__add-to-cart--small').getall()
        #product_price = response.css(".c-products-list__item").getall()
        theShopingCartImage = response.css('.o-btn__add-to-cart--small').getall()
        #for id in response.css('.o-btn__add-to-cart--small').getall():
        #    items['product_id'].append(id[25:39])
        product_id=[]
        for i in range(len(theShopingCartImage)):
            product_id.append(theShopingCartImage[i][25:38])

        items['product_name'] = product_name
        items['product_description'] = product_description
        #items['product_price'] = product_price
        #items['product_image'] = [product_image[0][25:38],product_image[1][25:38]]
        items['product_id'] = product_id
        #items['product_price'] = product_price

        yield items
    #    with open('materiel.json') as json_file:
        #    data = json.load(json_file)
    #        for p in data[0]['product_id']:
    ###            next_object = response.urljoin("produit/"+p+".html")
    ##            name = response.css("h1::text").get()
    #            descript = response.css(".c-product__specs::text").get()
    #            price = response.css(".o-product__price--large").get()
    #            img = response.css(".b-loaded::attr(href)").get()
    #            yield{name,descript,price,img}
