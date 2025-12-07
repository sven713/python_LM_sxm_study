from cache.redis_client import RedisClient
from retrieval.bm25_search import BM25Search
from db.mysql_client import MySQLClient
from base.logger import logger

class MySQLQASystem:
    def __init__(self):
        print(11111)
        # 初始化 MySQL 客户端
        self.mysql_client = MySQLClient()
        # 初始化 Redis 客户端
        self.redis_client = RedisClient()
        # 初始化 BM25 搜索
        self.bm25_search = BM25Search(self.redis_client, self.mysql_client)


def main():
    mysql_system = MySQLQASystem()
    print("???")
    try:
        # 打印欢迎信息
        print("\n欢迎使用 MySQL 问答系统！")
        print("输入查询进行问答，输入 'exit' 退出。")
        while True:
            # 获取用户输入
            query = input("\n输入查询: ").strip()
            if query.lower() == "exit":
                # 记录退出日志
                logger.info("退出 MySQL 系统")
                # 打印退出信息
                print("再见！")
                break
            # 执行查询
            answer = mysql_system.query(query)
            # 打印答案
            print(f"\n答案: {answer}")
    except Exception as e:
        # 记录系统错误
        logger.error(f"系统错误: {e}")
        # 打印错误信息
        print(f"发生错误: {e}")
    finally:
        # 关闭 MySQL 连接
        mysql_system.mysql_client.close()


if __name__ == "__main__":
    # 运行主程序
    main()
