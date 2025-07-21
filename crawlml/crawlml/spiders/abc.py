import scrapy
from scrapy.spiders import CrawlSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
import datetime


class ABCNewsSpider(CrawlSpider):
    name = "abc_news"
    allowed_domains = ["abc.ca.gov"]
    start_urls = ["https://www.abc.ca.gov/news-releases/"]

    rules = (
        # Extract individual article links from h2 tags
        Rule(
            LinkExtractor(
                restrict_css="h2.entry-title a",  # Target the actual article links
                allow=()  # Allow all links found in h2 tags
            ), 
            callback="parse_item",
            follow=False
        ),
        # Follow pagination links
        Rule(
            LinkExtractor(allow=(r"news-releases/page/\d+/")), 
            follow=True
        ),
    )

    def parse_item(self, response):
        # Extract article data
        title = response.css('h1.entry-title::text').get()
        date_elem = response.css('.entry-date::text').get()
        
        # Extract all paragraph text from content area
        content_paragraphs = response.css('.entry-content p::text').getall()
        content = ' '.join(content_paragraphs).strip()
        
        # Also get the first paragraph which often has the key info
        first_paragraph = response.css('.entry-content p:first-child::text').get()
        
        yield {
            'url': response.url,
            'title': title,
            'date': date_elem,
            'content': content,
            'first_paragraph': first_paragraph,
            'scraped_at': datetime.datetime.now().isoformat()
        }