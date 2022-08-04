# coding: utf-8

import email.message
import smtplib

from app.framework.utility.log_utility import ILog


class EmailSender:

    __TAG = "EmailSender"

    def __init__(self, uuid, email_id, email_pw, smtp_server_protocol, smtp_server_port):

        self.__send_uuid = uuid

        self.__smtp_server_protocol = smtp_server_protocol
        self.__smtp_server_port = smtp_server_port

        self.__email_id = email_id
        self.__email_pw = email_pw

        self.__smtp_server = None
        self.__msg = None

    def connect(self):
        ILog.debug(EmailSender.__TAG, f'연결성공')
        result = ""
        try:
            self.__smtp_server = smtplib.SMTP_SSL(self.__smtp_server_protocol, self.__smtp_server_port)
            result = self.__smtp_server.login(self.__email_id, self.__email_pw)
        except Exception as e:
            ILog.debug(EmailSender.__TAG, '열결실패')
            self.__smtp_server.close()
            raise Exception from e
        finally:
            ILog.debug(EmailSender.__TAG, f'열결성공 {result}')

    def send(self, from_people, to_people, title, content):

        try:
            self.__msg = email.message.EmailMessage()

            self.__msg["From"] = from_people
            self.__msg["To"] = to_people
            self.__msg["Subject"] = title
            self.__msg.set_content(content)

            self.__smtp_server.send_message(self.__msg)
        except Exception as e:
            ILog.debug(EmailSender.__TAG, f"발신 이메일: {self.__msg['From']}  --->  목표 이메일: {self.__msg['To']} 발송 실패 {e}")
            return False

        ILog.debug(EmailSender.__TAG, f"발신 이메일: {self.__msg['From']}  --->  목표 이메일: {self.__msg['To']} 발송 성공")
        return True

    def close(self):
        self.__smtp_server.close()
