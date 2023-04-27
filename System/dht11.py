from pyb import Pin,delay
import dht

d = dht.DHT11(Pin('G15'))
'''
while True:
    d.measure()
    print("temperature:{}°C,humidity:{}%".format(d.temperature(),d.humidity()))
    delay(1200)
'''