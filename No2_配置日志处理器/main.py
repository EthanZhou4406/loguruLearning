from loguru import logger

# 删除默认日志处理器
logger.remove()

# 自定义一个日志处理器
logger.add(sink="./logs/log.log",format="{time} | {level} | {message}")

# 测试效果
logger.info("这是一个信息日志")

logger.debug("这是一个调试日志")

logger.error("这是一个报错日志")