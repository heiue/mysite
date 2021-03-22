#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/3/19 4:45 下午
# @Author : weiyizheng
# @File : SaasPoster.py
# @desc :
from api.basemodels.BaseModel import BaseModel


class SaasPoster(BaseModel):
    table_name = 'saas_sc_poster'

    def __init__(self):
        BaseModel.__init__(self)