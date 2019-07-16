from redis import *


class RedisUtils:
    """Redis使用工具类"""

    def __init__(self, host="localhost", port=6379, db=0):
        """
        初始化 \n
        :param host:
        :param port:
        :param db:
        """
        self.strictRedis = StrictRedis(host, port=port, db=db)

    def set_value(self, name, value):
        """
        设置或者修改单个key-value值 \n
        :param name:
        :param value:
        :return:
        """
        ret = self.strictRedis.set(name, value)
        # print(ret)
        return ret

    def del_value(self, *name):
        """
        根据name删除值 \n
        :param name: 所有的key
        :return:
        """
        return self.strictRedis.delete(*name)

    def get_value(self, name):
        """
        根据指定的key获取value \n
        :param name:
        :return:
        """
        return self.strictRedis.get(name)

    def set_value_much(self, name):
        """
        设置或修改多个值
        :param name:
        :return:
        """
        return self.strictRedis.mset(name)

    def get_value_much(self, *name):
        """
        查询多个key获取value \n
        :param name:
        :return:
        """
        return self.strictRedis.mget(name)

    def append_value(self, key, value):
        """
        给指定key的value后面添加指定值,如果key不存在就创建一个key和value \n
        :param key:
        :param value:
        :return:
        """
        self.strictRedis.append(key, value)
        return self.strictRedis.get(key)

    def setex_value(self, key, time, value):
        """
        修改或创建一个key和value并设置存在时间 \n
        :param key:
        :param time:
        :param value:
        :return:
        """
        return self.strictRedis.setex(key, time, value)

    def ttl_value(self, name):
        """
        查看指定的key还能活多久 \n
        :param name:
        :return:
        """
        ret = self.strictRedis.ttl(name)
        return ret

    def exists_value(self, key):
        """
        查看key值是否存在 \n
        :param key:
        :return:
        """
        return self.strictRedis.exists(key)

    def keys(self):
        """
        查看所有key \n
        :return:
        """
        ret = self.strictRedis.keys()
        return ret

    def hset_value(self, name, key, value):
        """
        在一个hash中添加或修改一对key,value值 \n
        :param name:
        :param key:
        :param value:
        :return:
        """
        return self.strictRedis.hset(name, key, value)

    def hmset_value(self, key, mapping):
        """
        在一个hash中添加或修改多个key,value值 \n
        :param key:
        :param mapping:
        :return:
        """
        return self.strictRedis.hmset(key, mapping)

    def hget_value(self, name, key):
        """
        在一个hash中查看一个key对应的value值 \n
        :param name:
        :param key:
        :return:
        """
        return self.strictRedis.hget(name, key)

    def hmget_value(self, key, *fieldName):
        """
        在一个hash中查看多个key对应的value值 \n
        :param key:
        :param fieldName:
        :return:
        """
        return self.strictRedis.hmget(key, *fieldName)

    def hkeys_value(self, key):
        """
        查看hash中所有key的值 \n
        :param key:
        :return:
        """
        return self.strictRedis.hkeys(key)

    def hvals_value(self, key):
        """
        查看hash中所有value的值 \n
        :param key:
        :return:
        """
        return self.strictRedis.hvals(key)

    def hdel_value(self, name, *key):
        """
        删除hash中对应的key和value \n
        :param name:
        :param key:
        :return:
        """
        return self.strictRedis.hdel(name, *key)

    def lpush_value(self, name, *value):
        """
        从左侧添加值进入list \n
        :param name:
        :param value:
        :return:
        """
        return self.strictRedis.lpush(name, *value)

    def rpush_value(self, name, *value):
        """
        从右侧添加值进入list \n
        :param name:
        :param value:
        :return:
        """
        return self.strictRedis.rpush(name, *value)

    def linsert_value(self, name, where, now, new):
        """
        在list中指定元素前后添加元素 \n
        :param name:
        :param where: before | after
        :param now:
        :param new:
        :return:
        """
        return self.strictRedis.linsert(name, where, now, new)

    def lrange_value(self, name, start=0, end=-1):
        """
        查看list中从左到右指定起始到结束位置上的所有值 \n
        :param name:
        :return:
        """
        return self.strictRedis.lrange(name, start, end)

    def lset_value(self, name, index, value):
        """
        修改指定索引位置上的值 \n
        :param name:
        :param index:
        :param value:
        :return:
        """
        return self.strictRedis.lset(name, index, value)

    def lrem_value(self, name, value, count=0):
        """
        删除list中包含指定个数的值 \n
        :param name:
        :param value:
        :param count:
        :return:
        """
        return self.strictRedis.lrem(name, count, value)

    def sadd_value(self, name, *value):
        """
        在set中添加值 \n
        :param name:
        :param value:
        :return:
        """
        return self.strictRedis.sadd(name, *value)

    def smembers_value(self, name):
        """
        查询set中的所有值 \n
        :param name:
        :return:
        """
        return self.strictRedis.smembers(name)

    def srem_value(self, name, *value):
        """
        删除set中指定的值 \n
        :param name:
        :param value:
        :return:
        """
        return self.strictRedis.srem(name, *value)

    def zadd_value(self, name, mapping):
        """
        在zset中添加带有权重的值 \n
        :param name:键
        :param mapping:  {value:score,....value:score}
        :return:
        """
        return self.strictRedis.zadd(name, mapping)

    def zrange_value(self, name, start=0, end=-1):
        """
        查看zset中指定开始索引到结束索引的所有值 \n
        :param name:
        :param start:
        :param end:
        :return:
        """
        return self.strictRedis.zrange(name, start, end)

    def zrangebyscore_value(self, name, min, max):
        """
        查看zset中权重在一定范围中的所有值 \n
        :param name:
        :param min:
        :param max:
        :return:
        """
        return self.strictRedis.zrangebyscore(name, min, max)

    def zscore_value(self, name, value):
        """
        查看zset中指定元素的权重值 \n
        :param name:
        :param value:
        :return:
        """
        return self.strictRedis.zscore(name, value)

    def zrem_value(self, name, *value):
        """
        删除zset中指定元素 \n
        :param name:
        :param value:
        :return:
        """
        return self.strictRedis.zrem(name, *value)

    def type_value(self, name):
        """
        查看name下的元素的数据类型 \n
        :param name:
        :return:
        """
        return self.strictRedis.type(name)


if __name__ == '__main__':
    r = RedisUtils()

# redisUitls = RedisUtils()
# print(redisUitls.keys())
# print(type((b'body/+.jpg').decode("utf-8")))

# print(redisUitls.lrange_value("2_美女", 0, -1))
# a = "[<PhotoGraph: PhotoGraph object (1)>, <PhotoGraph: PhotoGraph object (2)>]"
# print(eval(a))
