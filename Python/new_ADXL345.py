from machine import Pin, I2C
import math
import time

'''
Constantes
'''

device = const(0x53)
regAddress = const(0x32)
TO_READ = 6
buff = bytearray(6)
POWER_CTL = 0x2D
DATA_FORMAT = 0x31


class ADXL345:
    def __init__(self, i2c, addr=device):
        self.addr = addr
        self.i2c = i2c

        b = bytearray(1)

        # Poner el ADX345 en +- 4G
        b[0] = 1
        self.i2c.writeto_mem(self.addr, DATA_FORMAT, b)

        # Poner el ADX345 Power-saving features control
        b[0] = 8
        self.i2c.writeto_mem(self.addr, POWER_CTL, b)

    @property
    def xValue(self):
        buff = self.i2c.readfrom_mem(self.addr, regAddress, TO_READ)
        x = (int(buff[1]) << 8) | buff[0]
        if x > 32767:
            x -= 65536
        return x

    @property
    def yValue(self):
        buff = self.i2c.readfrom_mem(self.addr, regAddress, TO_READ)
        y = (int(buff[3]) << 8) | buff[2]
        if y > 32767:
            y -= 65536
        return y

    @property
    def zValue(self):
        buff = self.i2c.readfrom_mem(self.addr, regAddress, TO_READ)
        z = (int(buff[5]) << 8) | buff[4]
        if z > 32767:
            z -= 65536
        return z
