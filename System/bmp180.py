import myiic
from pyb import delay

class bmp180:
    A=0
    C1=0
    AC2=0
    AC3=0
    AC4=0
    AC5=0
    AC6=0
    B1=0
    B2=0
    MB=0
    MC=0
    MD=0
    UT=0
    UP=0
    X1=0
    X2=0
    X3=0
    B3=0
    B4=0
    B5=0
    B6=0
    B7=0
    p=0
    Temp=0
    altitude=0.0

def BMP_WriteOneByte(WriteAddr,DataToWrite):
    myiic.IIC3_Start();
    myiic.IIC3_Send_Byte(0xEE);
    myiic.IIC3_Wait_Ack();
    myiic.IIC3_Send_Byte(WriteAddr);
    myiic.IIC3_Wait_Ack();
    myiic.IIC3_Send_Byte(DataToWrite);
    myiic.IIC3_Wait_Ack();
    myiic.IIC3_Stop();

def BMP_ReadOneByte(ReadAddr):
    data = 0;
    myiic.IIC3_Start();
    myiic.IIC3_Send_Byte(0xEE);
    myiic.IIC3_Wait_Ack();

    myiic.IIC3_Send_Byte(ReadAddr);
    myiic.IIC3_Wait_Ack();

    myiic.IIC3_Start();

    myiic.IIC3_Send_Byte(0xEF);
    myiic.IIC3_Wait_Ack();

    data = myiic.IIC3_Read_Byte(1);
    myiic.IIC3_Stop();

    return data;


def BMP_ReadTwoByte(ReadAddr):
    myiic.IIC3_Start();
    myiic.IIC3_Send_Byte(0xEE);
    myiic.IIC3_Wait_Ack();

    myiic.IIC3_Send_Byte(ReadAddr);
    myiic.IIC3_Wait_Ack();

    myiic.IIC3_Start();

    myiic.IIC3_Send_Byte(0xEF);
    myiic.IIC3_Wait_Ack();

    msb = myiic.IIC3_Read_Byte(1);
    lsb = myiic.IIC3_Read_Byte(0);

    myiic.IIC3_Stop();

    data = msb*256 + lsb;

    return data;


def BMP_ReadCalibrationData():
    bmp180.AC1 = BMP_ReadTwoByte(0xAA);
    bmp180.AC2 = BMP_ReadTwoByte(0xAC);
    bmp180.AC3 = BMP_ReadTwoByte(0xAE);
    bmp180.AC4 = BMP_ReadTwoByte(0xB0);
    bmp180.AC5 = BMP_ReadTwoByte(0xB2);
    bmp180.AC6 = BMP_ReadTwoByte(0xB4);
    bmp180.B1  = BMP_ReadTwoByte(0xB6);
    bmp180.B2  = BMP_ReadTwoByte(0xB8);
    bmp180.MB  = BMP_ReadTwoByte(0xBA);
    bmp180.MC  = BMP_ReadTwoByte(0xBC);
    bmp180.MD  = BMP_ReadTwoByte(0xBE);

    if bmp180.AC1>=32768:
        bmp180.AC1 -= 65535
    if bmp180.AC2>=32768:
        bmp180.AC2 -= 65535
    if bmp180.AC3>=32768:
        bmp180.AC3 -= 65535
    if bmp180.B1>=32768:
        bmp180.B1 -= 65535
    if bmp180.B2>=32768:
        bmp180.B2 -= 65535
    if bmp180.MB>=32768:
        bmp180.MB -= 65535
    if bmp180.MC>=32768:
        bmp180.MC -= 65535
    if bmp180.MD>=32768:
        bmp180.MD -= 65535
 
def BMP_Read_UT():
    BMP_WriteOneByte(0xF4,0x2E);
    delay(5);
    temp = BMP_ReadTwoByte(0xF6);
    return temp;


def BMP_Read_UP():
    BMP_WriteOneByte(0xF4,0x34);
    delay(5);
    pressure = BMP_ReadTwoByte(0xF6);
    #pressure = pressure + BMP_ReadOneByte(0xf8);
    pressure &= 0x0000FFFF;

    return pressure;


def BMP_UncompemstatedToTrue():
    bmp180.UT = BMP_Read_UT();
    bmp180.UT = BMP_Read_UT();
    bmp180.UP = BMP_Read_UP();

    bmp180.X1 = ((bmp180.UT - bmp180.AC6) * bmp180.AC5) >> 15;
    bmp180.X2 = int((bmp180.MC << 11) / (bmp180.X1 + bmp180.MD));
    bmp180.B5 = bmp180.X1 + bmp180.X2;
    bmp180.Temp  = (bmp180.B5 + 8) >> 4;

    bmp180.B6 = bmp180.B5 - 4000;
    bmp180.X1 = (bmp180.B2 * (bmp180.B6 * bmp180.B6 >> 12)) >> 11;
    bmp180.X2 = bmp180.AC2 * bmp180.B6 >> 11;
    bmp180.X3 = bmp180.X1 + bmp180.X2;

    bmp180.B3 = int(((bmp180.AC1 * 4 + bmp180.X3) + 2)/4);
    bmp180.X1 = (bmp180.AC3) * bmp180.B6 >> 13;
    bmp180.X2 = (bmp180.B1 *(bmp180.B6*bmp180.B6 >> 12)) >>16;
    bmp180.X3 = ((bmp180.X1 + bmp180.X2) + 2) >> 2;
    bmp180.B4 = bmp180.AC4 * int(bmp180.X3 + 32768) >> 15;
    bmp180.B7 = (int(bmp180.UP) - bmp180.B3) * 50000;
    

    if bmp180.B7 < 0x80000000:
        bmp180.p = int((bmp180.B7 * 2) / bmp180.B4);
    else:
        bmp180.p = int((bmp180.B7 / bmp180.B4) * 2);

    bmp180.X1 = (bmp180.p >> 8) * (bmp180.p >>8);
    bmp180.X1 = ((bmp180.X1) * 3038) >> 16;
    bmp180.X2 = (-7357 * bmp180.p) >> 16;

    bmp180.p = bmp180.p + ((bmp180.X1 + bmp180.X2 + 3791) >> 4);

    bmp180.altitude = 44330 * (1-pow(((bmp180.p) / 101325.0),(1.0/5.255)));


BMP_ReadCalibrationData()
ID = BMP_ReadOneByte(0xD0)
'''
while True:
    BMP_UncompemstatedToTrue();
    #print("ID = %d temp = %ld.%ldC Pressure = %ldPa Altitude = %.5fm\r\n", ID, bmp180.Temp/10, bmp180.Temp%10, bmp180.p, bmp180.altitude);
    print("ID={} temp={}°C pressure={}Pa Altitude={}m".format(ID,bmp180.Temp/10,bmp180.p*10,bmp180.altitude))
    delay(1000);
'''