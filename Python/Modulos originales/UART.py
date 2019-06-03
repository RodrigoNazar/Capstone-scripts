from machine import UART
from time import sleep

uart = UART(0)                         # init with given baudrate
uart.init(57600, bits=8, parity=None, stop=1)  # init with given parameters

uart1 = UART(1)                         # init with given baudrate
uart1.init(57600, bits=8, parity=None, stop=1)  # init with given parameters

while 1:
    uart.write('a')   # write the 3 characters
    uart1.write('b')   # write the 3 characters
    sleep(.1)
