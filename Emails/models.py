from django.db import models

# Create your models here.


class Email(models.Model):
    recipients = models.TextField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    