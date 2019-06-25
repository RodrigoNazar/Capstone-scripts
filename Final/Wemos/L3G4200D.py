from machine import Pin, I2C
import math
import time

device = const(0x69)
TO_READ = 6
buff = bytearray(6)


class Giroscopio:
    def __init__(self, i2c, addr=device):
        self.addr = addr
        self.i2c = i2c
        b = bytearray(1)
        b[0] = 15
        self.i2c.writeto_mem(self.addr, 0x20, b)
        b[0] = 48
        self.i2c.writeto_mem(self.addr, 0x23, b)

    @property
    def xValue(self):
        xMSB = self.i2c.readfrom_mem(self.addr, 0x29, TO_READ)
        xLSB = self.i2c.readfrom_mem(self.addr, 0x28, TO_READ)
        x = (int(xMSB) << 8) | xLSB
        if x > 32767:
            x -= 65536
        return x

    @property
    def yValue(self):
        yMSB = self.i2c.readfrom_mem(self.addr, 0x2B, TO_READ)
        yLSB = self.i2c.readfrom_mem(self.addr, 0x2A, TO_READ)
        y = (int(yMSB) << 8) | yLSB
        if y > 32767:
            y -= 65536
        return y

    @property
    def zValue(self):
        zMSB = self.i2c.readfrom_mem(self.addr, 0x2D, TO_READ)
        zLSB = self.i2c.readfrom_mem(self.addr, 0x2C, TO_READ)
        z = (int(zMSB) << 8) | zLSB
        if z > 32767:
            z -= 65536
        return z

    def RP_calculate(self, x, y, z):
        roll = math.atan2(y, z) * 57.3
        pitch = math.atan2((- x), math.sqrt(y * y + z * z)) * 57.3
        return roll, pitch
