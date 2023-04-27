from pyb import Pin,delay,udelay

#初始化IIC
SDA1=Pin('B7',Pin.OUT_PP)
SCL1=Pin('B6',Pin.OUT_PP)
SCL1.high()
SDA1.high()
SDA3=Pin('C9',Pin.OUT_PP)
SCL3=Pin('A8',Pin.OUT_PP)
SCL3.high()
SDA3.high()

#sda线输出   
def SDA1_OUT():
    SDA1=Pin('B7',Pin.OUT_PP)

#sda线输入
def SDA1_IN():
    SDA1=Pin('B7',Pin.IN, Pin.PULL_UP)

#产生IIC起始信号
def IIC1_Start():
    SDA1_OUT()#sda线输出
    SDA1.high() 
    SCL1.high()
    udelay(6)
    SDA1.low()#START:when CLK is high,DATA change form high to low 
    udelay(6)
    SCL1.low()#钳住I2C总线，准备发送或接收数据 

#产生IIC停止信号
def IIC1_Stop():
    SDA1_OUT()#sda线输出
    SCL1.low()
    SDA1.low()#STOP:when CLK is high DATA change form low to high
    udelay(6)
    SCL1.high() 
    udelay(6)
    SDA1.high()#发送I2C总线结束信号

#等待应答信号到来
#返回值：1，接收应答失败
#        0，接收应答成功
def IIC1_Wait_Ack():
    ucErrTime=0
    SDA1_IN()#SDA设置为输入  
    SDA1.high()
    udelay(1)
    SCL1.high()
    udelay(1)
    while SDA1.value()==1:
        ucErrTime += 1
        if ucErrTime>250:
            IIC1_Stop()
            return 1
        
    SCL1.low()#时钟输出0 
    return 0

#产生ACK应答
def IIC1_Ack():
    SCL1.low()
    SDA1_OUT()
    SDA1.low()
    udelay(2)
    SCL1.high()
    udelay(2)
    SCL1.low()

#不产生ACK应答
def IIC1_NAck():
    SCL1.low()
    SDA1_OUT()
    SDA1.high()
    udelay(2)
    SCL1.high()
    udelay(2)
    SCL1.low()

#IIC发送一个字节
#返回从机有无应答
#1，有应答
#0，无应答
def IIC1_Send_Byte(txd):
    SDA1_OUT()
    SCL1.low()#拉低时钟开始数据传输
    t=0
    while t<8:
        if ((txd&0x80)>>7)==1:
            SDA1.high()
        else:
            SDA1.low()
        txd = txd<<1
        udelay(2)
        SCL1.high()
        udelay(2)
        SCL1.low()
        udelay(2)
        t += 1
        
#读1个字节，ack=1时，发送ACK，ack=0，发送nACK   
def IIC1_Read_Byte(ack):
    receive=0
    SDA1_IN()#SDA设置为输入
    i=0
    while i<8:
        SCL1.low() 
        udelay(2)
        SCL1.high()
        receive = receive<<1
        if SDA1.value()==1:
            receive = receive + 1 
        udelay(1)
        i = i+1

    if ack == 0:
        IIC1_NAck()#发送nACK
    else:
        IIC1_Ack()#发送ACK   
    return receive


#sda线输出   
def SDA3_OUT():
    SDA3=Pin('C9',Pin.OUT_PP)

#sda线输入
def SDA3_IN():
    SDA3=Pin('C9',Pin.IN, Pin.PULL_UP)

#产生IIC起始信号
def IIC3_Start():
    SDA3_OUT()#sda线输出
    SDA3.high() 
    SCL3.high()
    udelay(6)
    SDA3.low()#START:when CLK is high,DATA change form high to low 
    udelay(6)
    SCL3.low()#钳住I2C总线，准备发送或接收数据 

#产生IIC停止信号
def IIC3_Stop():
    SDA3_OUT()#sda线输出
    SCL3.low()
    SDA3.low()#STOP:when CLK is high DATA change form low to high
    udelay(6)
    SCL3.high() 
    udelay(6)
    SDA3.high()#发送I2C总线结束信号

#等待应答信号到来
#返回值：1，接收应答失败
#        0，接收应答成功
def IIC3_Wait_Ack():
    ucErrTime=0
    SDA3_IN()#SDA设置为输入  
    SDA3.high()
    udelay(1)
    SCL3.high()
    udelay(1)
    while SDA3.value()==1:
        ucErrTime += 1
        if ucErrTime>250:
            IIC3_Stop()
            return 1
        
    SCL3.low()#时钟输出0 
    return 0

#产生ACK应答
def IIC3_Ack():
    SCL3.low()
    SDA3_OUT()
    SDA3.low()
    udelay(2)
    SCL3.high()
    udelay(2)
    SCL3.low()

#不产生ACK应答
def IIC3_NAck():
    SCL3.low()
    SDA3_OUT()
    SDA3.high()
    udelay(2)
    SCL3.high()
    udelay(2)
    SCL3.low()

#IIC发送一个字节
#返回从机有无应答
#1，有应答
#0，无应答
def IIC3_Send_Byte(txd):
    SDA3_OUT()
    SCL3.low()#拉低时钟开始数据传输
    t=0
    while t<8:
        if ((txd&0x80)>>7)==1:
            SDA3.high()
        else:
            SDA3.low()
        txd = txd<<1
        udelay(2)
        SCL3.high()
        udelay(2)
        SCL3.low()
        udelay(2)
        t += 1
        
#读1个字节，ack=1时，发送ACK，ack=0，发送nACK   
def IIC3_Read_Byte(ack):
    receive=0
    SDA3_IN()#SDA设置为输入
    i=0
    while i<8:
        SCL3.low() 
        udelay(2)
        SCL3.high()
        receive = receive<<1
        if SDA3.value()==1:
            receive = receive + 1 
        udelay(1)
        i = i+1

    if ack == 0:
        IIC3_NAck()#发送nACK
    else:
        IIC3_Ack()#发送ACK   
    return receive
