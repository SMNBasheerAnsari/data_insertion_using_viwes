from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.

def insert_topic(request):
    tn=input('enter topic_name:')
    to=Topic.objects.get_or_create(topic_name=tn)[0]
    to.save()

    return HttpResponse('topic is created')

def insert_webpage(request):
    tn=input('enter topic_name:')
    to=Topic.objects.get_or_create(topic_name=tn)[0]
    to.save()

    n=input('enter player name:')
    u=input('enter url:')
    wo=Webpage.objects.get_or_create(topic_name=to,name=n,url=u)[0]
    wo.save()

    return HttpResponse('webpage is created')

def insert_access_record(request):
    tn=input('enter topic_name:')
    to=Topic.objects.get_or_create(topic_name=tn)[0]
    to.save()

    n=input('enter player name:')
    u=input('enter url:')
    wo=Webpage.objects.get_or_create(topic_name=to,name=n,url=u)[0]
    wo.save()

    d=input('enter date like yyyy-mm-dd:')
    a=input('enter author name:')
    aro=AccessRecord.objects.get_or_create(name=wo,date=d,auther=a)[0]
    aro.save()

    return HttpResponse('access record is created')


    