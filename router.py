# -*- coding:utf-8 -*-
from handlers.MainHandler import MainHandler,GetInfoHandler

"""
路由相关
"""
url = [
    (r'/mysql_test', GetInfoHandler),
    (r'/', MainHandler)
]

