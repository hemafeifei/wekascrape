import scrapy
from wekascraper.items import BaiduIndex
from wekascraper.itemsloader import SearchIndexLoader
from datetime import datetime

class BaiduHotSearch(scrapy.Spider):

    # name of the spider
    name = 'baidu_index'

    # urls
    start_urls = ['https://top.baidu.com/board?tab=realtime']

    def parse(self, response) -> None:
        topics = response.xpath('//*[@id="sanRoot"]/main/div[2]/div/div[2]/div[*]')
        scrape_ts = datetime.now()
        image_dt = str(scrape_ts)[:10]

        for t in topics[1:21]:
            topic = SearchIndexLoader(item=BaiduIndex(image_dt=image_dt, scrape_ts=scrape_ts),
                                      selector=t)
            topic.add_xpath('search_rank', './a/div[1]/text()')
            topic.add_xpath('topic', './div[2]/a/div[1]/text()')
            topic.add_xpath('search_index', './div[1]/div[2]/text()')
            topic.add_xpath('url', './a/@href')

            yield topic.load_item()






