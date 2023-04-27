from pyb import delay,Pin

FLAME=Pin('F2',Pin.IN, Pin.PULL_UP)#火焰设为输入
FOG=Pin('F3',Pin.IN, Pin.PULL_UP)#可燃气体设为输入
PY=Pin('F7',Pin.IN, Pin.PULL_UP)#人体设为输入
HALL=Pin('F8',Pin.IN, Pin.PULL_UP)#霍尔设为输入
SW=Pin('F10',Pin.IN, Pin.PULL_UP)#震动设为输入
RELAY=Pin('F9',Pin.OUT_PP)#继电器设为输出

'''
while True:
    flame = FLAME.value()
    fog = FOG.value()
    py = PY.value()
    hall = HALL.value()
    sw = SW.value()
    
    if fog == 1:
        print("fog normal");
    else:
        print("fog warning");

    if flame == 1:
        print("flame normal");
    else:
        print("flame warning");
          
    if sw == 1:
        print("shack normal");
    else:
        print("shack warning");

    if py == 1:
        print("no one is here");
    else:
        print("someone's here");

    if hall == 1:
        print("no magnets\r\n");
    else:
        print("there are magnets\r\n");

    #如果有一个传感器发出警报，则打开继电器；否则关闭继电器
    flag = fog&flame&sw&py&hall
    if flag==0:
        RELAY.high()
    else:
        RELAY.low()

    delay(1000)
'''