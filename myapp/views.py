from django.shortcuts import render
from django.http import HttpResponse
from .tasks import test_fuct
# Create your views here.

def test(request):
    test_fuct.delay()
    return HttpResponse("Task Completed")

