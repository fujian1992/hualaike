#-*-coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    context={}
    print 'hdksghjksd================dfsdfsdf'

    return render(request,'jindex/index.html',context)
def news(request,parms):
    print '============'
    # print parms
    context ={}
    return render(request,'news/'+parms,context)
def company(request):
    pass


def case(request,parms):
    """
    案例展示
    :param requset:
    :return:
    """
    context={}
    return render(request,'anli/'+parms,context)


def about(request,parms):
    """
    关于我们
    :param requset:
    :return:
    """
    context={}
    return render(request,'about/'+parms,context)


def job(request,parms):
    """
    人才招聘
    :param requset:
    :return:
    """
    context={}
    return render(request,'job/'+parms,context)

def connection(request,parms):
    """
    联系我们
    :param requset:
    :return:
    """
    context={}
    return render(request,'lianxi/'+parms,context)

def product(request,parms):
    """
    产品
    :param requset:
    :return:
    """
    context={}
    return render(request,'chanpin/'+parms,context)