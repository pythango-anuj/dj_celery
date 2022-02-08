from django.urls import path
from . import  views
urlpatterns = [
    path('send_mail/', views.sending_mails, name='Sending_Email'),
    path('schedule_mail/', views.schedule_mail, name='Scheduling Mail')
]