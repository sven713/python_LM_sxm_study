import logging
from redis_client import RedisClient
# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def hhmain():
  print(11112)
  redis = RedisClient()
    # 初始化 Redis 客户端


if __name__ == "__main__":
    hhmain()