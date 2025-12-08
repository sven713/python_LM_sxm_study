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
            print('pp----',Config().MYSQL_PASSWORD)
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



    def fetch_questions(self):
            # 获取所有问题
            try:
                # 执行查询
                self.cursor.execute("SELECT question FROM jpkb")
                # 获取结果
                results = self.cursor.fetchall()
                # 记录获取成功
                self.logger.info("成功获取问题")
                # 返回结果
                return results
            except pymysql.MySQLError as e:
                # 记录查询失败
                self.logger.error(f"查询失败: {e}")
                # 返回空列表
                return []

# todo  没看

    def close(self):
            # 关闭数据库连接
            try:
                # 关闭连接
                self.connection.close()
                # 记录关闭成功
                self.logger.info("MySQL 连接已关闭")
            except pymysql.MySQLError as e:
                # 记录关闭失败
                self.logger.error(f"关闭连接失败: {e}")