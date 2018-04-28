

from common.dbutils import MySQLDBUtils, MongodbUtils
import redis

import config

# 项目中各个pool只需要实例化一次
class MysqlConnect():
    mysql_conn_app_dict = config.mysql_option
    mysql_pool = None
    def __init__(self):
        if self.mysql_pool:
            pass
        else:
            self.mysql_pool = MySQLDBUtils(self.mysql_conn_app_dict)

# 项目中各个pool只需要实例化一次
class MongoConnect():

    mongo_pool = None
    def __init__(self):
        self.mongo_pool = MongodbUtils(dict(mongo_auth_url='mongodb://127.0.0.1/log'))


# 默认普通链接 其他使用链接池方式链接
class RedisConnetc(object):
    redis = None
    def __init__(self, connet_type = 1):
        if connet_type == 1 :
            self.redis = redis.Redis(config.redis_options['host'], config.redis_options['port'])
        else:
            pool = redis.ConnectionPool(config.redis_options['host'], config.redis_options['port'])
            self.redis = redis.Redis(connection_pool=pool)
