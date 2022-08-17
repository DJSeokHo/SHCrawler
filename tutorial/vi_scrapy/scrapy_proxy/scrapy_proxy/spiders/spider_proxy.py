import scrapy
from scrapy import cmdline
from scrapy.http import HtmlResponse

from framewrok.utility.log_utility import ILog

设置代理
class SpiderProxySpider(scrapy.Spider):
    name = 'spider_proxy'
    allowed_domains = ['icanhazip.com']
    # start_urls = ['http://icanhazip.com']
    start_urls = ['https://icanhazip.com']

    def parse(self, response):

        html_response: HtmlResponse = response
        ILog.debug(__file__, html_response.text)


if __name__ == '__main__':
    cmdline.execute(f'scrapy crawl {SpiderProxySpider.name}'.split())
