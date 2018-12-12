#-*-coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    context={}
    print 'hdksghjksd================dfsdfsdf'

    return render(request,'jindex/index.html',context)
def news(request):
    print '============'
    # print parms
    context ={}
    return render(request,'news/2014/0304/11.html',context)
