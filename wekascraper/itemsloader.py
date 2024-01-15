from itemloaders.processors import TakeFirst, MapCompose
from scrapy.loader import ItemLoader
import re

class ChocolateProductLoader(ItemLoader):

    default_output_processor = TakeFirst()
    price_in = MapCompose(lambda x: re.search(r'\d.*\d', x).group(0))
    url_in = MapCompose(lambda x: 'https://www.chocolate.co.uk' + x)

class SearchIndexLoader(ItemLoader):
    default_output_processor = TakeFirst()
    search_rank_in = MapCompose(lambda x: int(x.strip()) if x is not None else 0)
    topic_in = MapCompose(lambda x: x.strip())
    search_index_in = MapCompose(lambda x: int(x.strip()) if x is not None else 0)
