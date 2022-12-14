# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from framewrok.utility.log_utility import ILog


class WeiboHashtagPopularPipeline:

    def __init__(self):
        self.fp = None

    def open_spider(self, spider):
        """
        这是 override的。
        :param spider:
        :return:
        """
        ILog.debug(__file__, 'open_spider')
        self.fp = open('drama_topic.json', 'w', encoding='utf-8')
        ILog.debug(__file__, type(self.fp))

    # item 就是 yield 传过来的数据
    def process_item(self, item, spider):
        # 这里用追加模式，所以是 a 不是 w
        # 每次都要打开关闭文件，效率很低
        # with open('movies.json', 'a', encoding='utf-8') as fp:
        #     fp.write(str(item))
        ILog.debug(__file__, f'process_item {str(item)}')
        self.fp.write(f'{str(item)},')

        return item

    def close_spider(self, spider):
        """
         这是 override的。
        :param spider:
        :return:
        """
        self.fp.close()
        ILog.debug(__file__, 'close_spider')
