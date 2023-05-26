from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

# Models
from .models import Email
from Emails.utils import send_bulk_email
@receiver(post_save, sender=Email)
def send_request_email(sender, instance, created, **kwargs):
    if created:
        try:
            print(instance.id)
            from_email = settings.DEFAULT_FROM_EMAIL
            #recipient_list = ['shaidsifat55@gmail.com','sifat15-7616@diu.edu.bd',] # Replace this with the email address where you want to receive the notification
            email = Email.objects.get(id=instance.id).recipients
            
            
            recipient = email
           # print(recipient_list.recipients)
           # print(type(recipient_list))
            data = recipient.split(',') 
            recipient_list = data
            

            subject = instance.subject
            message = instance.message
           

            res=send_bulk_email(subject, message, from_email,recipient_list)
            print(res)
            if(res == 1):  
                msg = "Mail Sent Successfuly"  
            else:  
                msg = "Mail could not sent" 
            print(msg) 
        except Exception as e:
            print(e)
