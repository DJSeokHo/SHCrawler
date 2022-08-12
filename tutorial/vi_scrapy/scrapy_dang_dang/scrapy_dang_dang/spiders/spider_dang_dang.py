import scrapy
from scrapy import cmdline, Selector
from scrapy.http import HtmlResponse

from framewrok.utility.log_utility import ILog
from framewrok.utility.uuid_utility import UUIDUtility
from tutorial.vi_scrapy.scrapy_dang_dang.scrapy_dang_dang.items import ScrapyDangDangItem


class SpiderDangDangSpider(scrapy.Spider):
    name = 'spider_dang_dang'
    allowed_domains = ['category.dangdang.com']  # 注意，这个范围需要修改，一般只写域名
    start_urls = ['http://category.dangdang.com/pg1-cp01.01.02.00.00.00.html']

    # https://category.dangdang.com/pg1-cp01.01.02.00.00.00.html
    # https://category.dangdang.com/pg2-cp01.01.02.00.00.00.html
    # https://category.dangdang.com/pg3-cp01.01.02.00.00.00.html
    # https://category.dangdang.com/pg4-cp01.01.02.00.00.00.html

    base_url = 'https://category.dangdang.com/pg'
    page = 1

    def parse(self, response):

        # pipelines 下载数据
        # items 定义数据结构

        html_response: HtmlResponse = response
        html_text = html_response.text

        # //ul[@id="component_59"]//li//img/@data-original 图片
        # //ul[@id="component_59"]//li//img/@alt 名字
        # //ul[@id="component_59"]//li//span[@class="search_now_price"]/text() 价格

        li_list: [Selector] = html_response.xpath('//ul[@id="component_59"]//li')

        temp_li: Selector
        for li in li_list:
            temp_li = li

            src: str = temp_li.xpath('.//img/@data-original').extract_first()

            if src:
                src = src
            else:
                src = temp_li.xpath('.//img/@src').extract_first()

            name = temp_li.xpath('.//img/@alt').extract_first()
            price = temp_li.xpath('.//span[@class="search_now_price"]/text()').extract_first()
            ILog.debug(__file__, f'{src} {name} {price}')

            # 生成item
            book = ScrapyDangDangItem(uuid=UUIDUtility.get_uuid(), src=src, name=name, price=price)

            # 交给 pipeline 去下载
            yield book  # 立即返回一个生成的book, 也可以用列表添加起来返回一个列表，但是这里在遍历中，我要立即返回一个 item

        # 继续爬取 # 最大可以是100
        if self.page < 2:
            self.page = self.page + 1

            url = f'{self.base_url}{self.page}-cp01.01.02.00.00.00.html'

            # 更改页码， 继续爬新的一页
            yield scrapy.Request(url=url, callback=self.parse)


if __name__ == '__main__':
    cmdline.execute(f'scrapy crawl {SpiderDangDangSpider.name}'.split())
