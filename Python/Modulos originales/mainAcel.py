from machine import Pin, I2C
import new_ADXL345 as ADXL345
import time

i2c = I2C(scl=Pin(5, Pin.PULL_UP), sda=Pin(4, Pin.PULL_UP), freq=10000)
adx = ADXL345.ADXL345(i2c)

while True:
    x = adx.xValue
    y = adx.yValue
    z = adx.zValue
    print('The acceleration info of x, y, z are:%d,%d,%d' % (x, y, z))
    time.sleep_ms(50)
