#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/3/16 5:36 下午
# @Author : weiyizheng
# @File : urls.py
# @desc :
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('api/hello', views.hello),
    path('api/list', views.list),
    path('api/list2', views.list2)
]