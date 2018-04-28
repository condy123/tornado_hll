# -*- coding:utf-8 -*-
from tornado.options import define, options
from tornado.ioloop import IOLoop
from tornado import web,httpserver
import tornado
import config
import router
from common import conn

#define("env", default='develop', help="", type=str)
define("port", default=8899, help="run on the given port", type=int)
APPLICATION_SETTINGS = dict(
    debug=True,
    app_setting=config.settings
    )
class Application(tornado.web.Application):
    def __init__(self, *args, **kwargs):
        super(Application, self).__init__(*args, **kwargs)
        self.mysql = conn.MysqlConnect().mysql_pool
        self.redis = conn.RedisConnetc().redis


options.parse_command_line()
app = Application(router.url, **APPLICATION_SETTINGS)

if __name__ == "__main__":
    options.log_file_prefix = config.log_path
    options.logging = config.log_level
    options.parse_command_line()
    #Application()
   # app.listen(options.port, xheaders=False)
    http_server = httpserver.HTTPServer(app)
    http_server.listen(options.port)
    IOLoop.current().start()

