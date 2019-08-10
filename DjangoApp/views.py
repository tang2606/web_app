# encoding: utf-8  
"""
    @version:
    @Topic 
    @Author: weidong.tang
    @Company: 小赢科技 <X-Financial> 
    @Contact: weidong.tang@xiaoying.com
    @software: PyCharm
    @file: views.py
    @time: 2019-08-10 15:40

"""

from django.shortcuts import render
from django.http import HttpResponse
from homepage.models import Homepage

def home(request):
    hemo_page = Homepage.objects

    return render(request, 'home.html',{'hp': hemo_page})

