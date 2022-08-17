# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from framewrok.module.sqlite.sqlite_wrapper import SQLiteWrapper
from framewrok.utility.log_utility import ILog
from tutorial.vi_scrapy.scrapy_dushu.scrapy_dushu.items import ScrapyDushuItem


class ScrapyDushuPipeline:

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

    # item 就是 yield 传过来的数据
    def process_item(self, item, spider):
        # 这里用追加模式，所以是 a 不是 w
        # 每次都要打开关闭文件，效率很低
        # with open('movies.json', 'a', encoding='utf-8') as fp:
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


# 'scrapy_dushu.pipelines.ScrapyDushuSQLitePipeline': 301
class ScrapyDushuSQLitePipeline:

    def open_spider(self, spider):
        """
        这是 override的。
        :param spider:
        :return:
        """
        ILog.debug(__file__, 'open_spider')

        SQLiteWrapper.instance().open(db_folder='database', db_path='database/dushu.sqlite3')

        sql = '''
            CREATE TABLE IF NOT EXISTS 'BOOK_TABLE' ( \
            'ID' INTEGER PRIMARY KEY AUTOINCREMENT, \
            'UUID' TEXT NOT NULL, \
            'NAME' TEXT NOT NULL, \
            'SRC' TEXT NOT NULL \
            ); \
            '''
        SQLiteWrapper.instance().create_table(sql)

    # item 就是 yield 传过来的数据
    def process_item(self, item, spider):

        scrapyDushuItem: ScrapyDushuItem = item

        insert_sql = '''
          REPLACE INTO BOOK_TABLE \
          (UUID, NAME, SRC) \
          VALUES \
          ('%s', '%s', '%s');
          ''' % (scrapyDushuItem.get('uuid'), scrapyDushuItem.get('name'), scrapyDushuItem.get('src'))

        SQLiteWrapper.instance().execute_sql(insert_sql)

        return item

    def close_spider(self, spider):
        """
         这是 override的。
        :param spider:
        :return:
        """

        SQLiteWrapper.instance().close()
        ILog.debug(__file__, 'close_spider')