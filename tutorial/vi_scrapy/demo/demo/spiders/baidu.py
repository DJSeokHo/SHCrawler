import ssl

import scrapy
from scrapy import cmdline
from scrapy.http import HtmlResponse

from framewrok.utility.log_utility import ILog

ssl._create_default_https_context = ssl._create_unverified_context


class BaiduSpider(scrapy.Spider):
    # 爬虫名字
    name = 'baidu'

    # 允许访问的域名
    allowed_domains = ['www.baidu.com']

    # 起始的url
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

    args = f'scrapy crawl {BaiduSpider.name}'.split()
    cmdline.execute(args)

"""
-15: 20
cate: tech
clientsource: 1
city: bj
zp_zhs_ext_cate: 0
plat: m
kw: 前端开发
localWord: 1
_: 1660131584222
PGTID: 0d360415-0000-16fd-5c31-1066604dc53e
pn: 2
"""