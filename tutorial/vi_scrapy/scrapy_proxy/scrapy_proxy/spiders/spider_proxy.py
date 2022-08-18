import scrapy
from scrapy import cmdline
from scrapy.http import HtmlResponse

from framewrok.utility.log_utility import ILog
from framewrok.utility.proxies_utility import ProxiesUtility


class SpiderProxySpider(scrapy.Spider):
    name = 'spider_proxy'
    allowed_domains = ['icanhazip.com']
    # start_urls = ['http://icanhazip.com']
    start_urls = ['https://icanhazip.com']

    # 设置代理
    def start_requests(self):
        proxy = ProxiesUtility.get_ssl_proxy_string()
        yield scrapy.Request(self.start_urls[0], meta={"proxy": proxy})

    def parse(self, response):

        html_response: HtmlResponse = response
        ILog.debug(__file__, html_response.text)


if __name__ == '__main__':
    cmdline.execute(f'scrapy crawl {SpiderProxySpider.name}'.split())
