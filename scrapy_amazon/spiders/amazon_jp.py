import scrapy


class AmazonJpSpider(scrapy.Spider):
    name = 'amazon_jp'
    allowed_domains = ['amazon.co.jp']
    start_urls = ['http://amazon.co.jp/']

    def parse(self, response):
        pass
