# email_utils.py

from django.core.mail import send_mail
from ratelimit import limits

@limits(calls=100, period=1000)
def send_bulk_email(subject, message, from_email, recipient_list):
   # print("message")ata 
   # t=recipient_list
   # data = [*t,]
  #  print(data)
    ####=['sifat15-7616@gmail.com']
    
    d=send_mail(subject, message, from_email=from_email, recipient_list= recipient_list)
    print(d)
    return d 