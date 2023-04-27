from pyb import UART, delay

# 显示类传感器
import tm1650
import oled
import oledfont
import myiic
# 控制类传感器
import beep
import dcmotor
import stepmotor
import relay
# 安防类传感器
import security
# 采集类传感器
import bmp180
import bh1750
import mp503
import mpu6050
import dht11
# 线程
import _thread

wifi = UART(6, 115200)
DC_OPEN = 1
DC_CLOSE = 2
STEP_OPEN = 3
STEP_CLOSE = 4
BEEP_OPEN = 5
BEEP_CLOSE = 6
RELAY_OPEN = 7
RELAY_CLOSE = 8
cmd = 0
step = 0
tm1650.Display_Init()


# 创建TCP服务器
# Name:Wifi名称
# Pass:Wifi密码
# IP:IP号
# Port:端口号

def CreateTcpServer(Name, Pass, Port):
    wifi.write("+++")  # 进入AT指令模式
    delay(500)
    wifi.write("AT\r\n")  # 测试AT指令
    delay(500)
    wifi.write("AT+CWMODE=2\r\n")  # 选择AP模式
    delay(500)
    wifi.write("AT+RST\r\n");  # 复位
    delay(2000)
    # 创建WIFI
    wifi.write("AT+CWSAP=\"" + Name + "\",\"" + Pass + "\",1,3\r\n")
    delay(500)
    # 设置WiFi模块IP地址
    wifi.write("AT+CIPAP=\"192.168.1.1\",\"192.168.1.1\",\"255.255.255.0\"\r\n")
    delay(500)
    wifi.write("AT+CIPMUX=1\r\n")  # 启用多连
    delay(500)
    wifi.write("AT+CIPSERVER=1," + Port + "\r\n")  # 设置端口号
    delay(500)
    wifi.write("AT+CIFSR\r\n")  # 查询模块信息


# 创建一个TCP服务器
CreateTcpServer("LMF", "12345678", "8888")


# wifi发送数据
def SendWifiData(data):
    dlen = len(data)
    wifi.write("AT+CIPSEND=0,{}\r\n".format(dlen))
    delay(150);
    wifi.write(data)


delay(500)


# 接收安卓端发送的信息
def receive_thread():
    while True:
        # 串口(wifi)数据
        if wifi.any():
            buf = wifi.read().decode()
            print(buf)
            if buf.find("C1_OPEN") != -1:
                dcmotor.DC_F.high()
                dcmotor.DC_B.low()
            if buf.find("C1_CLOSE") != -1:
                dcmotor.DC_F.high()
                dcmotor.DC_B.low()
            if buf.find("C2_OPEN") != -1:
                _thread.start_new_thread(forward_thread, ())
            if buf.find("C2_CLOSE") != -1:
                _thread.start_new_thread(back_thread, ())
            if buf.find("C3_OPEN") != -1:
                beep.BEEP.high()
            if buf.find("C3_CLOSE") != -1:
                beep.BEEP.low()
            if buf.find("C4_OPEN") != -1:
                relay.RELAY.high()
            if buf.find("C4_CLOSE") != -1:
                relay.RELAY.low()
            if buf.find("DIG") != -1:  # 数码管数据
                num1 = int(buf.split("_")[1])
                num2 = int(buf.split("_")[2])
                num3 = int(buf.split("_")[3])
                num4 = int(buf.split("_")[4])
                print(num1)
                print(num2)
                print(num3)
                print(num4)
                num = num1 * 1000 + num2 * 100 + num3 * 10 + num4
                print(num)
                tm1650.Show_Num(num, 0)
            if buf.find("LED") != -1:  # OLED数据
                obuf = buf.split("_")[1]
                oled.OLED_ShowStr(0, 0, obuf)


delay(500)


# 将传感器数据发送至安卓端
def send_thread():
    while True:
        # 安防类传感器
        flame = security.FLAME.value()
        fog = security.FOG.value()
        py = security.PY.value()
        hall = security.HALL.value()
        sbuf = 'SECURITY_{' + '"SMOKE":"{}","FIRE":"{}","IR":"{}","BODY":"{}","MAG":"{}"'.format(~fog + 2, ~flame + 2,
                                                                                                 3, ~py + 2,
                                                                                                 ~hall + 2) + '}'
        print(sbuf)
        SendWifiData(sbuf)
        delay(1000)
        # 采集类传感器
        bmp180.BMP_UncompemstatedToTrue()
        dht11.d.measure()
        p = bmp180.bmp180.p * 10
        light = bh1750.bh1750_get_value()
        air = mp503.mp503.read()
        mpu6050.MPU_Get_Gyroscope()
        sbuf = 'SENSOR_{' + '"TEMP":"{}","HUM":"{}","LIGHT":"{}","AIR":"{}","PR":"{}"'.format(dht11.d.temperature(),
                                                                                              dht11.d.humidity(), light,
                                                                                              air, p,
                                                                                              mpu6050.mpu6050.gx,
                                                                                              mpu6050.mpu6050.gy,
                                                                                              mpu6050.mpu6050.gz) + '}'
        print(sbuf)
        SendWifiData(sbuf)
        delay(1000)


delay(500)


def forward_thread():
    step = 0
    while step < 200:
        step = step + 1
        print(step)
        stepmotor.stepmotor_forward(5)
    delay(150)


delay(150)


def back_thread():
    step = 0
    while step < 200:
        step = step + 1
        print(step)
        stepmotor.stepmotor_forward(5)
    delay(150)


# 创建两个线程
delay(500)
_thread.start_new_thread(receive_thread, ())
delay(500)
_thread.start_new_thread(send_thread, ())

while True:
    pass
