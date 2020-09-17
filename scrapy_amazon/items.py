# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyAmazonItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class GameAndWatchItem(scrapy.Item):
    name = scrapy.Field(serializer=str)
    canBuy = scrapy.Field(serializer=bool)
    pass
