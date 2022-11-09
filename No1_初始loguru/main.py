import sys
# 导入logger对象
from loguru import logger

#向控制台输出一个日志信息
logger.debug("this is my first debug log")

#配置处理器
logger.add(sys.stderr,format="{time} {level} {message}",filter="my_module",level="INFO")
logger.info("this is a info log")

# 删除处理器
logger.remove()

# 将日志输出到文件中
# logger.add("file_{time}.log")
logger.info("this is a info log")

# 日志文件的覆盖或压缩操作
logger.add("file_1.log", rotation="500 MB")    # Automatically rotate too big file
# logger.add("file_2.log", rotation="12:00")     # New file is created each day at noon
# logger.add("file_3.log", rotation="1 week")    # Once the file is too old, it's rotated
# logger.add("file_X.log", retention="10 days")  # Cleanup after some time
# logger.add("file_Y.log", compression="zip")    # Save some loved space

# 日志内容支持可视化输出
logger.info("If you're using Python {}, prefer {feature} of course!", 3.6, feature="f-strings")
logger.remove()
# 利用@logger.catch装饰器捕获函数异常信息
@logger.catch
def my_function(x,y,z):
    return 1/(x+y+z)
my_function(0,0,0)

# 给日志添加色彩
logger.add(sys.stdout,colorize=True,format="<red>{time}</red> <level>{message}</level>")
logger.info("colorful logging")

# 异步的，线程安全的
logger.add("somefile.log",enqueue=True)

# 完全描述异常，自带变量值
logger.add("out.log", backtrace=True, diagnose=True)  # Caution, may leak sensitive data in prod

def func(a, b):
    return a / b

def nested(c):
    try:
        func(5, c)
    except ZeroDivisionError:
        logger.exception("What?!")

nested(0)

# 结构化日志
# logger.add(custom_sink_function, serialize=True)

# 利用bind来更改日志的上下文信息
logger.add("file.log", format="{extra[ip]} {extra[user]} {message}")
context_logger = logger.bind(ip="192.168.0.1", user="someone")
context_logger.info("Contextualize your logger easily")
context_logger.bind(user="someone_else").info("Inline binding of extra attribute")
context_logger.info("Use kwargs to add context during formatting: {user}", user="anybody")