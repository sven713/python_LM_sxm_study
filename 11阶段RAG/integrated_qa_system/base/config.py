# ToDo: 下面没仔细看
# base/config.py
# 导入配置解析库
import configparser
# 导入路径操作库
import os


class Config:
    # 初始化配置，加载 config.ini 文件
    def __init__(self, config_file='../config.ini'):
        # 创建配置解析器
        self.config = configparser.ConfigParser()
        # 读取配置文件
        self.config.read(config_file)

        # MySQL 配置
        # MySQL 主机地址
        self.MYSQL_HOST = self.config.get('mysql', 'host', fallback='localhost') 
        # MySQL 用户名
        self.MYSQL_USER = self.config.get('mysql', 'user', fallback='root')
        # MySQL 密码
        self.MYSQL_PASSWORD = self.config.get('mysql', 'password', fallback='abcd@123') 
        # MySQL 数据库名
        self.MYSQL_DATABASE = self.config.get('mysql', 'database', fallback='subjects_kg')  

        # Redis 配置
        # Redis 主机地址
        self.REDIS_HOST = self.config.get('redis', 'host', fallback='localhost') 
        # Redis 端口
        self.REDIS_PORT = self.config.getint('redis', 'port', fallback=6379)  
        # Redis 密码
        self.REDIS_PASSWORD = self.config.get('redis', 'password', fallback=None) 
        # Redis 数据库编号
        self.REDIS_DB = self.config.getint('redis', 'db', fallback=0)  
        # 日志文件路径
        self.LOG_FILE = self.config.get('logger', 'log_file', fallback='logs/app.log')  



        # 检索参数
        # 父块大小
        self.PARENT_CHUNK_SIZE = self.config.getint('retrieval', 'parent_chunk_size', fallback=1200)
        # 子块大小
        self.CHILD_CHUNK_SIZE = self.config.getint('retrieval', 'child_chunk_size', fallback=300)
        # 块重叠大小
        self.CHUNK_OVERLAP = self.config.getint('retrieval', 'chunk_overlap', fallback=50)

if __name__ == '__main__':
    conf = Config()
    print(conf.CHILD_CHUNK_SIZE)
