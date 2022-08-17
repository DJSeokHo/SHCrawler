from scrapy import cmdline, Selector
from scrapy.http import HtmlResponse
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from framewrok.utility.log_utility import ILog
from framewrok.utility.uuid_utility import UUIDUtility
from tutorial.vi_scrapy.scrapy_dushu.scrapy_dushu.items import ScrapyDushuItem

"""
如何建立一个带链接提取器的爬虫？
scrapy genspider -t crawl spider_name target_site_url
"""


class SpidersDushuSpider(CrawlSpider):
    name = 'spiders_dushu'
    allowed_domains = ['www.dushu.com']
    start_urls = ['https://www.dushu.com/book/1188_1.html']

    rules = (
        Rule(
            LinkExtractor(
                allow=r'/book/1188_\d+\.html',  # 该例子比较特殊，只能用正则
                # restrict_xpaths=r''
            ),
            callback='parse_item',
            follow=True),  # 如果是 True，就自动翻页，按照制定的链接规则一直跟进翻页。如果是False，就只爬初始时加载的页码
    )

    def parse_item(self, response):
        ILog.debug(__file__, "parse_item")
        html_response: HtmlResponse = response
        li_list = html_response.xpath('//div[@class="bookslist"]//li')
        temp_li: Selector
        temp_book: ScrapyDushuItem
        for li in li_list:
            temp_li = li
            temp_book = ScrapyDushuItem(
                seq=0,
                uuid=UUIDUtility.get_uuid(),
                name=temp_li.xpath('.//img/@alt').extract_first(),
                src=temp_li.xpath('.//img/@data-original').extract_first()
            )
            yield temp_book

    def parse(self, response, **kwargs):
        pass


if __name__ == '__main__':
    cmdline.execute(f'scrapy crawl {SpidersDushuSpider.name}'.split())
