#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/3/18 2:21 下午
# @Author : weiyizheng
# @File : urls.py
# @desc :
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('blog/index', views.IndexView.as_view()),
    path('blog/cbv', views.CBV.as_view())
]