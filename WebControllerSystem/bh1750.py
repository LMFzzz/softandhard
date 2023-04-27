import myiic
from pyb import delay

BH_CMD=0#写命令
BH_DATA=1#写数据

BH1750_SlaveAddress=0x46#设备地址
BH1750_writeAddress=0x46
BH1750_ReadAddress=0x47#设备地址
BS1750_DOWN=0x00#断电指令
BH1750_ON=0x01 # 通电指令
BH1750_RSE=0x07 # 重置指令
BH1750_CON_H=0x10 # 连续高分辨率模式，1lx，120ms
BH1750_CON_H2=0x11 # 连续高分辨率模式，0.5lx，120ms
BH1750_CON_L=0x13 # 连续低分辨率模式，4lx，16ms
BH1750_ONE_H=0x20 # 一次高分辨率模式，1lx，120ms
BH1750_ONE_H2=0x21 # 一次高分辨率模式，0.5lx，120ms
BH1750_ONE_L=0x23 # 一次低分辨率模式，4lx，16ms

RESOLUTION=BH1750_CON_H2 # 连续高分辨率模式，0.5lx
SCALE_INTERVAL=0.5

READ_ADDR=0x91 #((LM75A_ADDR << 1) | 0x01)
WRITE_ADDR=0x90 #((LM75A_ADDR << 1) | 0x0)

def bh17_write_reg(cmd):
    ack = 0 
    myiic.IIC3_Start()
    myiic.IIC3_Send_Byte(BH1750_writeAddress)
    ack = myiic.IIC3_Wait_Ack()
    if ack == 1:
        print("BH1750_writeAddress No ack \r\n")
        return 1
    
    myiic.IIC3_Send_Byte(cmd)
    ack = myiic.IIC3_Wait_Ack()
    if ack==1:
        print("cmd No ack\r\n")
        return 1;

    myiic.IIC3_Stop()
    return 0


def bh17_read_reg(read_buff,read_size):
    ack = 0
    myiic.IIC3_Start()
    myiic.IIC3_Send_Byte(BH1750_ReadAddress)
    ack = myiic.IIC3_Wait_Ack()
    if ack == 1:
        print("BH1750_ReadAddress No ack \r\n")
        return 1
    read_buff[0] = myiic.IIC3_Read_Byte(1)
    read_buff[1] = myiic.IIC3_Read_Byte(0)
    myiic.IIC3_Stop()
    return 0

#get value from bh1750
def bh1750_get_value():
    bh_buff = [0,0]#,buf[64];
    value=0.0
    bh17_write_reg(BH1750_ON)
    bh17_write_reg(BH1750_CON_H)
    reg = bh17_read_reg(bh_buff,2)
    value = (bh_buff[0]<<8)|bh_buff[1]

    if reg == 0:
        return value/1.2 * SCALE_INTERVAL
        #print("Light is : {0} lx\r\n".format(value/1.2 * SCALE_INTERVAL))

    return 0

'''
while True:
    light = bh1750_get_value()
    print("Light is : {0} lx".format(light))
    delay(1000)
'''