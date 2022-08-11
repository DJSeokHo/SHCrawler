# _*_ coding: utf-8 _*_
# @Time : 2022/08/11 10:24 AM
# @Author : Coding with cat
# @File : response_object
# @Project : SHCrawler

class ResponseObject:

    __data: str = ""
    __code: int = 0
    __process_time: str = 0
    __url: str = ""
    __proxy: str = ""
    __message: str = ""
    __error: str = ""

    def __init__(self, data: str, code: int, process_time: str, url: str, proxy: str, message: str, error: str):
        self.__data = data
        self.__code = code
        self.__process_time = process_time
        self.__url = url
        self.__proxy = proxy
        self.__message = message
        self.__error = error

    def get_dictionary(self) -> dict:
        dictionary = {}
        dictionary.update({"data": self.__data})
        dictionary.update({"code": self.__code})
        dictionary.update({"time": self.__process_time})
        dictionary.update({"url": self.__url})
        dictionary.update({"proxy": self.__proxy})
        dictionary.update({"message": self.__message})
        dictionary.update({"error": self.__error})
        return dictionary

    def get_data(self) -> str:
        return self.__data
