# coding: utf-8
class ILog:

    @staticmethod
    def debug(tag, content):
        print("ILog =====> " + tag + ":" + str(content))
