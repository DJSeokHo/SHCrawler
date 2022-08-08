# _*_ coding: utf-8 _*_
# @Time : 2022/08/05 9:57 AM
# @Author : Coding with cat
# @File : urllib_utility
# @Project : SHCrawler
import ssl
import time
import urllib.request
import urllib.parse
from http.client import HTTPResponse, HTTPMessage
from urllib.error import URLError, HTTPError

from framewrok.utility.log_utility import ILog

ssl._create_default_https_context = ssl._create_unverified_context


class ResponseObject:
    __data: str = ""
    __code: int = 0
    __process_time: str = 0
    __url: str = ""
    __message: str = ""
    __error: str = ""

    def __init__(self, data: str, code: int, process_time: str, url: str, message: str, error: str):
        self.__data = data
        self.__code = code
        self.__process_time = process_time
        self.__url = url
        self.__message = message
        self.__error = error

    def get_dictionary(self) -> dict:
        dictionary = {}
        dictionary.update({"data": self.__data})
        dictionary.update({"code": self.__code})
        dictionary.update({"time": self.__process_time})
        dictionary.update({"url": self.__url})
        dictionary.update({"message": self.__message})
        dictionary.update({"error": self.__error})
        return dictionary


class UrlLibUtility:

    @staticmethod
    def get(url: str, headers: dict = None, query_params: dict = None, proxies: dict = None) -> ResponseObject:

        response_object: ResponseObject
        t = time.time()

        try:

            if headers is None:
                headers = {}

            if query_params is not None:
                url = url + '?' + urllib.parse.urlencode(query_params)

            request = urllib.request.Request(url=url, headers=headers)

            if proxies is not None:
                ILog.debug(__file__, str(proxies))
                handler = urllib.request.ProxyHandler(proxies=proxies)
            else:
                if url.startswith("https://"):
                    ILog.debug(__file__, "https")
                    handler = urllib.request.HTTPSHandler()
                else:
                    ILog.debug(__file__, "http")
                    handler = urllib.request.HTTPHandler()

            opener = urllib.request.build_opener(handler)

            response: HTTPResponse = opener.open(request)

            content = response.read().decode('utf-8')
            code = response.getcode()

            process_time = f'{int((time.time() - t) * 1000)}ms'
            response_object = ResponseObject(data=content, code=code, process_time=process_time, url=url, message="", error="")

        except HTTPError as e:
            process_time = f'{int((time.time() - t) * 1000)}ms'
            response_object = ResponseObject(data='', code=e.getcode(), process_time=process_time, url=e.geturl(), message="", error=str(e))
        except URLError as e:
            process_time = f'{int((time.time() - t) * 1000)}ms'
            response_object = ResponseObject(data='', code=-1, process_time=process_time, url=url, message="", error=str(e))

        return response_object

    @staticmethod
    def post(url: str, headers: dict = None, query_params: dict = None, form_data: dict = None, proxies: dict = None) -> ResponseObject:

        response_object: ResponseObject
        t = time.time()

        try:
            if headers is None:
                headers = {}

            if query_params is not None:
                url = url + urllib.parse.urlencode(query_params)

            if form_data is not None:
                form_data = urllib.parse.urlencode(form_data).encode('utf-8')

            request = urllib.request.Request(url=url, data=form_data, headers=headers)

            if proxies is not None:
                ILog.debug(__file__, str(proxies))
                handler = urllib.request.ProxyHandler(proxies=proxies)
            else:
                if url.startswith("https://"):
                    ILog.debug(__file__, "https")
                    handler = urllib.request.HTTPSHandler()
                else:
                    ILog.debug(__file__, "http")
                    handler = urllib.request.HTTPHandler()

            opener = urllib.request.build_opener(handler)

            response: HTTPResponse = opener.open(request)

            content = response.read().decode('utf-8')
            code = response.getcode()

            process_time = f'{int((time.time() - t) * 1000)}ms'
            response_object = ResponseObject(data=content, code=code, process_time=process_time, url=url,
                                             message="", error='')

        except HTTPError as e:
            process_time = f'{int((time.time() - t) * 1000)}ms'
            response_object = ResponseObject(data='', code=e.getcode(), process_time=process_time, url=e.geturl(),
                                             message="", error=e.strerror)
        except URLError as e:
            process_time = f'{int((time.time() - t) * 1000)}ms'
            response_object = ResponseObject(data='', code=-1, process_time=process_time, url=url, message="",
                                             error=e.reason)

        return response_object

    @staticmethod
    def download(url: str, file_name: str) -> ResponseObject:

        t = time.time()
        response_object: ResponseObject

        try:

            results: tuple = urllib.request.urlretrieve(url, file_name)

            message: HTTPMessage = results[1]

            process_time = f'{int((time.time() - t) * 1000)}ms'
            response_object: ResponseObject = ResponseObject(data=file_name, code=0, process_time=process_time, url=url,
                                                             message=str(message), error='')

        except HTTPError as e:
            process_time = f'{int((time.time() - t) * 1000)}ms'
            response_object = ResponseObject(data='', code=e.getcode(), process_time=process_time, url=e.geturl(),
                                             message="", error=e.strerror)
        except URLError as e:
            process_time = f'{int((time.time() - t) * 1000)}ms'
            response_object = ResponseObject(data='', code=-1, process_time=process_time, url=url, message="",
                                             error=e.reason)

        return response_object
