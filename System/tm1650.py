from pyb import Pin,udelay,delay

######数码管段码及寄存器地址######
data_num=[0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f] #0-9
data_alphabet=[0x77,0x7c,0x39,0x5e,0x79,0x71] #a-f
display_address=[0x6e,0x6c,0x6a,0x68] #数码管地址
display_brightness=[0x11,0x21,0x31,0x41,0x51,0x61,0x71,0x01] #亮度设置

######tm1650引脚初始化######
SDA=Pin('F1',Pin.OUT_PP)
SCL=Pin('F0',Pin.OUT_PP)

######tm1650命令######
TIM_COMMAND=0x48 #数据命令
TIM_START=0x01   #默认开启显示位
DIS_ADD_1=0x68 #第一个数码管地址
DIS_ADD_2=0x6a #第二个数码管地址
DIS_ADD_3=0x6c #第三个数码管地址
DIS_ADD_4=0x6e #第四个数码管地址
data_dp=0x80 #小数点的段码
data_null= 0x00 #不显示
data_neg=0x40 #负号的段码

#####tm1650发送数据#####
def Display_Send_Data(address,data):
    i=0
    buff=0
    SCL.high()
    SDA.high()
    udelay(1)
    SDA.low()
    udelay(1)
    SCL.low()
    udelay(2)
    
    i=0
    while i<8:
        buff = ((address >> (7- i))&0x01)
        if buff == 1:
            SDA.high()
        else:
            SDA.low()
        SCL.low()
        udelay(1)
        SCL.high()
        udelay(1)
        SCL.low()
        udelay(1)
        i = i+1

    SCL.high()
    udelay(2)
    SCL.low()
    udelay(2)

    i=0
    while i<8:
        buff = ((data >> (7- i))&0x01)
        if buff == 1:
            SDA.high()
        else:
            SDA.low()
        SCL.low()
        udelay(1)
        SCL.high()
        udelay(1)
        SCL.low()
        udelay(1)
        i=i+1

    SCL.high()
    udelay(1)
    SCL.low()
    udelay(1)

    SCL.high()
    SDA.low()
    udelay(1)
    SDA.high()
    udelay(1)
    
    
#####显示初始化#####
def Display_Init():
    delay(500) #等待芯片启动
    Display_Send_Data(TIM_COMMAND,display_brightness[6])#默认最大亮度
    Display_Send_Data(DIS_ADD_1,data_null)#不显示
    Display_Send_Data(DIS_ADD_2,data_null)
    Display_Send_Data(DIS_ADD_3,data_null)
    Display_Send_Data(DIS_ADD_4,data_null)


#####显示数字#####
#####num:数字范围0-9999#####
#####dp:是否显示小数点#####
def Show_Num(num,dp):
    i=0
    buff = 0
    if num <= 9999:
        i=0
        while i<4:
            buff = int(num % 10)
            if (dp&0x01) == 1:
                print("t")
                Display_Send_Data(display_address[i],data_num[buff]|data_dp)
            else:
                Display_Send_Data(display_address[i],data_num[buff])
            num /= 10
            dp = dp >> 1
            i=i+1
            
