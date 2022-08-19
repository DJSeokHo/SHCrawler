# _*_ coding: utf-8 _*_
# @Time : 2022/08/05 9:57 AM
# @Author : Coding with cat
# @File : urllib_utility
# @Project : SHCrawler
import ssl
import time
import urllib.request
import urllib.parse
from enum import Enum
from http.client import HTTPResponse, HTTPMessage
from urllib.error import URLError, HTTPError

from framewrok.module.http.response_object.response_object import ResponseObject
from framewrok.utility.log_utility import ILog

ssl._create_default_https_context = ssl._create_unverified_context


class Method(Enum):
    GET = 0
    POST = 1
    PUT = 2
    DELETE = 3


class UrlLibWrapper:

    __original_url: str = ""
    __url: str = ""
    __headers: dict = None
    __proxies: dict = None
    __form_datas: dict = None
    __method: Method = Method.GET

    def url(self, url: str):
        self.__original_url = url
        self.__url = self.__original_url
        return self

    def headers(self, headers: dict):
        self.__headers = headers
        return self

    def query_params(self, query_params: dict):
        self.__url = self.__original_url + '?' + urllib.parse.urlencode(query_params)
        return self

    def form_datas(self, form_datas: dict, method: Method = Method.POST):
        self.__form_datas = form_datas
        self.__method = method
        return self

    def proxies(self, proxies: dict):
        self.__proxies = proxies
        return self

    def response(self) -> ResponseObject:

        response_object: ResponseObject
        t = time.time()

        try:

            # headers
            if self.__headers is None:
                self.__headers = {}

            # proxy
            if self.__proxies is not None:
                ILog.debug(__file__, str(self.__proxies))
                handler = urllib.request.ProxyHandler(proxies=self.__proxies)
            else:
                if self.__url.startswith("https://"):
                    ILog.debug(__file__, "https")
                    handler = urllib.request.HTTPSHandler()
                else:
                    ILog.debug(__file__, "http")
                    handler = urllib.request.HTTPHandler()

            if self.__method == Method.GET:
                request = urllib.request.Request(url=self.__url, headers=self.__headers)
            else:

                form_data = None
                if self.__form_datas is not None:
                    form_data = urllib.parse.urlencode(self.__form_datas).encode('utf-8')

                request = urllib.request.Request(url=self.__url, data=form_data, headers=self.__headers)

            opener = urllib.request.build_opener(handler)

            response: HTTPResponse = opener.open(request)

            content = response.read().decode('utf-8')
            code = response.getcode()

            process_time = f'{int((time.time() - t) * 1000)}ms'
            response_object = ResponseObject(data=content, code=code, process_time=process_time, url=self.__url,
                                             proxy=str(self.__proxies), message="", error="")
        except HTTPError as e:
            process_time = f'{int((time.time() - t) * 1000)}ms'
            response_object = ResponseObject(data='', code=e.getcode(), process_time=process_time, url=self.__url,
                                             proxy=str(self.__proxies), message="", error=str(e))
        except Exception as e:
            process_time = f'{int((time.time() - t) * 1000)}ms'
            response_object = ResponseObject(data='', code=-1, process_time=process_time, url=self.__url, message="",
                                             proxy=str(self.__proxies), error=str(e))
        return response_object

    def just_download(self, file_name: str):
        urllib.request.urlretrieve(self.__url, file_name)

    def download(self, file_name: str) -> ResponseObject:

        t = time.time()
        response_object: ResponseObject

        try:

            results: tuple = urllib.request.urlretrieve(self.__url, file_name)

            message: HTTPMessage = results[1]

            process_time = f'{int((time.time() - t) * 1000)}ms'
            response_object: ResponseObject = ResponseObject(data=file_name, code=200, process_time=process_time,
                                                             url=self.__url, proxy=str(self.__proxies),
                                                             message=str(message), error='')

        except HTTPError as e:
            process_time = f'{int((time.time() - t) * 1000)}ms'
            response_object = ResponseObject(data='', code=e.getcode(), process_time=process_time, url=self.__url,
                                             proxy=str(self.__proxies), message="", error=e.strerror)
        except URLError as e:
            process_time = f'{int((time.time() - t) * 1000)}ms'
            response_object = ResponseObject(data='', code=-1, process_time=process_time, url=self.__url, message="",
                                             proxy=str(self.__proxies), error=e.reason)

        return response_object

    @staticmethod
    def encode(query_params) -> str:
        return urllib.parse.urlencode(query_params, encoding='utf-8')
