import sys
from loguru import logger

# 自定义一个日志等级
# name表示该日志等级的名称
# no表示该日志等级的安全等级，用来决定合适添加或更新
# color表示该日志等级支持的颜色markdown标签
# icon表示该日志的图标
myLevel = logger.level(name="myInfo",no=25,color="<white><bold>",icon="\!/")
# 使用自定义等级，输出一个日志
logger.remove()
logger.add(sys.stderr,format="{time} {level.name} {level.icon} {message}")
logger.log("myInfo","这是一个利用自定义日志等级，输出的日志")
