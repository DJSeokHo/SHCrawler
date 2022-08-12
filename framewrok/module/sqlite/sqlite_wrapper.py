# coding: utf-8
import os
import sqlite3

from framewrok.module.sqlite.executor import Executor
from framewrok.utility.log_utility import ILog
from framewrok.utility.uuid_utility import UUIDUtility


class SQLiteWrapper:
    __instance = None
    __connect = None
    __db_folder: str = ""
    __db_path: str = ""

    @classmethod
    def instance(cls):
        if not cls.__instance:
            cls.__instance = cls()
        return cls.__instance

    def open(self, db_folder, db_path):
        ILog.debug(__file__, "open")
        self.__db_folder = db_folder
        self.__db_path = db_path

        self.__check_db_file()

        self.close()
        """
        open data base and create table
        :return:
        """
        if self.__connect is not None:
            return

        self.__connect = sqlite3.connect(self.__db_path, check_same_thread=False)

    def __check_db_file(self):
        if not os.path.exists(self.__db_folder):
            ILog.debug(__file__, "create folder")
            os.makedirs(self.__db_folder)

        if not os.path.exists(self.__db_path):
            ILog.debug(__file__, "create file")
            db_file = open(self.__db_path, "w")
            db_file.close()

    def create_table(self, sql):
        try:
            Executor.execute_sql_without_result(sql, self.__connect)
        except Exception as e:
            raise e

    def execute_sql(self, sql):
        try:
            Executor.execute_sql_without_result(sql, self.__connect)
        except Exception as e:
            raise e

    def execute_sql_with_return(self, sql) -> list:

        try:
            result = Executor.execute_sql_with_result_list(sql, self.__connect)
        except Exception as e:
            raise e

        return result

    def close(self):
        """
        close data base
        :param self:
        :return:
        """
        if self.__connect is None:
            return

        self.__connect.close()
        self.__connect = None


if __name__ == '__main__':
    SQLiteWrapper.instance().open(db_folder='database', db_path='database/test.sqlite3')

    sql = '''
    CREATE TABLE IF NOT EXISTS 'TEST_TABLE' ( \
    'ID' INTEGER PRIMARY KEY AUTOINCREMENT, \
    'UUID' TEXT NOT NULL, \
    'CONTENT' TEXT NOT NULL
    ); \
    '''

    insert_sql = '''
    REPLACE INTO TEST_TABLE \
    (UUID, CONTENT) \
    VALUES \
    ('%s', '%s');
    ''' % (UUIDUtility.get_uuid(), "test content")

    select_sql = '''
    SELECT * FROM TEST_TABLE
    '''

    SQLiteWrapper.instance().create_table(sql)

    SQLiteWrapper.instance().execute_sql(insert_sql)

    result_list = SQLiteWrapper.instance().execute_sql_with_return(select_sql)

    for result in result_list:
        ILog.debug(__file__, str(result))

    SQLiteWrapper.instance().close()
