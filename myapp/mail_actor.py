import pykka
from django.core.mail import EmailMessage


# class MailerActor(pykka.ThreadingActor):
#     def __init__(self, greeting='Testing!'):
#         super(MailerActor, self).__init__()
#         self.greeting = greeting
#
#     def on_receive(self, msg):
#         # print(self.greeting)
#         print(msg)


def send_mail(subject, body, to_mail, cc_mail, bcc_mail):
    email = EmailMessage(subject, body, "test@test.com", to_mail, bcc_mail, None, None, None, cc_mail, None)
    email.content_subtype = "html"
    res = email.send()
    print("Email Res: " + str(res))






