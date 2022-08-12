# coding: utf-8
from framewrok.utility.log_utility import ILog


class Executor:

    @staticmethod
    def execute_sql_without_result(sql, connect):
        try:
            db_cursor = connect.cursor()
            db_cursor.execute(sql)
            connect.commit()
            ILog.debug(__file__, sql)
            ILog.debug(__file__, "success")
        except Exception as e:
            ILog.debug(__file__, e)
            connect.rollback()
            connect.commit()
            raise e

    @staticmethod
    def execute_sql_with_result_list(sql, connect) -> list:

        result_list = []
        try:

            db_cursor = connect.cursor()
            result_cursor = db_cursor.execute(sql)

            # result_cursor is a tuple list
            for row in result_cursor:
                result_list.append(row)

            ILog.debug(__file__, sql)
            ILog.debug(__file__, "success")
            return result_list

        except Exception as e:
            ILog.debug(__file__, e)
            raise e
