import logging
from redis_client import RedisClient
# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def hhmain():
  print(11112)
  redis_client = RedisClient()
  # 示例数据
  key = "user:1"
  value = {"name": "Alice", "age": 25}
  # 存储数据
  redis_client.set_data(key, value)
  # 获取数据
  result = redis_client.get_data(key)
  print('!!!',result)


if __name__ == "__main__":
    hhmain()