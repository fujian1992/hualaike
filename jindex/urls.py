#-*-coding:utf-8 -*-
from django.conf.urls import include, url
import views
urlpatterns = [
    url(r'^', views.index),
    url(r'^news$', views.news),

]
