import scrapy
from scrapy import cmdline, Selector
from scrapy.http import HtmlResponse

from framewrok.utility.log_utility import ILog


class SpiderCarHomeSpider(scrapy.Spider):
    name = 'spider_car_home'
    allowed_domains = ['https://car.autohome.com.cn/price/brand-15.html']
    # html结尾的话，后面去掉'/'
    start_urls = ['https://car.autohome.com.cn/price/brand-15.html']

    def parse(self, response):
        ILog.debug(__file__, "=============================================")
        html_response: HtmlResponse = response

        name_list: list[Selector] = html_response.xpath('//div[@class="list-cont"]//div[@class="list-cont-main"]//div['
                                                        '@class="main-title"]/a/text()')
        price_list: list[Selector] = html_response.xpath('//div[@class="list-cont"]//div['
                                                         '@class="list-cont-main"]//div['
                                                         '@class="main-lever-right"]//span/text()')

        # for name, price in name_list, price_list:
        #     ILog.debug(__file__, f'{name.extract()} {price.extract()}')


if __name__ == '__main__':
    args = f'scrapy crawl {SpiderCarHomeSpider.name}'.split()
    cmdline.execute(args)
