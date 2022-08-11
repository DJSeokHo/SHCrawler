# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os
from io import TextIOWrapper

from itemadapter import ItemAdapter

from framewrok.module.http.url_lib_wrapper.url_lib_wrapper import UrlLibWrapper
from framewrok.utility.log_utility import ILog

"""
如果想使用管道的话，那么就必须在 settings 中开启管道
"""


class ScrapyDangDangPipeline:

    def __init__(self):
        self.fp = None

    def open_spider(self, spider):
        """
        这是 override的。
        :param spider:
        :return:
        """
        ILog.debug(__file__, 'open_spider')
        self.fp = open('book.json', 'w', encoding='utf-8')
        ILog.debug(__file__, type(self.fp))

        if not os.path.exists('books'):
            ILog.debug(__file__, 'create books')
            os.makedirs('books')

    # item 就是 yield 传过来的数据
    def process_item(self, item, spider):
        # 这里用追加模式，所以是 a 不是 w
        # 每次都要打开关闭文件，效率很低
        # with open('book.json', 'a', encoding='utf-8') as fp:
        #     fp.write(str(item))
        self.fp.write(str(item))
        return item

    def close_spider(self, spider):
        """
         这是 override的。
        :param spider:
        :return:
        """
        self.fp.close()
        ILog.debug(__file__, 'close_spider')


# 多条管道同时开启
# 1. 定义管道类
# 2. 在settings中开启管道
# 'scrapy_dang_dang.pipelines.ScrapyDangDangDownloadPipeline': 301
class ScrapyDangDangDownloadPipeline:

    def process_item(self, item, spider):

        url = f'http:{item.get("src")}'
        file_name = f'./books/{item.get("uuid")}.jpg'
        ILog.debug(__file__, f'{url} {file_name}')

        UrlLibWrapper().url(url).download(file_name=file_name, just_download=True)

        return item
