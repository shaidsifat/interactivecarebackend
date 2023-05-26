from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Email
from .serializers import EmailSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404, HttpResponse
from Emails.utils import send_bulk_email
from django.core.mail import send_mail  
from django.conf import settings 

class SendEmal(APIView):


    def get(self,request,format=None):

    
        # snippets = Email.objects.all()
        #  serializer =EmailSerializer(snippets, many=True)
            subject = 'New message send'
            message = f'A new meesage for interactivecare.'
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = ['shaidsifat55@gmail.com','sifat15-7616@diu.edu.bd',] # Replace this with the email address where you want to receive the notification
            
            res=send_bulk_email(subject, message, from_email, recipient_list)
           # print(res)
            if(res == 1):  
                msg = "Mail Sent Successfuly"  
            else:  
                msg = "Mail could not sent"  
            return HttpResponse(msg)  
                




    def post(self, request, format=None):
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():

            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# views.py



def send_bulk_emails_view(request):
    recipients = ['email1@example.com', 'email2@example.com', 'email3@example.com']
    subject = 'Hello'
    message = 'This is a bulk email message.'

    send_bulk_email(recipients, subject, message)

    return render(request, 'email_sent.html')
