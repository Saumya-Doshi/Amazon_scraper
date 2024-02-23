# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyScrapyProjectItem(scrapy.Item):
    description = scrapy.Field()
    price = scrapy.Field()
    rating = scrapy.Field()
    brand = scrapy.Field()
    Model_name = scrapy.Field()
    color = scrapy.Field()
    form_factor = scrapy.Field()
    connectivity_Technology = scrapy.Field()