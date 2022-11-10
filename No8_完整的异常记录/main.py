import sys
from loguru import logger

logger.remove()
logger.add(sys.stderr,backtrace=True,diagnose=True)

def func(a,b):
    return a/b

def nested(c):
    try:
        func(5,c)
    except ZeroDivisionError:
        # 输出一个异常日志What？！
        logger.exception("What?!")

nested(0)