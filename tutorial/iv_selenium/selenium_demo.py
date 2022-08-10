# _*_ coding: utf-8 _*_
# @Time : 2022/08/09 3:03 PM
# @Author : Coding with cat
# @File : selenium_demo
# @Project : SHCrawler

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from framewrok.module.selenium_wrapper.selenium_wrapper import SeleniumWrapper
from framewrok.utility.log_utility import ILog

"""
    让库自动安装
    pip3 install webdriver-manager
"""


def __test_1():
    SeleniumWrapper().chrome_builder('https://www.jd.com') \
        .builder_with_ui() \
        .capture(file_name='jd.png', delay_sec=2) \
        .get_page_source(__page_source) \
        .quite(delay_sec=2)


def __page_source(page_source):
    ILog.debug(__file__, "__page_source")
    ILog.debug(__file__, page_source)


def __test_2():
    # 百度搜索例子
    # 1 找到输入框
    # 2 输入'周杰伦'
    # 3 点击'百度一下'按钮

    SeleniumWrapper().chrome_builder('https://www.baidu.com').builder_with_ui() \
        .get_page_source(__page_source).capture('baidu.png', delay_sec=2) \
        .input_text(by=By.NAME, value='wd', content='周杰伦', delay_sec=2) \
        .click_button(by=By.ID, value='su', delay_sec=2) \
        .scroll_to_bottom(delay_sec=2) \
        .click_button(by=By.XPATH, value='//a[@class="n"]', delay_sec=2) \
        .back(delay_sec=2) \
        .forward(delay_sec=2) \
        .scroll_to_bottom(delay_sec=2) \
        .scroll_to_top(delay_sec=2) \
        .quite(delay_sec=2)


def __test_3():
    # 无界面浏览器

    SeleniumWrapper().chrome_builder('https://www.baidu.com') \
        .builder_none_ui(google_chrome_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome') \
        .capture(file_name='baidu.png', delay_sec=2) \
        .get_page_source(__page_source) \
        .quite(delay_sec=2)


def __test_4():
    SeleniumWrapper().chrome_builder('https://www.baidu.com') \
        .builder_with_ui() \
        .click_button(by=By.ID, value='su', delay_sec=2, on_web_element=__on_web_element) \
        .quite(delay_sec=2)


def __on_web_element(web_element: WebElement):
    ILog.debug(__file__, "__on_web_element")
    ILog.debug(__file__, web_element)
    ILog.debug(__file__, web_element.get_attribute('class'))
    ILog.debug(__file__, web_element.tag_name)
    ILog.debug(__file__, web_element.get_attribute('value'))


if __name__ == '__main__':
    # __test_1()
    # __test_2()
    # __test_3()
    __test_4()
