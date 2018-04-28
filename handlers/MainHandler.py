from tornado.web import RequestHandler
from tornado import gen
from common.conn import MysqlConnect,RedisConnetc
from handlers.BaseHandler import BaseHandler

class MainHandler(BaseHandler):
    @gen.coroutine
    def get(self):
        dbs = self.mysql
        search_sql = (
            "SELECT * FROM person where id = 1"
        )
        news_info = yield dbs.get_one(search_sql)
        info_dict = dict()
        if news_info:
            info_dict['title'] = news_info[0]
            info_dict['pubtime'] = news_info[1]
        self.write(info_dict)

class LoginHandler(RequestHandler):
    def get(self):
        self.render('login.html')


class GetInfoHandler(RequestHandler):
    """
    Mysql demo
    """
    @gen.coroutine
    def get(self):
        conn = MysqlConnect()
        search_sql = (
            "SELECT * FROM person where id = 1"
        )
        news_info = yield conn.mysql_pool.get_one(search_sql)
        print(news_info)
        info_dict = dict()
        if news_info:
            info_dict['title'] = news_info[0]
            info_dict['pubtime'] = news_info[1]
        self.write(info_dict)


# class ZanHandler(RequestHandler):
#     """
#     mongo demo
#     """
#     @gen.coroutine
#     def get(self):
#         db_zan_collection = mongo_pool.get_collection('db',
#                                                       'collection')
#         yield db_zan_collection.insert({'key': 'value'})
#         self.write({"code": "0", "msg": u"ok"})