import sys
from loguru import logger

# 去除默认日志处理器
logger.remove()

# 创建一个自定义的日志处理器
logger.add(sys.stderr,format="{time:YYYY-MM-DD HH:mm:ss}--{level.name}--{message}")

# 输出一条日志记录
logger.info("这是一条日志信息")