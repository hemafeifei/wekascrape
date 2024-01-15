import scrapy
from wekascraper.items import ZhihuIndex
from wekascraper.itemsloader import ZhihuIndexLoader
from datetime import datetime

class ZhihuHotSearch(scrapy.Spider):

    # name of the spider
    name = 'zhihu_index'

    # urls
    start_urls = ['https://www.zhihu.com/billboard']

    def parse(self, response) -> None:
        topics = response.xpath('//*[@id="root"]/div/main/div/a[*]')
        scrape_ts = datetime.now()
        image_dt = str(scrape_ts)[:10]

        for t in topics[:12]:
            topic = ZhihuIndexLoader(item=ZhihuIndex(image_dt=image_dt, scrape_ts=scrape_ts),
                                      selector=t)
            topic.add_xpath('search_rank', './div[1]/div[1]/text()')
            topic.add_xpath('topic', './div[2]/div[1]/text()')
            topic.add_xpath('search_index', './div[2]/div[2]/text()')
            yield topic.load_item()