from loguru import logger
import time
from datetime import timedelta

# 删除默认日志处理器
logger.remove()

# 自定义日志文件处理器
# 将日志存储在文件中
# hander_1将所有的日志存放在一个日志文件中
hander_1 = logger.add("./logs/common.log")

# hander_2将根据日志产生时间不同，存放在不同的日志文件中
hander_2 = logger.add("./logs/logs_{time:YYYY-MM-DD-HH-mm-ss}.log")


# rotation参数表示当文件达到条件后，开始新的日志文件记录
# hander_3将日志文件存在一个日志文件中，当日志文件大小达到1KB时，开始新的日志文件记录
hander_3 = logger.add("./logs/log3.log",rotation="1KB")
# hander_4将日志文件存在一个日志文件中，每天12:00时，开始新的日志文件记录
hander_4 = logger.add("./logs/log4.log",rotation="12:00")
# hander_5将日志文件存在一个日志文件中，并每过1周时间，开始新的日志信息
hander_5 = logger.add("./logs/log5.log",rotation="1 week")

# retention参数表示将超过指定时间长度的日志文件删除，作用在生成新的日志文件时，或程序退出时
times = timedelta(seconds=20)
# hander_6每当日志文件达到1KB时，将产生一个新的日志文件，并删除存在时长超过20s的日志文件
hander_6 = logger.add("./logs/logs_{time:YYYY-MM-DD-HH-mm-ss}.log",rotation="1KB",retention=times)

# compression表示将该日志处理器生成的日志文件，在日志文件不在被程序占用时(生成了新的日志文件时，或者程序退出时)压缩存储，
# hander_7将日志文件压缩存储
hander_7 = logger.add("./logs/logs_{time:YYYY-MM-DD-HH-mm-ss}.log",rotation="1KB",compression="zip")

while 1:
    logger.info("这个是什么意思？")
    time.sleep(5)


