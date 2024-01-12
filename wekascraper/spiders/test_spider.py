import scrapy
from wekascraper.items import ChocolateProduct
import re

class ChocolateSpider(scrapy.Spider):

    # name of the spider
    name = 'chocolatespider'

    # urls
    start_urls = ['https://www.chocolate.co.uk/collections/all']

    def parse(self, response) ->None:

        products = response.xpath('//*[@id="facet-main"]/product-list/div/product-item[*]/div[2]/div')
        product_item = ChocolateProduct()
        for p in products:
            product_item.name = p.xpath('./a/text()').get()
            product_item.price = re.search(r'\d.*\d', p.xpath('./div/div/span').get()).group(0)
            product_item.url = p.xpath('./a/@href').get()
            yield product_item

        next_page = response.xpath('//*[@id="facet-main"]/page-pagination/nav/a[3]/@href').get()
        if next_page is not None:
            next_page_url = 'https://www.chocolate.co.uk' + next_page
            yield response.follow(next_page_url, callback=self.parse)