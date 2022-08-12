import scrapy
from scrapy import cmdline, Selector
from scrapy.http import HtmlResponse

from framewrok.utility.log_utility import ILog
from framewrok.utility.uuid_utility import UUIDUtility
from tutorial.vi_scrapy.scrapy_movie.scrapy_movie.items import ScrapyMovieItem


class SpiderMovieSpider(scrapy.Spider):
    name = 'spider_movie'
    allowed_domains = ['www.ygdy8.net']
    start_urls = ['https://www.ygdy8.net/html/gndy/china/index.html']

    def parse(self, response):
        """
        列表页的parse
        :param response:
        :return:
        """
        # 父页面列表的名字和详情页的图片
        # //div[@class="co_content8"]//td[2]//a[2]/text()
        # //div[@class="co_content8"]//td[2]//a[2]/@href
        html_response: HtmlResponse = response

        a_list = html_response.xpath('//div[@class="co_content8"]//td[2]//a[2]')
        for a in a_list:
            a_tag: Selector = a
            title = a_tag.xpath('./text()').extract_first()
            href = a_tag.xpath('./@href').extract_first()

            # 详情页的链接
            url = f'https://www.ygdy8.net{href}'
            ILog.debug(__file__, f'{title} {url}')

            # 对详情页发起访问, 然后需要把这里的 title和传递给详情页的parse，组合成一个item进行保存才行，怎么传递？用meta
            yield scrapy.Request(url=url, callback=self.parse_detail, meta={
                'title': title
            })

            # TODO delete this
            break

    def parse_detail(self, response):
        """
        详情页的 parse
        :param response:
        :return:
        """

        # //div[@id="Zoom"]//img/@src
        # xpath 尽量不要去找span, 有可能识别不了
        html_response: HtmlResponse = response
        src = html_response.xpath('//div[@id="Zoom"]//img/@src').extract_first()
        title = html_response.meta['title']
        ILog.debug(__file__, src)

        # 生成item
        movie = ScrapyMovieItem(uuid=UUIDUtility.get_uuid(), title=title, src=src)

        # 交给 pipeline 去下载
        yield movie  # 立即返回一个生成的movie, 也可以用列表添加起来返回一个列表，但是这里在遍历中，我要立即返回一个 item


if __name__ == '__main__':
    cmdline.execute(f'scrapy crawl {SpiderMovieSpider.name}'.split())
