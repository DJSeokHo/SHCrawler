# _*_ coding: utf-8 _*_
# @Time : 2022/08/10 9:52 AM
# @Author : Coding with cat
# @File : selenium_wrapper
# @Project : SHCrawler

import time

from selenium.webdriver.chrome.webdriver import WebDriver

from framewrok.utility.log_utility import ILog
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


"""
    让库自动安装
    pip3 install webdriver-manager
"""

"""
by:

ID = "id"
XPATH = "xpath"
LINK_TEXT = "link text"
PARTIAL_LINK_TEXT = "partial link text"
NAME = "name"
TAG_NAME = "tag name"
CLASS_NAME = "class name"
CSS_SELECTOR = "css selector"
"""


class SeleniumWrapper:

    __url = ""
    __web_driver: WebDriver

    def chrome_builder(self, url):
        self.__url = url
        return self

    def builder_with_ui(self):

        try:
            options = webdriver.ChromeOptions()
            options.add_experimental_option("detach", True)

            self.__web_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
            self.__web_driver.get(self.__url)
        except Exception as e:
            ILog.debug(__file__, str(e))
            self.__web_driver.quit()
        finally:
            return self

    def builder_none_ui(self, google_chrome_path: str):

        try:
            options = Options()
            options.headless = True

            options.binary_location = google_chrome_path

            options.add_experimental_option("detach", True)

            self.__web_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
            self.__web_driver.get(self.__url)
        except Exception as e:
            ILog.debug(__file__, str(e))
            self.__web_driver.quit()
        finally:
            return self

    def get_page_source(self, on_page_source_str):
        try:
            return on_page_source_str(self.__web_driver.page_source)
        except Exception as e:
            ILog.debug(__file__, str(e))
            self.__web_driver.quit()
        finally:
            return self

    def capture(self, file_name: str, delay_sec: int = 0):
        try:
            time.sleep(delay_sec)

            self.__web_driver.save_screenshot(file_name)
        except Exception as e:
            ILog.debug(__file__, str(e))
            self.__web_driver.quit()
        finally:
            return self

    def input_text(self, by: By, value: str, content: str, delay_sec: int = 0, on_web_element=None):

        try:
            time.sleep(delay_sec)
            input_text = self.__web_driver.find_element(by=by, value=value)
            on_web_element(input_text)

            input_text.send_keys(content)
        except Exception as e:
            ILog.debug(__file__, str(e))
            self.__web_driver.quit()
        finally:
            return self

    def click_button(self, by: By, value: str, delay_sec: int = 0, on_web_element=None):

        try:
            time.sleep(delay_sec)

            button = self.__web_driver.find_element(by=by, value=value)
            on_web_element(button)

            button.click()
        except Exception as e:
            ILog.debug(__file__, str(e))
            self.__web_driver.quit()
        finally:
            return self

    def scroll_to_top(self, delay_sec: int = 0):

        try:
            time.sleep(delay_sec)

            self.__web_driver.execute_script("document.documentElement.scrollTop=0")
        except Exception as e:
            ILog.debug(__file__, str(e))
            self.__web_driver.quit()
        finally:
            return self

    def scroll_to_bottom(self, delay_sec: int = 0):

        try:
            time.sleep(delay_sec)

            self.__web_driver.execute_script("document.documentElement.scrollTop=100000")
        except Exception as e:
            ILog.debug(__file__, str(e))
            self.__web_driver.quit()
        finally:
            return self

    def execute_script(self, script: str, delay_sec: int = 0):

        try:
            time.sleep(delay_sec)

            self.__web_driver.execute_script(script)
        except Exception as e:
            ILog.debug(__file__, str(e))
            self.__web_driver.quit()
        finally:
            return self

    def back(self, delay_sec: int = 0):
        try:
            time.sleep(delay_sec)

            self.__web_driver.back()
        except Exception as e:
            ILog.debug(__file__, str(e))
            self.__web_driver.quit()
        finally:
            return self

    def forward(self, delay_sec: int = 0):
        try:
            time.sleep(delay_sec)

            self.__web_driver.forward()
        except Exception as e:
            ILog.debug(__file__, str(e))
            self.__web_driver.quit()
        finally:
            return self

    def quite(self, delay_sec: int = 0):
        try:
            time.sleep(delay_sec)

            # close只会关闭当前页面，quit会退出驱动并且关闭所关联的所有窗口
            # browser.close()
            self.__web_driver.quit()
        except Exception as e:
            ILog.debug(__file__, str(e))
            self.__web_driver.quit()
        finally:
            return self
