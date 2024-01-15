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
            # yield {
            #     'search_rank': t.xpath('./a/div[1]').css("div.index_1Ew5p::text").get(),
            #     'topic': t.xpath('./div[2]/a/div[1]/text()').get(),
            #     'search_index': t.xpath('./div[1]/div[2]').css("div.hot-index_1Bl1a::text").get(),
            #     'url': t.xpath('./a/@href').get(),
            #     'image_dt': str(datetime.now())[:10],
            #     'scrape_ts': datetime.now()
            # }
            topic = SearchIndexLoader(item=BaiduIndex(image_dt=image_dt, scrape_ts=scrape_ts),
                                      selector=t)
            topic.add_xpath('search_rank', './a/div[1]/text()')
            topic.add_xpath('topic', './div[2]/a/div[1]/text()')
            topic.add_xpath('search_index', './div[1]/div[2]/text()')
            topic.add_xpath('url', './a/@href')

            yield topic.load_item()

