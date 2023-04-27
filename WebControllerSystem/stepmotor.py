# 导入gpio引脚、延时模块
from pyb import Pin, delay

# 定义步进电机引脚
STEP_1 = Pin('E1', Pin.OUT_PP)
STEP_2 = Pin('E2', Pin.OUT_PP)
STEP_3 = Pin('E3', Pin.OUT_PP)
STEP_4 = Pin('E4', Pin.OUT_PP)


# 定义正转一步函数
def stepmotor_forward(speed):
    STEP_1.high()
    STEP_2.low()
    STEP_3.low()
    STEP_4.low()
    delay(speed)

    STEP_1.low()
    STEP_4.high()
    delay(speed)

    STEP_4.low()
    STEP_3.high()
    delay(speed)

    STEP_3.low()
    STEP_2.high()
    delay(speed)


# 定义反转一步函数
def stepmotor_backward(speed):
    STEP_1.high()
    STEP_2.low()
    STEP_3.low()
    STEP_4.low()
    delay(speed)

    STEP_1.low()
    STEP_2.high()
    delay(speed)

    STEP_2.low()
    STEP_3.high()
    delay(speed)

    STEP_3.low()
    STEP_4.high()
    delay(speed)


'''
#死循环中不断反转步进电机电机状态
while True:
    x=0
    while x<200:#正转200步
        x=x+1
        stepmotor_forward(5)
        
    delay(150)
    
    x=0
    while x<200:#反转200步
        x=x+1
        stepmotor_backward(5)
'''
