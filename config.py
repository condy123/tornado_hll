# -*- coding:utf-8 -*-
import os
import time
mysql_option = dict(
        host='127.0.0.1', port=3306,
        user='root',
        pwd='',
        db='hll',
        charset='utf8',
        max_idle_connections=10,
        max_open_connections=100,
        max_recycle_sec=3
)

# Redis配置参数
redis_options = dict(
    host="127.0.0.1",
    port=6379
)

# 日志配置
log_path = os.path.join(os.path.dirname(__file__), "logs/"+time.strftime("%Y-%m-%d", time.localtime()) +"-log.txt")
log_level = "debug"


"""
配置相关信息
"""
settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "template_path": os.path.join(os.path.dirname(__file__), "templates"),
}