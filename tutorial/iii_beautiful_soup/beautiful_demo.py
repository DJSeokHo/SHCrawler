# _*_ coding: utf-8 _*_
# @Time : 2022/08/08 11:13 AM
# @Author : Coding with cat
# @File : beautiful_demo
# @Project : SHCrawler

from bs4 import BeautifulSoup

from framewrok.module.url_lib_wrapper.url_lib_wrapper import UrlLibWrapper
from framewrok.utility.log_utility import ILog
from framewrok.utility.proxies_utility import ProxiesUtility


def __test_1():
    # 解析本地文件

    soup = BeautifulSoup(open('local_test_file.html', encoding='utf-8'), 'html5lib')
    # ILog.debug(__file__, soup)
    # find 获取第一个符合的标签
    ILog.debug(__file__, soup.find('a'))

    # find 获取第一个符合的标签，附加条件是title的值
    ILog.debug(__file__, soup.find('a', title='a2'))
    # find 获取第一个符合的标签，附加条件是class的值, class 是关键字，所以在后面加一个下划线
    ILog.debug(__file__, soup.find('a', class_='a1'))

    # attrs 获取标签的属性和值，字典形式
    ILog.debug(__file__, soup.find('a').attrs)

    # find 获取所有符合的标签, 返回列表
    ILog.debug(__file__, soup.find_all('a'))

    # find 获取所有符合的标签, 返回列表, 这里是寻找 a 和 span, 注意: a和span 需要放在列表里
    ILog.debug(__file__, soup.find_all(['a', 'span']))
    ILog.debug(__file__, soup.find_all('li'))
    ILog.debug(__file__, soup.find_all('li', limit=2))

    # 推荐使用select
    # select 获取所有符合的标签, 返回列表
    ILog.debug(__file__, soup.select('a'))

    # select 支持类选择器操作
    ILog.debug(__file__, soup.select('.a1'))

    # select 支持类选择器操作
    ILog.debug(__file__, soup.select('#l1'))

    # select 支持属性选择器, 选择 li 里带 id 的标签
    ILog.debug(__file__, soup.select('li[id]'))

    # select 支持属性选择器, 选择 li 里带 id 的标签
    ILog.debug(__file__, soup.select('li[id="l2"]'))

    # 层级选择器
    # 找到 div下的li
    ILog.debug(__file__, soup.select('div li'))

    # 子代选择器
    ILog.debug(__file__, soup.select('div > ul > li'))
    ILog.debug(__file__, soup.select('a, li'))

    div_tag = soup.select('#d1')[0]
    ILog.debug(__file__, div_tag.get_text())

    # 节点的属性
    p_tag = soup.select('#id_p1')[0]
    ILog.debug(__file__, p_tag.attrs.get('class'))


def __test_2():
    # beautiful soup 采集星巴克

    response_object = UrlLibWrapper().url('https://www.starbucks.com.cn/menu/').headers({
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
                  "application/signed-exchange;v=b3;q=0.9",
        # "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,ko;q=0.8,zh-TW;q=0.7,en;q=0.6",
        "Cache-Control": "max-age=0", "Connection": "keep-alive",
        "Cookie": "_ga=GA1.3.1074637402.1659941941; _gid=GA1.3.891670170.1659941941; "
                  "ZHh6ku4z=A9DsP3yCAQAARVkCQtZYmSv7pNIpu3LSmDOb0graMUzeWqCx4mQha2VEBjaVAd5qSdGucm46wH8AAOfvAAAAAA|1"
                  "|1|f9bfccca0c6f082780b75739e4be3bc0e9824720",
        "Host": "www.starbucks.com.cn",
        # "If-Modified-Since": "Tue, 02 Aug 2022 13:37:13 GMT",
        # "If-None-Match": "W/\"62e92889-e33b\"",
        "Referer": "https://www.starbucks.com.cn/",
        "sec-ch-ua": "\"Chromium\";v=\"104\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"104\"",
        "sec-ch-ua-mobile": "?0", "sec-ch-ua-platform": "\"macOS\"", "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/104.0.0.0 Safari/537.36"
    }).proxies(ProxiesUtility.get_ssl_proxy().to_proxy_dict()).response()
    '''
    网站采取了强缓存验证， 服务器将要爬取的内容在本地做了缓存，
    再次请求的时候，会首先检查本地缓存中是否已存在，如果有就返回304
    
    解决方法：
    在requests headers中，禁用删除If - Modified-Since 和If-None-Natch 这两项，服务器是通过检查这两项来判断是否是已经做了缓存。
    '''

    ILog.debug(__file__, response_object.get_dictionary())

    soup = BeautifulSoup(response_object.get_data(), 'html5lib')
    produce_tag_list = soup.select('ul[class="grid padded-3 product"] strong')
    produce_list = list()
    for produce_tag in produce_tag_list:
        produce_list.append(produce_tag.get_text())

    ILog.debug(__file__, produce_list)


if __name__ == '__main__':
    # __test_1()
    __test_2()
