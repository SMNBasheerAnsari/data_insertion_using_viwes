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


def display_topic(request):
    tpo=Topic.objects.all()
    d={'topics':tpo}
    return render(request,'display_topic.html',d)

def display_webpage(request):
    wpo=Webpage.objects.all()
    d1={'webpage':wpo}
    return render(request,'display_webpages.html',d1)

def display_accessrecord(request):
    aro=AccessRecord.objects.all()
    d2={'accessrecord':aro}
    return render(request,'display_accessrecord.html',d2)

def display_db(request):
    tpo=Topic.objects.all()
    wpo=Webpage.objects.all()
    aro=AccessRecord.objects.all()

    #tpo=Topic.objects.filter(topic_name='cricket')
    #wpo=Webpage.objects.filter(topic_name='cricket')
    #aro=AccessRecord.objects.filter(auther='ba')

    #wpo=Webpage.objects.get(name='ABC') #for gives error

    #tpo=Topic.objects.exclude(topic_name='cricket')
    #wpo=Webpage.objects.exclude(topic_name='cricket')
    #aro=AccessRecord.objects.exclude(auther='ba')

    d={'to':tpo,'wo':wpo,'ao':aro}
    return render(request,'display_db.html',d)

#slicing orderby rownum len() startwith() endwith() to_char() to_date() like operater
def display_topic2(request):
    tn=input('enter topic_name:')
    to=Topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    tpo=Topic.objects.all()
    d={'topics':tpo}

    return render(request,'display_topic.html',d)

def update_db1(request):
    #Webpage.objects.filter(name='dhoni').update(url='https://msd.in') --single row
    #Webpage.objects.filter(topic_name='cricket').update(url='https://bcciCricket.in')  --multiple row
    #Webpage.objects.filter(topic_name='dds').update(url='https://bcciCricket.in')  --zero rows selected
    #Webpage.objects.filter(name='ronaldo').update(topic_name='cricket')--fk change True
    #Webpage.objects.filter(name='rohit').update(topic_name='falks')--fk change False gives error

    tpo=Topic.objects.all()
    wpo=Webpage.objects.all()
    aro=AccessRecord.objects.all()

    d={'to':tpo,'wo':wpo,'ao':aro}
    return render(request,'display_db.html',d)

def update_db2(request):
    #Webpage.objects.update_or_create(name='dhoni',defaults={'url':'https://abcd.com'}) #--single row
    #Webpage.objects.update_or_create(topic_name='cricket',defaults={'url':'https://bcciCricket.in'})  #--multiple row gives error
   
    cto=Topic.objects.get(topic_name='cricket')
    #Webpage.objects.update_or_create(name='dhoni',defaults={'topic_name':cto})#--fk change True
    #Webpage.objects.update_or_create(name='dhoni',defaults={'topic_name':cto,'name':'MSD','url':'https://mds.in'})
    Webpage.objects.update_or_create(name='qwer',defaults={'url':'https://bcciCricket.in','topic_name':cto,}) # --zero rows selected

    tpo=Topic.objects.all()
    wpo=Webpage.objects.all()
    aro=AccessRecord.objects.all()

    d={'to':tpo,'wo':wpo,'ao':aro}
    return render(request,'display_db.html',d)

def delete_db(request):

    #Webpage.objects.filter(name='qwer').delete()
    AccessRecord.objects.all().delete()

    tpo=Topic.objects.all()
    wpo=Webpage.objects.all()
    aro=AccessRecord.objects.all()

    d=d={'to':tpo,'wo':wpo,'ao':aro}
    return render(request,'display_db.html',d)