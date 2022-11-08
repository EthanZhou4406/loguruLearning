# 1. 安装  

```shell	
pip install loguru
```

# 2.使用  

## 2.1 初次使用 

```python	
# 导入logger对象
from loguru import logger

#向控制台输出一个日志信息
logger.debug("this is my first debug log")
```

输出结果：

![image-20221108211555052](loguru.assets/image-20221108211555052.png)

默认情况下logger将日志信息输出到stderr中。

## 2.2 日志的认识

日志就是将程序运行过程中一些关键的信息记录下来，供程序员查看使用。

其中关键的信息通常是：

- 异常报错
- 执行步骤等

通常将日志以文件的形式存储在硬盘中，也可以直接将日志信息输出至窗口。

在loguru中默认将日志信息输出至窗口。

![image-20221108211555052](loguru.assets/image-20221108211555052.png)

观察这个例子发现，这条日志中主要由三个部分组成：

1. 时间
2. 日志等级
3. 日志具体内容

## 2.3 改变日志输出位置

