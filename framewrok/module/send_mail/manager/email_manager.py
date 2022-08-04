# coding: utf-8

import time

from framewrok.module.send_mail.manager.sender.email_sender import EmailSender
from framewrok.utility.log_utility import ILog
from framewrok.utility.uuid_utility import UUIDUtility


class EmailManager:
    __TAG = "EmailManager"

    __SMTP_SERVER = "smtp.daum.net"
    # __SMTP_SERVER = "smtp.google.com"
    __SMTP_SERVER_PORT = 465

    __ID = "xxxx"
    __PW = "xxxxx"

    __FROM = "xxxx <xxxxx@xxxx.xxx>"

    _instance = None

    def __new__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self):
        self.__target_list = []
        self.__email_sender = None

    def set_target(self, target_list):
        self.__target_list.clear()
        self.__target_list = self.__target_list + target_list
        ILog.debug(EmailManager.__TAG, len(self.__target_list))

    def create_sender(self):
        ILog.debug(EmailManager.__TAG, "이메일 발송 준비")
        self.__email_sender = EmailSender(UUIDUtility.get_uuid(), EmailManager.__ID, EmailManager.__PW,
                                          EmailManager.__SMTP_SERVER, EmailManager.__SMTP_SERVER_PORT)
        self.__email_sender.connect()

    def start(self):

        for target in self.__target_list:

            time.sleep(8)
            result = self.__email_sender.send(EmailManager.__FROM, target, "자동 메일 발송 마지막 테스트",
                                              "분당 8 ~ 10개, 1시간 480 ~ 600개 예정입니다.")
            if not result:
                self.__email_sender.connect()
                time.sleep(3)
                self.__email_sender.send(EmailManager.__FROM, target, "자동 메일 발송 마지막 테스트",
                                         "분당 8 ~ 10개, 1시간 480 ~ 600개 예정입니다.")
        self.close()

    def close(self):

        self.__email_sender.close()
        ILog.debug(EmailManager.__TAG, f'이메일 발송 완셩하였습니다.')


if __name__ == '__main__':
    pass
    email_manager = EmailManager()

    email_manager.set_target(["shtest@test.com", "shtest1@test.com"])
    email_manager.create_sender()
    email_manager.start()
