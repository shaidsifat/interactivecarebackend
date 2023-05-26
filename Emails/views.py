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
        query = Email.objects.all().values('id','recipients','subject','message')
        if query:
          return Response({"message":query}, status=status.HTTP_200_OK)
        return Response({"message":"data not found"})




    def post(self, request, format=None):
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




