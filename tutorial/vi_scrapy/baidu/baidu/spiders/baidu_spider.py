import scrapy
from scrapy import cmdline
from scrapy.http import HtmlResponse

from framewrok.utility.log_utility import ILog


class BaiduSpiderSpider(scrapy.Spider):
    name = 'baidu_spider'
    allowed_domains = ['www.baidu.com']
    start_urls = ['https://www.baidu.com/']

    def parse(self, response):
        """
        :param response: 响应对象
        :return: None
        """

        response_object: HtmlResponse = response
        ILog.debug(__file__, type(response))
        ILog.debug(__file__, response_object.text)


if __name__ == '__main__':
    cmdline.execute(f'scrapy crawl {BaiduSpiderSpider.name}'.split())
