# redis: 缓存
import json
import redis
import sys
import os
# 添加 integrated_qa_system 目录到 Python 路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../'))
from base.config import Config
from base.logger import logger


class RedisClient:
    def __init__(self):
      print(22222)
      self.logger = logger

      try:
        self.client = redis.StrictRedis(
            host=Config().REDIS_HOST,
            port=Config().REDIS_PORT,
            password=Config().REDIS_PASSWORD,
            db=Config().REDIS_DB,
            decode_responses=True
        )
        self.logger.info("Redis 连接成功")
      except redis.RedisError as e:
        self.logger.error(f"Redis 连接失败: {e}")
        raise


    def set_data(self, key, value):
        try:
            self.client.set(key, json.dumps(value))
            self.logger.info(f"存储数据到 Redis: {key}")
        except redis.RedisError as e:
            self.logger.error(f"Redis 存储失败: {e}")

    def get_data(self, key):
        try:
            data = self.client.get(key)
            return json.loads(data) if data else None
        except redis.RedisError as e:
            self.logger.error(f"Redis 获取失败: {e}")
            return None
    
    def get_answer(self, query):
        try:
            answer = self.client.get(f"answer:{query}")
            if answer:
                self.logger.info(f"从 Redis 获取答案: {query}")
                return answer
            return None
        except redis.RedisError as e:
            self.logger.error(f"Redis 查询失败: {e}")
            return None