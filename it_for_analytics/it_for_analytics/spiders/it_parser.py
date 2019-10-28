import scrapy
from ..items import ItForAnalyticsItem
from datetime import datetime


class QuotesSpider(scrapy.Spider):
    name = "it_parser"

    def start_requests(self):
        url = 'https://www.indotrading.com/productcatalog/'
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        links = response.xpath('//*[@id="B"]/div/div/div[2]/div/div/div/a/@href').getall()
        for href in links:
            yield response.follow(href, self.parse_products)
        # yield response.follow(links, self.parse_products)

    #     next_page = response.xpath('').get()
    #     if next_page is not None:
    #         yield response.follow(next_page, callback=self.parse)
    #
    def parse_products(self, response):
        item = ItForAnalyticsItem()
        products = response.xpath('//h3/a/text()').getall()
        dates = response.xpath('//div[@class="entry_meta"]/span[@class="normal-color font12"]/text()').getall()
        industrys = response.xpath('//div[@class="idt-elipsis catName"]/b/text()').getall()
        descriptions = response.xpath('//p[@class="three-line font13"]/text()').getall()
        prices = response.xpath('//*[@id="products_container"]/div/div/div/div/div/div/div/div/ul/li/text()').getall()
        response_rates = response.xpath('//*[@id="products_container"]/div/div/div/div/div/div/div[2]/div/div/text()').getall()
        sellers = response.xpath('//div[@class="mar-less font12"]/div/span/text()').getall()
        next_pages = response.xpath('//*[@id="tab-1"]/div[2]/ul/li/a/@href').getall()
        i = len(products) - 1
        while i:
            if products:
                item['product'] = products[i].strip()
                item['date'] = dates[i].strip()
                item['industry'] = industrys[i]
                item['description'] = descriptions[i]
                item['price'] = prices[i]
                item['response_rate'] = response_rates[i]
                item['seller'] = sellers[i]
                i -= 1
                yield item
            else:
                break
        for next_page in next_pages:
            yield response.follow(next_page, self.parse_products)
