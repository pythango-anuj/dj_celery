import json

from django.shortcuts import render
from django.http import HttpResponse
from .tasks import send_the_mails
from django_celery_beat.models import PeriodicTask, CrontabSchedule

# Create your views here.
def sending_mails(request):
    send_the_mails.delay()
    return HttpResponse("..........All Emails SENT!..........")

def schedule_mail(request):
    schedule, created = CrontabSchedule.objects.get_or_create(hour=22, minute=5)
    i = 3
    task = PeriodicTask.objects.create(crontab=schedule, name='scheduling_the_mails'+str(i), task='send_email.tasks.send_the_mails')#, args=json.dumps({"By":"Anuj Pandey"}))
    return HttpResponse("..........Mail Scheduled!...........")
