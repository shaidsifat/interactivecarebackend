from django import views
from django.urls import include, path

from Emails.views import  SendEmal
 



urlpatterns = [
    path('send_email/',SendEmal.as_view(),name='send_email'),
]