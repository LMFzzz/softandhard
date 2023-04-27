#导入gpio引脚、延时模块
from pyb import Pin,delay

#定义继电器引脚
RELAY=Pin('D7',Pin.OUT_PP)
'''
#死循环中每隔一秒改变继电器状态
while True:
    RELAY.high()
    delay(1000)
    RELAY.low()
    delay(1000)
'''