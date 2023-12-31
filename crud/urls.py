"""
URL configuration for crud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('insert_topic/',insert_topic,name='insert_topic'),
    path('insert_webpage/',insert_webpage,name='insert_webpage'),
    path('insert_access_record/',insert_access_record,name='insert_access_record'),
    path('display_topic/',display_topic,name='display_topic'),
    path('display_webpage/',display_webpage,name='display_webpage'),
    path('display_accessrecord/',display_accessrecord,name='display_accessrecord'),
    path('display_db/',display_db,name='display_db'),

    path('display_topic2/',display_topic2,name='display_topic2'),
    path('update_db1/',update_db1,name='update_db1'),
    path('update_db2/',update_db2,name='update_db2'),
    path('delete_db/',delete_db,name='delete_db'),
]
