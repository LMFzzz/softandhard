import myiic
from pyb import delay

MPU_SELF_TESTX_REG=0X0D    #自检寄存器X
MPU_SELF_TESTY_REG=0X0E    #自检寄存器Y
MPU_SELF_TESTZ_REG=0X0F    #自检寄存器Z
MPU_SELF_TESTA_REG=0X10    #自检寄存器A
MPU_SAMPLE_RATE_REG=0X19    #采样频率分频器
MPU_CFG_REG=0X1A    #配置寄存器
MPU_GYRO_CFG_REG=0X1B    #陀螺仪配置寄存器
MPU_ACCEL_CFG_REG=0X1C    #加速度计配置寄存器
MPU_MOTION_DET_REG=0X1F    #运动检测阀值设置寄存器
MPU_FIFO_EN_REG=0X23    #FIFO使能寄存器
MPU_I2CMST_CTRL_REG=0X24    #IIC主机控制寄存器
MPU_I2CSLV0_ADDR_REG=0X25    #IIC从机0器件地址寄存器
MPU_I2CSLV0_REG=0X26    #IIC从机0数据地址寄存器
MPU_I2CSLV0_CTRL_REG=0X27    #IIC从机0控制寄存器
MPU_I2CSLV1_ADDR_REG=0X28    #IIC从机1器件地址寄存器
MPU_I2CSLV1_REG=0X29    #IIC从机1数据地址寄存器
MPU_I2CSLV1_CTRL_REG=0X2A    #IIC从机1控制寄存器
MPU_I2CSLV2_ADDR_REG=0X2B    #IIC从机2器件地址寄存器
MPU_I2CSLV2_REG=0X2C    #IIC从机2数据地址寄存器
MPU_I2CSLV2_CTRL_REG=0X2D    #IIC从机2控制寄存器
MPU_I2CSLV3_ADDR_REG=0X2E    #IIC从机3器件地址寄存器
MPU_I2CSLV3_REG=0X2F    #IIC从机3数据地址寄存器
MPU_I2CSLV3_CTRL_REG=0X30    #IIC从机3控制寄存器
MPU_I2CSLV4_ADDR_REG=0X31    #IIC从机4器件地址寄存器
MPU_I2CSLV4_REG=0X32    #IIC从机4数据地址寄存器
MPU_I2CSLV4_DO_REG=0X33    #IIC从机4写数据寄存器
MPU_I2CSLV4_CTRL_REG=0X34    #IIC从机4控制寄存器
MPU_I2CSLV4_DI_REG=0X35    #IIC从机4读数据寄存器

MPU_I2CMST_STA_REG=0X36    #IIC主机状态寄存器
MPU_INTBP_CFG_REG=0X37    #中断/旁路设置寄存器
MPU_INT_EN_REG=0X38    #中断使能寄存器
MPU_INT_STA_REG=0X3A    #中断状态寄存器

MPU_ACCEL_XOUTH_REG=0X3B    #加速度值,X轴高8位寄存器
MPU_ACCEL_XOUTL_REG=0X3C    #加速度值,X轴低8位寄存器
MPU_ACCEL_YOUTH_REG=0X3D    #加速度值,Y轴高8位寄存器
MPU_ACCEL_YOUTL_REG=0X3E    #加速度值,Y轴低8位寄存器
MPU_ACCEL_ZOUTH_REG=0X3F    #加速度值,Z轴高8位寄存器
MPU_ACCEL_ZOUTL_REG=0X40    #加速度值,Z轴低8位寄存器

MPU_TEMP_OUTH_REG=0X41    #温度值高八位寄存器
MPU_TEMP_OUTL_REG=0X42    #温度值低8位寄存器

MPU_GYRO_XOUTH_REG=0X43    #陀螺仪值,X轴高8位寄存器
MPU_GYRO_XOUTL_REG=0X44    #陀螺仪值,X轴低8位寄存器
MPU_GYRO_YOUTH_REG=0X45    #陀螺仪值,Y轴高8位寄存器
MPU_GYRO_YOUTL_REG=0X46    #陀螺仪值,Y轴低8位寄存器
MPU_GYRO_ZOUTH_REG=0X47    #陀螺仪值,Z轴高8位寄存器
MPU_GYRO_ZOUTL_REG=0X48    #陀螺仪值,Z轴低8位寄存器

MPU_I2CSLV0_DO_REG=0X63    #IIC从机0数据寄存器
MPU_I2CSLV1_DO_REG=0X64    #IIC从机1数据寄存器
MPU_I2CSLV2_DO_REG=0X65    #IIC从机2数据寄存器
MPU_I2CSLV3_DO_REG=0X66    #IIC从机3数据寄存器

MPU_I2CMST_DELAY_REG=0X67    #IIC主机延时管理寄存器
MPU_SIGPATH_RST_REG=0X68    #信号通道复位寄存器
MPU_MDETECT_CTRL_REG=0X69    #运动检测控制寄存器
MPU_USER_CTRL_REG=0X6A    #用户控制寄存器
MPU_PWR_MGMT1_REG=0X6B    #电源管理寄存器1
MPU_PWR_MGMT2_REG=0X6C    #电源管理寄存器2
MPU_FIFO_CNTH_REG=0X72    #FIFO计数寄存器高八位
MPU_FIFO_CNTL_REG=0X73    #FIFO计数寄存器低八位
MPU_FIFO_RW_REG=0X74    #FIFO读写寄存器
MPU_DEVICE_ID_REG=0X75    #器件ID寄存器

#如果AD0脚(9脚)接地,IIC地址为0X68(不包含最低位).
#如果接V3.3,则IIC地址为0X69(不包含最低位).
MPU_ADDR=0X68

#存储陀螺仪数据的类
class mpu6050:
    ax=0#x轴加速度
    ay=0#y轴加速度
    az=0#z轴加速度
    gx=0#x轴角速度
    gy=0#y轴角速度
    gz=0#z轴角速度

#陀螺仪初始化函数
def MPU_Init():
    MPU_Write_Byte(MPU_PWR_MGMT1_REG,0X80);    #复位MPU6050
    delay(100);
    MPU_Write_Byte(MPU_PWR_MGMT1_REG,0X00);    #唤醒MPU6050
    MPU_Set_Gyro_Fsr(3);                    #陀螺仪传感器,±2000dps
    MPU_Set_Accel_Fsr(0);                    #加速度传感器,±2g
    MPU_Set_Rate(50);                        #设置采样率50Hz
    MPU_Write_Byte(MPU_INT_EN_REG,0X00);    #关闭所有中断
    MPU_Write_Byte(MPU_USER_CTRL_REG,0X00);    #I2C主模式关闭
    MPU_Write_Byte(MPU_FIFO_EN_REG,0X00);    #关闭FIFO
    MPU_Write_Byte(MPU_INTBP_CFG_REG,0X80);    #INT引脚低电平有效
    res=MPU_Read_Byte(MPU_DEVICE_ID_REG);
    if res==MPU_ADDR:#器件ID正确
        MPU_Write_Byte(MPU_PWR_MGMT1_REG,0X01);    #设置CLKSEL,PLL X轴为参考
        MPU_Write_Byte(MPU_PWR_MGMT2_REG,0X00);    #加速度与陀螺仪都工作
        MPU_Set_Rate(50);                        #设置采样率为50Hz
    else:
        return 1;
    return 0;


#设置MPU6050陀螺仪传感器满量程范围
#fsr:0,±250dps;1,±500dps;2,±1000dps;3,±2000dps
#返回值:0,设置成功
#    其他,设置失败
def MPU_Set_Gyro_Fsr(fsr):
    value = MPU_Write_Byte(MPU_GYRO_CFG_REG,fsr<<3)
    return value#设置陀螺仪满量程范围

#设置MPU6050加速度传感器满量程范围
#fsr:0,±2g;1,±4g;2,±8g;3,±16g
#返回值:0,设置成功
#    其他,设置失败
def MPU_Set_Accel_Fsr(fsr):
    value = MPU_Write_Byte(MPU_ACCEL_CFG_REG,fsr<<3)
    return value#设置加速度传感器满量程范围

#设置MPU6050的数字低通滤波器
#lpf:数字低通滤波频率(Hz)
#返回值:0,设置成功
#    其他,设置失败
def MPU_Set_LPF(lpf):
    data=0;
    if lpf>=188:
        data=1
    elif lpf>=98:
        data=2;
    elif lpf>=42:
        data=3;
    elif lpf>=20:
        data=4;
    elif lpf>=10:
        data=5;
    else:
        data=6;
    value = MPU_Write_Byte(MPU_CFG_REG,data);
    return value#设置数字低通滤波器

#设置MPU6050的采样率(假定Fs=1KHz)
#rate:4~1000(Hz)
#返回值:0,设置成功
#    其他,设置失败
def MPU_Set_Rate(rate):
    data=0
    if rate>1000:
        rate=1000;
    if rate<4:
        rate=4;
    data=1000/rate-1;
    data=MPU_Write_Byte(MPU_SAMPLE_RATE_REG,data);    #设置数字低通滤波器
    value = MPU_Set_LPF(rate/2);
    return  value#自动设置LPF为采样率的一半


#得到温度值
#返回值:温度值(扩大了100倍)
def MPU_Get_Temperature():
    buf=[0,0]
    MPU_Read_Len(MPU_ADDR,MPU_TEMP_OUTH_REG,2,buf)
    raw=(buf[0]<<8)|buf[1]
    if raw>=(65536/2):
        raw = raw-65535
    temp=36.53+(raw)/340
    return temp

#得到陀螺仪值(原始值)
#gx,gy,gz:陀螺仪x,y,z轴的原始读数(带符号)
#返回值:0,成功
#    其他,错误代码
def MPU_Get_Gyroscope():
    buf=[0,0,0,0,0,0]
    res=MPU_Read_Len(MPU_ADDR,MPU_GYRO_XOUTH_REG,6,buf)
    if res==0:
        mpu6050.gx=(buf[0]<<8)|buf[1]
        mpu6050.gy=(buf[2]<<8)|buf[3]
        mpu6050.gz=(buf[4]<<8)|buf[5]
        if mpu6050.gx>=(65536/2):
            mpu6050.gx-=65535
        if mpu6050.gy>=(65536/2):
            mpu6050.gy-=65535
        if mpu6050.gz>=(65536/2):
            mpu6050.gz-=65535

    return res

#得到加速度值(原始值)
#gx,gy,gz:陀螺仪x,y,z轴的原始读数(带符号)
#返回值:0,成功
#    其他,错误代码
def MPU_Get_Accelerometer():
    buf=[0,0,0,0,0,0]
    res=MPU_Read_Len(MPU_ADDR,MPU_ACCEL_XOUTH_REG,6,buf);
    if res==0:
        mpu6050.ax=(buf[0]<<8)|buf[1];
        mpu6050.ay=(buf[2]<<8)|buf[3];
        mpu6050.az=(buf[4]<<8)|buf[5];
        if mpu6050.ax>=(65536/2):
            mpu6050.ax-=65535
        if mpu6050.ay>=(65536/2):
            mpu6050.ay-=65535
        if mpu6050.az>=(65536/2):
            mpu6050.az-=65535
    return res

#IIC连续写
#addr:器件地址
#reg:寄存器地址
#len:写入长度
#buf:数据区
#返回值:0,正常
#    其他,错误代码
def MPU_Write_Len(addr,reg,len,buf):
    myiic.IIC3_Start();
    myiic.IIC3_Send_Byte((addr<<1)|0);#发送器件地址+写命令
    if (myiic.IIC3_Wait_Ack()):    #等待应答
        myiic.IIC3_Stop();
        return 1;

    myiic.IIC3_Send_Byte(reg);    #写寄存器地址
    myiic.IIC3_Wait_Ack();        #等待应答
    i=0
    while i<len:
        myiic.IIC3_Send_Byte(buf[i]);    #发送数据
        if (myiic.IIC3_Wait_Ack()):       #等待ACK
            myiic.IIC3_Stop();
            return 1;
        i+=1

    myiic.IIC3_Stop();
    return 0;

#IIC连续读
#addr:器件地址
#reg:要读取的寄存器地址
#len:要读取的长度
#buf:读取到的数据存储区
#返回值:0,正常
#    其他,错误代码
def MPU_Read_Len(addr,reg,len,buf):
    myiic.IIC3_Start();
    myiic.IIC3_Send_Byte((addr<<1)|0);#发送器件地址+写命令
    if myiic.IIC3_Wait_Ack():    #等待应答
        myiic.IIC3_Stop();
        return 1;
    
    myiic.IIC3_Send_Byte(reg);    #写寄存器地址
    myiic.IIC3_Wait_Ack();        #等待应答
    myiic.IIC3_Start();
    myiic.IIC3_Send_Byte((addr<<1)|1);#发送器件地址+读命令
    myiic.IIC3_Wait_Ack();        #等待应答
    
    i=0
    while len!=0:
        if len==1:
            buf[i]=myiic.IIC3_Read_Byte(0);#读数据,发送nACK
        else:
            buf[i]=myiic.IIC3_Read_Byte(1);#读数据,发送ACK
        len-=1
        i+=1
    
    myiic.IIC3_Stop();    #产生一个停止条件
    return 0;

#IIC写一个字节
#reg:寄存器地址
#data:数据
#返回值:0,正常
#    其他,错误代码
def MPU_Write_Byte(reg,data):
    myiic.IIC3_Start();
    myiic.IIC3_Send_Byte((MPU_ADDR<<1)|0);#发送器件地址+写命令
    if myiic.IIC3_Wait_Ack():    #等待应答
        myiic.IIC3_Stop();
        return 1;

    myiic.IIC3_Send_Byte(reg);    #写寄存器地址
    myiic.IIC3_Wait_Ack();        #等待应答
    myiic.IIC3_Send_Byte(int(data));#发送数据
    if myiic.IIC3_Wait_Ack():    #等待ACK
        myiic.IIC3_Stop();
        return 1;
    myiic.IIC3_Stop();
    return 0;

#IIC读一个字节
#reg:寄存器地址
#返回值:读到的数据
def MPU_Read_Byte(reg):
    myiic.IIC3_Start();
    myiic.IIC3_Send_Byte((MPU_ADDR<<1)|0);#发送器件地址+写命令
    myiic.IIC3_Wait_Ack();        #等待应答
    myiic.IIC3_Send_Byte(reg);    #写寄存器地址
    myiic.IIC3_Wait_Ack();        #等待应答
    myiic.IIC3_Start();
    myiic.IIC3_Send_Byte((MPU_ADDR<<1)|1);#发送器件地址+读命令
    myiic.IIC3_Wait_Ack();        #等待应答
    res=myiic.IIC3_Read_Byte(0);#读取数据,发送nACK
    myiic.IIC3_Stop();            #产生一个停止条件
    return res;

MPU_Init()
'''
while True:
    temp = MPU_Get_Temperature()
    MPU_Get_Gyroscope()
    MPU_Get_Accelerometer()
    print("temp:{}".format(temp))
    print("gx:{}   gy:{}   gz:{}".format(mpu6050.gx,mpu6050.gy,mpu6050.gz))
    print("ax:{}   ay:{}   az:{}\r\n".format(mpu6050.ax,mpu6050.ay,mpu6050.az))
    delay(1000)
'''