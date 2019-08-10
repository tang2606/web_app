# encoding: utf-8  
"""
    @version:
    @Topic 
    @Author: weidong.tang
    @Company:
    @Contact:
    @software: PyCharm
    @file: home.py
    @time: 2019-08-10 11:54

"""
# from django.http import HttpResponse
from django.shortcuts import render

def home(request):

    return render(request,'hello.html')


def count(request):
    print('request is : ',request)
    name = request.GET.get('name')
    mail = request.GET.get('mail')

    print(name,mail)

    return render(request,'count.html',{'name': name, 'mail': mail})
