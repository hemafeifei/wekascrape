import scrapy
from wekascraper.items import WeiboIndex
from datetime import datetime
import json

# Weibo Hot search, without Itemloader
class WeiboHotSearch(scrapy.Spider):
    # name of the spider
    name = 'weibo_index'

    # urls
    start_urls = ['https://www.weibo.com/ajax/side/hotSearch']

    def parse(self, response) -> None:
        topics = json.loads(response.text)
        scrape_ts = datetime.now()
        image_dt = str(scrape_ts)[:10]
        topic_item = WeiboIndex(image_dt=image_dt, scrape_ts=scrape_ts)

        for t in topics['data']['realtime'][:25]:
            if (t.get('raw_hot', 0) > 0) & (t.get('rank')<20):
                topic_item.search_rank = int(t.get('rank', 99)) + 1 # weibo rank starts from 1
                topic_item.topic = t['word']
                topic_item.search_index = t.get('num', 0)
                topic_item.channel_type = t.get('channel_type', '')
                topic_item.category = t.get('category', '')
                yield topic_item