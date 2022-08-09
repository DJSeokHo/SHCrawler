# _*_ coding: utf-8 _*_
# @Time : 2022/08/09 10:15 PM
# @Author : Coding with cat
# @File : request_demo
# @Project : SHCrawler
import requests

from framewrok.utility.json_utility import JSONUtility
from framewrok.utility.log_utility import ILog
from framewrok.utility.proxies_utility import ProxiesUtility


def __test_1():
    url = 'https://www.baidu.com'

    response = requests.get(url=url)
    response.encoding = 'utf-8'

    ILog.debug(__file__, type(response))
    ILog.debug(__file__, f'1 {response.text}')  # 网页的源码字符串
    ILog.debug(__file__, f'2 {response.url}')
    ILog.debug(__file__, f'3 {response.content}')  # 返回网页的二进制
    ILog.debug(__file__, f'4 {response.status_code}')
    ILog.debug(__file__, f'5 {response.headers}')


def __test_2():
    url = 'https://www.baidu.com/s'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/104.0.0.0 Safari/537.36 '
    }

    query_params = {
        'wd': '周杰伦'
    }

    response = requests.get(url=url, params=query_params, headers=headers,
                            proxies=ProxiesUtility.get_ssl_proxy().to_proxy_dict())
    ILog.debug(__file__, response.text)


def __test_3():

    url = 'https://fanyi.baidu.com/sug'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/104.0.0.0 Safari/537.36 '
    }

    form_datas = {
        'kw': 'hello'
    }

    response = requests.post(url=url, data=form_datas, headers=headers)

    ILog.debug(__file__, JSONUtility.to_json_object(response.text).get("data"))


if __name__ == '__main__':
    # __test_1()
    __test_2()
    # __test_3()
