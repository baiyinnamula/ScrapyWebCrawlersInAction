import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Response


class QuoteSpider(CrawlSpider):
    name = "quote"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    #设定规则
    rules = (
        # 对于quotes 内容页URL ，调用 parse_quotes 处理
        #并以此规则跟进获取的链接
        Rule(LinkExtractor(allow=r"/page/\d+"), callback="parse_quotes", follow=True),
        #对于 author 内容页 URL， 调用 parse_author 处理，提取数据
        Rule(LinkExtractor(allow=r'/author/\w+'), callback='parse_author')
        )

    # 提取内容页数据方法
    def parse_quotes(self, response: Response):
        for quote in response.css('.quote'):
            yield {
                'content': quote.css('.text::text').extract_first(),
                'author': quote.css('.author::text').extract_first(),
                'tags': quote.css('.tag::text').extract(),
            }

        # 提取内容页数据方法
    def parse_author(self, response: Response):
        name = response.css('.author-title::text').extract_first()
        author_born_date = response.css('.author-born-date::text').extract_first()
        author_born_location = response.css('.author-born-location::text').extract_first()
        author_description = response.css('.author-description::text').extract_first()
        
        return ({
            'name':name,
            'author_born_date':author_born_date,
            'author_born_location':author_born_location,
            'author_description':author_description
        })
      