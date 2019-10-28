# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ItForAnalyticsItem(scrapy.Item):
    next_page = scrapy.Field()
    product = scrapy.Field()
    date = scrapy.Field()
    industry = scrapy.Field()
    description = scrapy.Field()
    price = scrapy.Field()
    response_rate = scrapy.Field()
    seller = scrapy.Field()
