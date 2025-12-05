# db/mysql_client.py
# 导入 MySQL 连接库
import pymysql
# 导入pandas
import pandas as pd
# 导入配置和日志
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../'))
# 导入配置和日志
from base.config import Config
from base.logger import logger


class MySQLClient:
    def __init__(self):
        # 初始化日志
        self.logger = logger
        try:
            # 连接 MySQL 数据库
            self.connection = pymysql.connect(
                host=Config().MYSQL_HOST,
                user=Config().MYSQL_USER,
                password=Config().MYSQL_PASSWORD,
                database=Config().MYSQL_DATABASE
            )
            # 创建游标
            self.cursor = self.connection.cursor()
            # 记录连接成功
            self.logger.info("MySQL 连接成功")
        except pymysql.MySQLError as e:
            # 记录连接失败
            self.logger.error(f"MySQL 连接失败: {e}")
            raise


# todo  没看