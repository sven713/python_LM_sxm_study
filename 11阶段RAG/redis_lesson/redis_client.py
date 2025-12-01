# redis: 缓存
import redis
from base import  Config,logger


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