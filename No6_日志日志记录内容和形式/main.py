import sys
from loguru import logger

logger.remove()

logger.add(sys.stderr,format="<yellow>{time}</yellow>--<red>{message}</red>")

logger.info("这是一个日志信息")
