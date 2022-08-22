import random
import time

import scrapy
from scrapy import cmdline, Selector, Request
from scrapy.http import HtmlResponse

from examples.weibo_hashtag_popular.weibo_hashtag_popular.items import WeiboHashtagPopularItem
from framewrok.module.http.url_lib_wrapper.url_lib_wrapper import UrlLibWrapper
from framewrok.utility.log_utility import ILog
from framewrok.utility.proxies_utility import ProxiesUtility


class SpiderWeiboHashtagPopularSpider(scrapy.Spider):
    name = 'spider_weibo_hashtag_popular'
    allowed_domains = ['s.weibo.com', 'www.kan.cc']
    # start_urls = ['https://s.weibo.com/weibo']

    # https://www.kan.cc/search.html?page=1&searchtype=5&order=time&tid=1&year=2022 看韩剧
    # https://s.weibo.com/weibo?q=%E5%A5%87%E6%80%AA%E7%9A%84%E5%BE%8B%E5%B8%88%E7%A6%B9%E8%8B%B1%E9%9B%A8 微博话题详情

    def start_requests(self):
        yield self.get_drama_list()

    def get_drama_list(self):

        year = time.strftime("%Y", time.localtime())
        parameter = {
            'page': '1',
            'searchtype': '5',
            'order': 'time',
            'tid': '1',
            'year': year,
        }

        url = f'https://www.kan.cc/search.html?{UrlLibWrapper.encode(parameter)}'
        ILog.debug(__file__, url)

        headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,"
                      "*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            # "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9,ko;q=0.8,zh-TW;q=0.7,en;q=0.6",
            "cache-control": "max-age=0",
            "cookie": "Hm_lvt_193d42d6df9341f3a303004df15e3f0d=1660870107; "
                      "_hjSessionUser_2880106=eyJpZCI6Ijk2YzdiNjk3LTUwMjgtNWVlMC04ZjEzLTJlZWZmZWJlMWE2NyIsImNyZWF0ZWQiOjE2NjA4NzAxMDgwNzAsImV4aXN0aW5nIjp0cnVlfQ==; _funcdn_token=0d88a0fa170086943b8a40685db3dc9575d09ed68568475a6c2171b4c0eddb92; Hm_lpvt_193d42d6df9341f3a303004df15e3f0d=1660870175",
            "if-modified-since": "Fri, 19 Aug 2022 00:48:50 GMT",
            "referer": "https://www.kan.cc/search.html?page=1&searchtype=5&order=hit&tid=1&year=2022",
            "sec-ch-ua": "\"Chromium\";v=\"104\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"104\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"macOS\"",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "same-origin", "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/104.0.0.0 Safari/537.36"
        }

        proxy = ProxiesUtility.get_ssl_proxy_string()
        ILog.debug(__file__, f'proxy is {proxy}')
        return scrapy.Request(url=url, headers=headers, meta={'proxy': proxy},
                              callback=self.parse_drama_list)

    def parse_drama_list(self, response):
        html_response: HtmlResponse = response
        # ILog.debug(__file__, html_response.text)

        title_list = html_response.xpath('//ul[@class="myui-vodlist clearfix"]//li//div['
                                         '@class="myui-vodlist__detail"]//a/text()')
        title: Selector
        for item in title_list:
            title = item
            ILog.debug(__file__, title.get())

        title: Selector
        for i in range(0, len(title_list)):

            title = title_list[i]
            yield self.get_topic_value(title.get())
            time.sleep(random.choice([0.1, 0.5, 1, 1.5, 2]))

    def get_topic_value(self, title):
        ILog.debug(__file__, f'get_topic_value {title}')
        parameter = {
            'q': f'#{title}#'
        }

        url = f'https://s.weibo.com/weibo?{UrlLibWrapper.encode(parameter)}'
        ILog.debug(__file__, url)

        parameter_for_referer = {
            'q': title,
            'pagetype': 'topic',
            'topic': '1',
            'Refer': 'weibo_topic'
        }

        referer = f'https://s.weibo.com/topic?{UrlLibWrapper.encode(parameter_for_referer)}'
        ILog.debug(__file__, f'referer is {referer}')

        headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,"
                      "*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            # "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9,ko;q=0.8,zh-TW;q=0.7,en;q=0.6",
            "cookie": "login_sid_t=dad79da3fddc0e3fa0f92ea665ee873e; cross_origin_proto=SSL; "
                      "_s_tentry=passport.weibo.com; Apache=2763422235674.613.1652751815618; "
                      "SINAGLOBAL=2763422235674.613.1652751815618; "
                      "ULV=1652751815621:1:1:1:2763422235674.613.1652751815618:; "
                      "WBtopGlobal_register_version=2022051709; SSOLoginState=1652751840; "
                      "XSRF-TOKEN=EL1hfx1JJ9Z743JWhEn1pKrl; YF-V-WEIBO-G0=b09171a17b2b5a470c42e2f713edace0; "
                      "SCF=Aj6ZlH9rjOrnyy_1_9mZY0OFXtR53aVEAbaqEXcPSv990QwpgEQWejGT2KtZyHDE3YkV9uG_TCiCl1vcjv3ZiCA.; "
                      "SUB=_2A25OBpD4DeRhGeVM61IX9i7Lwz6IHXVtdYUwrDV8PUNbmtAfLXbfkW9NTMKiQWUn35-JKI4cdGEVwpUnuVDbrW1v"
                      "; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WW9uubII4-Ou2jXh4f6QDNv5JpX5KMhUgL"
                      ".FoeEeh5cSo5N1hz2dJLoIpUKHcHDdbH8SFHF1FHF1CH8SCHWSbHWxBtt; ALF=1692668966; "
                      "WBPSESS=s-0NQ4M0QVQpcAEHgxJPBrcZKtb9tN3_hCT0PgdZ2KV-Aw1SBjKwWG3ZPu"
                      "-q9ekbTW37V9ll6dvnBTDrDnPxMSQ7CR5c5d4LstqlDxSCoD67crPMXjqceneSUEeJaRFR62iqEgZzy2-4PLpQIlzR1A==",
            "referer": referer,
            "sec-ch-ua": "\"Chromium\";v=\"104\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"104\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"macOS\"",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "same-origin", "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/104.0.0.0 Safari/537.36"
        }

        return scrapy.Request(url=url, headers=headers, meta={'title': title, 'proxy': ''}, callback=self.parse_detail)

    def parse_detail(self, response):
        ILog.debug(__file__, f'parse_detail')

        html_response: HtmlResponse = response
        # ILog.debug(__file__, html_response.text)

        title = html_response.meta['title']

        try:

            span_list: [Selector] = html_response.xpath('//div[@class="info"]//div[@class="total"]//span/text()')
            if len(span_list) == 0:
                ILog.debug(__file__, f'{title} span_list ??? {len(span_list)}')
                return

            item = WeiboHashtagPopularItem(
                title=title,
                today_view=span_list[0].get(),
                today_discussion=span_list[1].get()
            )

            ILog.debug(__file__, f'yield item {str(item)}')
            yield item

        except Exception as e:
            ILog.debug(__file__, f'????? {str(e)}')
            retry: Request = html_response.request
            retry = retry.copy()
            retry.dont_filter = True
            yield retry


if __name__ == '__main__':
    cmdline.execute(f'scrapy crawl {SpiderWeiboHashtagPopularSpider.name}'.split())
    # ILog.debug(__file__, time.strftime("%Y", time.localtime()))
    # ILog.debug(__file__, os.path.join("aaa", "bbb", "dushu.sqlite3"))
