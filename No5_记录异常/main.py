from loguru import logger

@logger.catch
def my_function(x,y,z):
    return 1/(x+y+z)

my_function(0,0,0)