#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/3/19 4:45 下午
# @Author : weiyizheng
# @File : BaseModel.py
# @desc :
import pymysql
from django.conf import settings


class BaseModel(object):
    table_name = ''

    def __init__(self):
        db_config = settings.DATABASES.get('default')
        self.db = pymysql.connect(
            host=db_config.get('HOST'),
            user=db_config.get('USER'),
            passwd=db_config.get('PASSWORD'),
            database=db_config.get('NAME'))

    def get_all(self):
        data_dict = []
        cursor = self.db.cursor(cursor=pymysql.cursors.DictCursor)
        if self.table_name:
            cursor.execute("select * from " + self.table_name + " where 1=1 and id < 10")
            data_dict = cursor.fetchall()
            # print(data_dict)
        else:
            return []
        return data_dict

    def __del__(self):
        self.db.close()
