from email.mime.text import MIMEText
import smtplib

from .spamfilter.filter import SpamFilter


class MailMan:

    PORT = 465
    SERVER = 'smtp.gmail.com'
    DEFAULT_SUBJECT = '[* Website alert *]'
    CONNECTION = None

    @staticmethod
    def _create_message(body, to_, recipient, subject):
        msg = MIMEText(body)
        msg['Subject'] = (MailMan.DEFAULT_SUBJECT if subject is None
                          else subject)
        msg['From'] = to_
        msg['To'] = recipient
        return msg

    @staticmethod
    def is_spam(msg):
        spamfilter = SpamFilter()
        return spamfilter.hit(msg)

    @staticmethod
    def send_mail(username, password, recipient, body, subject=None):
        if MailMan.is_spam(body):
            return
        server_ssl = smtplib.SMTP_SSL(MailMan.SERVER, MailMan.PORT)
        server_ssl.login(username, password)
        msg = MailMan._create_message(body, username, recipient, subject)
        server_ssl.send_message(msg)
        server_ssl.close()

