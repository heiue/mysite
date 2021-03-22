#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/3/16 3:56 下午
# @Author : weiyizheng
# @File : view.py
# @desc :
from django.http import HttpResponse, request
import json
from api.models import SaasScPoster
from api.basemodels.SaasPoster import SaasPoster
from django.conf import settings


def hello(request):
    data = {
        "msg": "首页"
    }
    return HttpResponse(json.dumps({"data": data}))


# Django自带的数据库操作
def list(request):
    data = {}
    lists = SaasScPoster.objects.filter(id__lt=10).values()
    # print(lists)
    return HttpResponse()


def list2(request):
    data = {}
    lists = SaasPoster().get_all()
    data['list'] = lists
    return HttpResponse(json.dumps(data))
