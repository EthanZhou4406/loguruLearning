from loguru import logger
import sys
import math

# exception参数的说明
# True时记录异常的详细报错信息
# False时忽略详细的报错信息

def fun(x):
    1/x

try:
    fun(0)
except ZeroDivisionError:
    logger.opt(exception=False).error("这是一个错误")

print("----------------------------------")

try:
    fun(0)
except ZeroDivisionError:
    logger.opt(exception=True).error("这是一个错误")


# record 参数的说明
# record 为True时，表示在格式化输出中可以使用record的属性
# record 为False时，表示在格式化输出中不可以使用record的属性
logger.opt(record=True).info("Current line is:{record[line]}")
logger.opt(record=False).info("Current line is:{record[line]}")

# lazy 参数的说明
# lazy 为True时，格式化信息中的变量，将作为一个函数进行调用，并将其结果放入格式化信息中
# lazy 为False时，格式化信息中的变量，将根据其的赋值对象进行存储
logger.opt(lazy=True).debug("if sink <=Debug:{x}",x=lambda:math.factorial(2**5))
logger.opt(lazy=False).debug("if sink <=Debug:{x}",x=lambda:math.factorial(2**5))
logger.opt(lazy=False).debug("if sink <=Debug:{x}",x=1)
# logger.opt(lazy=True).debug("if sink <=Debug:{x}",x=1)

# colors 参数说明
# colors 为True时，日志信息中颜色标签会被渲染
# colors 为False时，日志信息中颜色标签不会被渲染
logger.opt(colors=True).info("<green>这是一个日志信息</green>")
logger.opt(colors=False).info("<green>这是一个日志信息</green>")

# raw 参数说明
# raw 为True时，会忽略sink中添加的信息，而只输出message
# raw 为False时，会添加sink中添加的信息，输出format中的信息
logger.opt(raw=True).info("这是一个日志信息\n")
logger.opt(raw=False).info("这是一个日志信息\n")

# capture 参数说明
# capture 为True时，可以使用extra中的键值对
# capture 为False时，无法使用extra中的键值对
# logger.add(sys.stderr,format="{extra[value]}--{message}")
# logger_1=logger.bind(value=123)
# logger_1.opt(capture=True).info("Displayed but not captured:{valu}",valu="test")
# logger_1.opt(capture=False).info("Displayed but not captured:")


# depth 参数说明
# depth 为0时表示当前函数层，1表示外1层函数，n表示外n层函数，main层为module层，n最多为函数的层数
def wrapped():
    logger.opt(depth=0).info("get 0 context")
    logger.opt(depth=1).info("get 1 context")
    logger.opt(depth=2).info("get 2 context")
    logger.opt(depth=3).info("get 3 context")
    # logger.opt(depth=4).info("get 4 context")

def func():
    wrapped()
    # logger.opt(depth=2).info("get func context")

def funcc():
    func()
funcc()