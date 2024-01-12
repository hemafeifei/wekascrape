# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from dataclasses import dataclass, field
from typing import Optional


class WekascraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

@dataclass
class ChocolateProduct:
    name: Optional[str] = field(default=None)
    price: Optional[float] = field(default=None)
    url: Optional[str] = None
