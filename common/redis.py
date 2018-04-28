import tornadoredis

import tornadoredis
c = tornadoredis.Client(host="127.0.0.1",port=6379)
# 测试是否连接成功，写一个key，并查看redis数据库是否存在该key
c.set("name","zhangsan")