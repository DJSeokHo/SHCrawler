import scrapy
from scrapy import cmdline, Selector
from scrapy.http import HtmlResponse

from framewrok.utility.log_utility import ILog


class SpiderTc58Spider(scrapy.Spider):
    name = 'spider_tc_58'
    allowed_domains = ['bj.58.com']
    start_urls = ['https://bj.58.com/sou/?key=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91']

    def parse(self, response):
        """
        :param response: 响应对象
        :return: None
        """

        html_response: HtmlResponse = response
        ILog.debug(__file__, type(html_response))
        # ILog.debug(__file__, html_response.text)  # 网页数据字符串
        ILog.debug(__file__, html_response.url)
        # ILog.debug(__file__, html_response.headers)
        # ILog.debug(__file__, html_response.protocol)
        # ILog.debug(__file__, html_response.body)  # 网页数据二进制
        span: Selector = html_response.xpath('//div[@id="filter"]//div[@class="tabs"]/a/span')[0]
        ILog.debug(__file__, type(span))
        ILog.debug(__file__, span.extract())  # 提取 selector对象的data属性值


if __name__ == '__main__':
    cmdline.execute(f'scrapy crawl {SpiderTc58Spider.name}'.split())
