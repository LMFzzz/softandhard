#导入gpio引脚、延时模块
from pyb import Pin,delay

#定义蜂鸣器引脚
BEEP=Pin('B14',Pin.OUT_PP)

'''
#死循环中使蜂鸣器不断哔哔哔鸣叫
while True:
    BEEP.high()
    delay(200)
    BEEP.low()
    delay(1000)
'''