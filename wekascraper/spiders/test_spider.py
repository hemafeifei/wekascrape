import scrapy
import re

class ChocolateSpider(scrapy.Spider):

    # name of the spider
    name = 'chocolatespider'

    # urls
    start_urls = ['https://www.chocolate.co.uk/collections/all']

    def parse(self, response) ->None:

        products = response.xpath('//*[@id="facet-main"]/product-list/div/product-item[*]/div[2]/div')
        for p in products:
            yield {
                # '<a href="/products/2-5kg-of-our-best-selling-61-dark-hot-chocolate-drops" class="product-item-meta__title">2.5kg Bulk 61% Dark Hot Chocolate Drops</a>'
                'name': p.xpath('./a/text()').get(),
                'price': re.search(r'\d.*\d', p.xpath('./div/div/span').get()).group(0),
                'url': p.xpath('./a/@href').get()
            }

        next_page = response.xpath('//*[@id="facet-main"]/page-pagination/nav/a[3]/@href').get()
        if next_page is not None:
            next_page_url = 'https://www.chocolate.co.uk' + next_page
            yield response.follow(next_page_url, callback=self.parse)