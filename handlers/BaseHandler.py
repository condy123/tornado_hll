# coding:utf-8

import json
from tornado.web import RequestHandler, StaticFileHandler


class BaseHandler(RequestHandler):
    """自定义基类"""
    @property
    def mysql(self):
        """作为RequestHandler对象的db属性"""
        print(self.application.mysql)
        return self.application.mysql

    @property
    def redis(self):
        """作为RequestHandler对象的redis属性"""
        return self.application.redis

    def prepare(self):
        """预解析json数据"""
        if self.request.headers.get("Content-Type", "").startswith("application/json"):
            self.json_args = json.loads(self.request.body)
        else:
            self.json_args = {}

    def set_default_headers(self):
        """设置默认json格式"""
        self.set_header("Content-Type", "application/json; charset=UTF-8")

























