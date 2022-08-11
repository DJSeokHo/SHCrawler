# _*_ coding: utf-8 _*_
# @Time : 2022/08/05 9:57 AM
# @Author : Coding with cat
# @File : urllib_utility
# @Project : SHCrawler
import ssl
import time
from urllib.error import HTTPError

import requests

from framewrok.module.http.response_object.response_object import ResponseObject

ssl._create_default_https_context = ssl._create_unverified_context


class RequestsWrapper:

    __requester = None

    __url: str = ""
    __headers: dict = None
    __proxies: dict = None
    __query_params: dict = None
    __form_datas: dict = None

    def url(self, url: str):
        self.__url = url

        self.__requester = requests

        return self

    def headers(self, headers: dict):
        self.__headers = headers
        return self

    def query_params(self, query_params: dict):
        self.__query_params = query_params
        return self

    def form_datas(self, form_datas: dict):
        self.__form_datas = form_datas
        return self

    def proxies(self, proxies: dict):
        self.__proxies = proxies
        return self

    def session(self, with_session: bool):
        if with_session:
            self.__requester = requests.session()
        return self

    def download(self, url: str, file_name: str):

        code_response = self.__requester.get(url)
        code_content = code_response.content

        with open(file_name, 'wb') as fp:
            fp.write(code_content)

        return self

    def get(self) -> ResponseObject:

        response_object: ResponseObject
        t = time.time()

        try:

            response = self.__requester.get(url=self.__url, params=self.__query_params, headers=self.__headers,
                                            proxies=self.__proxies)
            response.encoding = 'utf-8'

            content = response.content.decode('utf-8')
            code = response.status_code

            process_time = f'{int((time.time() - t) * 1000)}ms'

            response_object = ResponseObject(data=content, code=code, process_time=process_time, url=self.__url,
                                             proxy=str(self.__proxies), message="", error="")
        except HTTPError as e:
            process_time = f'{int((time.time() - t) * 1000)}ms'
            response_object = ResponseObject(data='', code=e.getcode(), process_time=process_time, url=self.__url,
                                             proxy=str(self.__proxies), message="", error=str(e))
        except Exception as e:
            process_time = f'{int((time.time() - t) * 1000)}ms'
            response_object = ResponseObject(data='', code=-1, process_time=process_time, url=self.__url,
                                             proxy=str(self.__proxies), message="", error=str(e))

        return response_object

    def post(self) -> ResponseObject:

        response_object: ResponseObject
        t = time.time()

        try:

            response = self.__requester.post(url=self.__url, params=self.__query_params, data=self.__form_datas,
                                             headers=self.__headers, proxies=self.__proxies)
            response.encoding = 'utf-8'

            content = response.content.decode('utf-8')
            code = response.status_code

            process_time = f'{int((time.time() - t) * 1000)}ms'

            response_object = ResponseObject(data=content, code=code, process_time=process_time, url=self.__url,
                                             proxy=str(self.__proxies), message="", error="")
        except HTTPError as e:
            process_time = f'{int((time.time() - t) * 1000)}ms'
            response_object = ResponseObject(data='', code=e.getcode(), process_time=process_time, url=self.__url,
                                             proxy=str(self.__proxies), message="", error=str(e))
        except Exception as e:
            process_time = f'{int((time.time() - t) * 1000)}ms'
            response_object = ResponseObject(data='', code=-1, process_time=process_time, url=self.__url,
                                             proxy=str(self.__proxies), message="", error=str(e))

        return response_object
