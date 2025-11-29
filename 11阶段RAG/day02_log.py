import logging

# 配置基本的日志设置
# logging.basicConfig(level=logging.INFO)

# 获取日志记录器
# logger = logging.getLogger()

# # 记录不同级别的日志
# logger.debug("这是调试信息，通常用于开发")
# logger.info("程序运行正常")
# logger.warning("注意，可能有小问题")
# logger.error("发生错误")
# logger.critical("严重错误，程序可能崩溃")


# ------------demo2--------------------

# 配置日志格式
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# 获取日志记录器
logger = logging.getLogger("Example2")

# 记录日志
logger.debug("调试模式已开启")
logger.info("正在处理数据")
logger.error("数据处理失败")
