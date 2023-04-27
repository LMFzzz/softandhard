import myiic
import oledfont
from pyb import delay

def Write_IIC_Command(IIC_Command):
    myiic.IIC1_Start()
    myiic.IIC1_Send_Byte(0x78)#Slave address,SA0=0
    myiic.IIC1_Wait_Ack()

    myiic.IIC1_Send_Byte(0x00)#write command
    myiic.IIC1_Wait_Ack()
    
    myiic.IIC1_Send_Byte(IIC_Command)
    myiic.IIC1_Wait_Ack()

    myiic.IIC1_Stop()
    
def Write_IIC_Data(IIC_Data):
    myiic.IIC1_Start()
    myiic.IIC1_Send_Byte(0x78)#D/C#=0; R/W#=0
    myiic.IIC1_Wait_Ack()

    myiic.IIC1_Send_Byte(0x40)#write data
    myiic.IIC1_Wait_Ack()
    myiic.IIC1_Send_Byte(IIC_Data)
    myiic.IIC1_Wait_Ack()
    myiic.IIC1_Stop()

def OLED_Init():
    delay(100)
    Write_IIC_Command(0xAE)#display off
    Write_IIC_Command(0x20)#Set Memory Addressing Mode
    Write_IIC_Command(0x10)#00,Horizontal Addressing Mode;01,Vertical Addressing Mode;10,Page Addressing Mode (RESET);11,Invalid
    Write_IIC_Command(0xb0)#Set Page Start Address for Page Addressing Mode,0-7
    Write_IIC_Command(0xc8)#Set COM Output Scan Direction
    Write_IIC_Command(0x00)#---set low column address
    Write_IIC_Command(0x10)#---set high column address
    Write_IIC_Command(0x40)#--set start line address
    Write_IIC_Command(0x81)#--set contrast control register
    Write_IIC_Command(0xff)#???? 0x00~0xff
    Write_IIC_Command(0xa1)#--set segment re-map 0 to 127
    Write_IIC_Command(0xa6)#--set normal display
    Write_IIC_Command(0xa8)#--set multiplex ratio(1 to 64)
    Write_IIC_Command(0x3F)#
    Write_IIC_Command(0xa4)#0xa4,Output follows RAM content;0xa5,Output ignores RAM content
    Write_IIC_Command(0xd3)#-set display offset
    Write_IIC_Command(0x00)#-not offset
    Write_IIC_Command(0xd5)#--set display clock divide ratio/oscillator frequency
    Write_IIC_Command(0xf0)#--set divide ratio
    Write_IIC_Command(0xd9)#--set pre-charge period
    Write_IIC_Command(0x22)#
    Write_IIC_Command(0xda)#--set com pins hardware configuration
    Write_IIC_Command(0x12)
    Write_IIC_Command(0xdb)#--set vcomh
    Write_IIC_Command(0x20)#0x20,0.77xVcc
    Write_IIC_Command(0x8d)#--set DC-DC enable
    Write_IIC_Command(0x14)#
    Write_IIC_Command(0xaf)#--turn on oled panel

def OLED_SetPos(x,y) :
    Write_IIC_Command(0xb0+y)
    Write_IIC_Command(((x&0xf0)>>4)|0x10)
    Write_IIC_Command((x&0x0f)|0x01)
    
def LED_CLS():
    m=0
    while m<8:
        Write_IIC_Command(0xb0+m)
        Write_IIC_Command(0x00)
        Write_IIC_Command(0x10)
        n=0
        while n<128:
            Write_IIC_Data(0x0);
            n=n+1
        m=m+1

#显示bmp位图
#x0：起始x坐标
#y0：起始y坐标
#x1：图片长
#y1：显示几行
#BMP：图片数据
def OLED_DrawBMP(x0,y0,x1,y1,BMP):
    j=0
    if y1%8==0:
        y = y1/8
    else:
        y = y1/8 + 1
    
    y=y0
    while y<y1:
        OLED_SetPos(x0,y)
        x=x0
        while x<x1:
            Write_IIC_Data((BMP[j]))
            j=j+1
            x=x+1
        y=y+1

#显示字符串
#x：起始x坐标
#y：第几行显示
#ch：要显示的字符串
def OLED_ShowStr(x, y, ch):
    c = 0
    i = 0
    chlen = len(ch)

    while i<chlen:
        c = oledfont.st.find(ch[i])
        if x > 120:
            x = 0
            y=y+2
        OLED_SetPos(x,y)
        j = 0
        while j<8:
            Write_IIC_Data(oledfont.F8X16[c*16+j])
            j=j+1
        OLED_SetPos(x,y+1)
        j=0
        while j<8:
            Write_IIC_Data(oledfont.F8X16[c*16+j+8]);
            j=j+1
        x += 8
        i=i+1

OLED_Init()#OLED初始化
LED_CLS()#清屏
#OLED_DrawBMP(0,0,120,8,oledfont.bmptest)#显示自定义图片
#OLED_ShowStr(0,0,"OLED")#显示字符串