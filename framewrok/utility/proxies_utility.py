# _*_ coding: utf-8 _*_
# @Time : 2022/08/08 4:34 PM
# @Author : Coding with cat
# @File : proxies_utility
# @Project : SHCrawler
import random

from bs4 import BeautifulSoup

from framewrok.module.http.url_lib_wrapper.url_lib_wrapper import UrlLibWrapper


class ProxyModel:

    __ip: str = ""
    __port: str = ""
    __anonymity: str = ""
    __https: str = ""

    def __init__(self, ip: str, port: str, anonymity: str, https: str):
        self.__ip = ip
        self.__port = port
        self.__anonymity = anonymity
        self.__https = https

    def get_ip(self) -> str:
        return self.__ip

    def get_port(self) -> str:
        return self.__port

    def get_anonymity(self) -> str:
        return self.__anonymity

    def get_https(self) -> str:
        return self.__https

    def to_proxy_dict(self) -> dict:

        if self.__https == 'yes':
            protocol = 'https'
        else:
            protocol = 'http'

        return {
            protocol: f'{self.__ip}:{self.__port}'
        }


class ProxiesUtility:

    @staticmethod
    def get_ssl_proxy() -> ProxyModel:

        response_object = UrlLibWrapper().url('https://www.sslproxies.org/').headers({
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,"
                      "*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            # "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9,ko;q=0.8,zh-TW;q=0.7,en;q=0.6",
            "cache-control": "max-age=0",
            "cookie": "_gid=GA1.2.1758933792.1659942216; _ga_F5HK5559Z2=GS1.1.1659942215.2.1.1659944018.0; "
                      "_ga=GA1.2.2091794637.1659707631",
            # "if-modified-since": "Mon, 08 Aug 2022 07:32:02 GMT",
            "referer": "https://www.google.com/",
            "sec-ch-ua": "\"Chromium\";v=\"104\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"104\"",
            "sec-ch-ua-mobile": "?0", "sec-ch-ua-platform": "\"macOS\"", "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate", "sec-fetch-site": "cross-site", "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/104.0.0.0 Safari/537.36 "
        }).response()

        soup = BeautifulSoup(response_object.get_data(), 'html5lib')
        tr_tag_list = soup.select('table[class="table table-striped table-bordered"] tbody tr', limit=10)

        proxies = list()
        proxy_model: ProxyModel
        for tr_tag in tr_tag_list:
            td_tag_list = tr_tag.select('td')
            proxy_model = ProxyModel(
                ip=td_tag_list[0].get_text(),
                port=td_tag_list[1].get_text(),
                anonymity=td_tag_list[4].get_text(),
                https=td_tag_list[6].get_text()
            )

            if proxy_model.get_anonymity() == 'elite proxy' or proxy_model.get_anonymity() == 'anonymous':
                proxies.append(proxy_model.to_proxy_dict())

        return random.choice(proxies)


if __name__ == '__main__':
    ProxiesUtility.get_ssl_proxy()
