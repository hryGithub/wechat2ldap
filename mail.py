# !/usr/bin/python
# -*- coding: utf-8 -*-

import smtplib
from settings import *
from email.mime.text import MIMEText
from email.header import Header


class Email:
    def __init__(self):
        self.sender = SMTP_USER
        self.mail_url = SMTP_HOST
        self.mail_port = SMTP_PORT
        self.sender_username = SMTP_USER
        self.sender_password = SMTP_PASSWD

    def send_mail(self, email, username, sn):
        receiver = [email]
        mail_msg = MESSAGE
        message = MIMEText(mail_msg % (username, username), 'html', 'utf-8')
        message['From'] = Header('系统机器人', 'utf-8')
        message['To'] = Header('%s' % sn, 'utf-8')
        subject = 'LDAP 账号信息'
        message['Subject'] = Header(subject, 'utf-8')
        try:
            smtpobj = smtplib.SMTP_SSL(self.mail_url, self.mail_port)
            smtpobj.login(self.sender_username, self.sender_password)
            smtpobj.sendmail(self.sender, receiver, message.as_string())
            smtpobj.quit()
            print('发送邮件成功')
        except smtplib.SMTPException as e:
            print('发送邮件失败', e)


if __name__ == "__main__":
    mail = Email()
    mail.send_mail('hujian@innowealth.com.cn', 'hujian', '张三')

