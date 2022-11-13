# 主要利用notifiers库
import notifiers
from notifiers.logging import NotificationHandler
from loguru import logger

# 邮箱的信息，寄件人的用户名和密码，收件人邮箱
params={
    "username": "ethanzh-u4406@126.com",
    "password": "PMEK-LQHS-WQMBHI",
    "to": "1574203568@qq.com",
    "host":"smtp.126.com",
    "ssl":True,
    "port":25,
}

# 单独发送一封邮件
notifier = notifiers.get_notifier("email",strict=True)
notifier.notify(message="The application is running",**params)


# 当发生错误日志时，发送警告邮件
handler = NotificationHandler("email",defaults=params)
logger.add(handler,level="ERROR")