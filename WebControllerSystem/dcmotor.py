#导入gpio引脚、延时模块
from pyb import Pin,delay

#定义直流电机引脚
DC_F=Pin('E6',Pin.OUT_PP)
DC_B=Pin('E5',Pin.OUT_PP)

'''
#死循环中每隔一秒改变直流电机状态
while True:
    #正转1s
    DC_F.high()
    DC_B.low()
    delay(1000)
    
    #停止0.5s
    DC_F.low()
    DC_B.low()
    delay(500)

    #反转1s
    DC_F.low()
    DC_B.high()
    delay(1000)
'''