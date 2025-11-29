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
# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(asctime)s - %(levelname)s - %(message)s'
# )

# # 获取日志记录器
# logger = logging.getLogger("Example2")

# # 记录日志
# logger.debug("调试模式已开启")
# logger.info("正在处理数据")
# logger.error("数据处理失败")

# ------------demo3--------------------

# todo  示例3：将日志存储到文件


# 配置日志，输出到文件
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='app.log',  # 日志文件路径
    filemode='a'         # 'a'表示追加，'w'表示覆盖
)

# 获取日志记录器
logger = logging.getLogger("Example3")

# 记录日志
logger.info("程序启动!!")
logger.warning("内存使用率较高")
logger.error("无法连接数据库")
