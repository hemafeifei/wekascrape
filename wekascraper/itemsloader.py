from itemloaders.processors import TakeFirst, MapCompose
from scrapy.loader import ItemLoader
import re

class ChocolateProductLoader(ItemLoader):

    default_output_processor = TakeFirst()
    price_in = MapCompose(lambda x: re.search(r'\d.*\d', x).group(0))
    url_in = MapCompose(lambda x: 'https://www.chocolate.co.uk' + x)