import scrapy
from scrapy.spiders import CrawlSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule

# deals url: https://www.rei.com/c/camping-and-hiking/f/scd-deals
class ProductsSpider(CrawlSpider):
    name = "products"
    allowed_domains = ["rei.com"]
    start_urls = ["https://www.rei.com/c/camping-and-hiking/f/scd-deals"]

    rules = (
        Rule(LinkExtractor(allow=(r"page="),)),
        Rule(LinkExtractor(allow=(r"product/"),), callback="parse_item"),
    )

    def parse_item(self, response):
        pass
