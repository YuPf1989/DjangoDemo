# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, render_to_response


# Create your views here.
def sayHello(request):
    s = "hello world"
    current_time = datetime.datetime.now()
    # html ='<head>'
    # '< / head >'
    # '< body ><h1>%s</h1><p>%s</p>'
    # '< / body >'
    # '< / html >' %(s,current_time)
    html = '<html><head></head><body><h1> %s </h1><p> %s </p></body></html>' % (s, current_time)
    return HttpResponse(html)

def showStudents(request):
    students = [{'id':1,'name':'小明','age':20},{'id':2,'name':'小红','age':21},{'id':3,'name':'小强','age':23}]
    return render_to_response('web.html',{'students':students})