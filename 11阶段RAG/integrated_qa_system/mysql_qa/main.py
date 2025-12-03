from cache.redis_client import RedisClient



class MySQLQASystem:
    def __init__(self):
      print(11111)
      # 初始化 MySQL 客户端
      # self.mysql_client = MySQLClient()
      # 初始化 Redis 客户端
      self.redis_client = RedisClient()
      # 初始化 BM25 搜索
      # self.bm25_search = BM25Search(self.redis_client, self.mysql_client)



def main():
  mysql_system = MySQLQASystem()
  print('???')

if __name__ == "__main__":
    # 运行主程序
    main()