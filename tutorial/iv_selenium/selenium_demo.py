# _*_ coding: utf-8 _*_
# @Time : 2022/08/09 3:03 PM
# @Author : Coding with cat
# @File : selenium_demo
# @Project : SHCrawler
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from framewrok.utility.log_utility import ILog

"""
    让库自动安装
    pip3 install webdriver-manager
"""


def __test_1():

    # 京东例子
    # 有些网站会检查浏览器，给出不完整的数据
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach", True)

    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)

    url = 'https://www.jd.com'
    # url = 'https://www.baidu.com'
    browser.get(url)

    time.sleep(2)

    content = browser.page_source
    ILog.debug(__file__, content)

    # close只会关闭当前页面，quit会退出驱动并且关闭所关联的所有窗口
    # browser.close()
    browser.quit()


def __test_2():
    # 百度搜索例子
    # 1 找到输入框
    # 2 输入'周杰伦'
    # 3 点击'百度一下'按钮

    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach", True)

    chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)

    try:

        url = 'https://www.baidu.com'
        chrome.get(url)

        time.sleep(2)

        # content = browser.page_source
        # ILog.debug(__file__, content)
        """
        ID = "id"
        XPATH = "xpath"
        LINK_TEXT = "link text"
        PARTIAL_LINK_TEXT = "partial link text"
        NAME = "name"
        TAG_NAME = "tag name"
        CLASS_NAME = "class name"
        CSS_SELECTOR = "css selector"
        """
        # 根据id
        button_by_id = chrome.find_element(by=By.ID, value='su')
        ILog.debug(__file__, button_by_id)
        ILog.debug(__file__, button_by_id.get_attribute('class'))
        ILog.debug(__file__, button_by_id.tag_name)
        ILog.debug(__file__, button_by_id.get_attribute('value'))

        # 根据xpath
        button_by_xpath = chrome.find_element(by=By.XPATH, value='//input[@id="su"]')
        # ILog.debug(__file__, button_by_xpath)

        # 根据name
        input_text = chrome.find_element(by=By.NAME, value='wd')
        # ILog.debug(__file__, input_text)

        # 根据标签
        inputs = chrome.find_elements(by=By.TAG_NAME, value='input')
        # ILog.debug(__file__, inputs)

        input_text.send_keys('周杰伦')

        time.sleep(2)

        button_by_id.click()

        time.sleep(2)

        js_scroll_to_bottom = "document.documentElement.scrollTop=100000"
        chrome.execute_script(js_scroll_to_bottom)

        time.sleep(2)

        next_button_by_xpath = chrome.find_element(by=By.XPATH, value='//a[@class="n"]')
        next_button_by_xpath.click()

        time.sleep(2)

        chrome.execute_script(js_scroll_to_bottom)

        time.sleep(2)

        chrome.back()

        time.sleep(2)

        chrome.forward()

        chrome.execute_script(js_scroll_to_bottom)

        time.sleep(2)

    except Exception as e:
        ILog.debug(__file__, str(e))
    finally:
        # close只会关闭当前页面，quit会退出驱动并且关闭所关联的所有窗口
        # browser.close()
        chrome.quit()


def __test_3():
    # 无界面浏览器

    options = Options()
    options.headless = True

    options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

    options.add_experimental_option("detach", True)

    chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:

        url = 'https://www.baidu.com'
        chrome.get(url)

        time.sleep(2)

        chrome.save_screenshot('baidu.png')
        # content = browser.page_source
        # ILog.debug(__file__, content)
        """
        ID = "id"
        XPATH = "xpath"
        LINK_TEXT = "link text"
        PARTIAL_LINK_TEXT = "partial link text"
        NAME = "name"
        TAG_NAME = "tag name"
        CLASS_NAME = "class name"
        CSS_SELECTOR = "css selector"
        """
        # 根据id
        button_by_id = chrome.find_element(by=By.ID, value='su')
        ILog.debug(__file__, button_by_id)
        ILog.debug(__file__, button_by_id.get_attribute('class'))
        ILog.debug(__file__, button_by_id.tag_name)
        ILog.debug(__file__, button_by_id.get_attribute('value'))

        time.sleep(2)

    except Exception as e:
        ILog.debug(__file__, str(e))
    finally:
        # close只会关闭当前页面，quit会退出驱动并且关闭所关联的所有窗口
        # browser.close()
        chrome.quit()


if __name__ == '__main__':
    # __test_1()
    # __test_2()
    __test_3()
