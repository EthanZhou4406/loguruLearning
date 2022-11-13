from loguru import logger
# 利用disable来关闭__main__模块下的日志记录
logger.disable("__main__")
logger.info("No matter added sinks, this message is not displayed")
# 利用enable来开启__main__模块下的日志记录
logger.enable("__main__")
logger.info("This message however is propagated to the sinks")



from sub import func
logger.disable("sub")
func(0)
logger.enable("sub")
func(0)