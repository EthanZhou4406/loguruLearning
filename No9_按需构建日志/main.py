import sys
import time
from datetime import datetime
from loguru import logger

logger.remove()

# 利用serialize参数将日志信息，以JSON格式输出
logger.add(sys.stderr,serialize=True)
# logger.info("这是一个日志信息")

logger.remove()

# 利用{extra[attr]}定义额外的属性，定义一个额外属性ip
# logger.add(sys.stderr,format="{extra[ip]} {message}")

# 利用bind为额外属性ip绑定一个值
# logger_1 = logger.bind(ip="localhost")
# 利用绑定了ip属性的日志记录器记录日志
# logger_1.info("这是一个日志信息")
# 可以重新绑定ip属性值
# logger_1.bind(ip="127.0.0.1").info("这是另一个日志信息")

# logger.remove()

# ip = "192.10.10.1"
# with logger.contextualize(ip=ip):
#     logger.info("这是一个日志信息")

# filter参数为True时记录日志，此处利用lambda函数查看是否有special额外属性
# logger.add(sys.stderr, filter=lambda record: "special" in record["extra"])
# logger.debug("This message is not logged to the file")
# logger.bind(special=True).info("This message, though, is logged to the file!")

# patch()函数运行动态的将信息传入日志中。
logger.add(sys.stderr, format="{extra[utc]} {message}")
logger = logger.patch(lambda record: record["extra"].update(utc=datetime.utcnow()))
while 1:
    time.sleep(10)
    logger.info("这是一个日志信息")