#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/3/16 3:56 下午
# @Author : weiyizheng
# @File : view.py
# @desc :
from django.http import HttpResponse, request
import json
from api.models import SaasScPoster, ChUser
from api.basemodels.SaasPoster import SaasPoster
from django.conf import settings
from django.db.models import Count


def hello(request):
    data = {
        "msg": "首页"
    }
    return HttpResponse(json.dumps({"data": data}))


# Django自带的数据库操作
def list(request):
    # ch_user 新增一条
    # user = ChUser(name='weiyizheng', phone='13521282025')
    # user.save()
    # user = ChUser.objects.create(name='heiue', phone='13521282025')
    # print(user.id)

    """ 修改 """
    # user = ChUser.objects.get(id=1)
    # user.name = 'wyz'
    # user.save()

    # id = ChUser.objects.filter(id=1).update(name='wyzheng')
    # print(id)

    """ 删除 """
    # user = ChUser.objects.get(id=1)
    # user.delete()

    ChUser.objects.filter(id=2).delete()

    """ 获取一条 """
    one = ChUser.objects.get(id=3)
    print(one.name)

    """ 过滤 """
    data = {}
    lists = ChUser.objects.order_by("-id").exclude(id__gt=5).values()
    # lists = ChUser.objects.order_by("-id").filter(id__lt=10).values()
    data = []
    for item in lists:
        data.append(item)
    # print(lists)

    """ 聚合 """
    count = ChUser.objects.aggregate(Count('id'))
    print(count)
    return HttpResponse(json.dumps(data))


def list2(request):
    data = {}
    lists = SaasPoster().get_all()
    data['list'] = lists
    return HttpResponse(json.dumps(data))
