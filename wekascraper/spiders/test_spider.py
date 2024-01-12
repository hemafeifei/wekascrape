import scrapy
from wekascraper.items import ChocolateProduct
from wekascraper.itemsloader import ChocolateProductLoader
import re

class ChocolateSpider(scrapy.Spider):

    # name of the spider
    name = 'chocolatespider'

    # urls
    start_urls = ['https://www.chocolate.co.uk/collections/all']

    def parse(self, response) ->None:

        products = response.xpath('//*[@id="facet-main"]/product-list/div/product-item[*]/div[2]/div')

        for p in products:
            chocolate = ChocolateProductLoader(item=ChocolateProduct(), selector=p)
            chocolate.add_xpath("name", './a/text()')
            chocolate.add_xpath("price", './div/div/span')
            chocolate.add_xpath("url", './a/@href')

            yield chocolate.load_item()

        next_page = response.xpath('//*[@id="facet-main"]/page-pagination/nav/a[3]/@href').get()
        if next_page is not None:
            next_page_url = 'https://www.chocolate.co.uk' + next_page
            yield response.follow(next_page_url, callback=self.parse)