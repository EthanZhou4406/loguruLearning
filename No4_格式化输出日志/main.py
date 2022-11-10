from loguru import logger

logger.info("this is a {} log info","format")

logger.info("this is another {} log {}, {info}","2",4,info="another one")



logger.info("if you're using Python {}, prefer {feature} of course!", 3.6, feature="f-strings")