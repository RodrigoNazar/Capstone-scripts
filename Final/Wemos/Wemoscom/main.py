import socket
from machine import freq, Pin
import utime

freq(160000000)

d3 = Pin(0, Pin.OUT)  # D3
d5 = Pin(14, Pin.OUT)  # D5
d6 = Pin(12, Pin.OUT)  # D6
d7 = Pin(13, Pin.OUT)  # D7
d8 = Pin(15, Pin.OUT)  # D8

d3.value(0)
d5.value(0)
d6.value(0)
d7.value(0)
d8.value(0)

addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)

print('\nEscuchando...')


while True:
    cl, addr = s.accept()
    data = cl.recv(1024).decode('ascii')

    print(data)

    if data == '1':
        d3.value(1)
        utime.sleep_us(10)
        print('1')
        d3.value(0)
    elif data == '2':
        d5.value(1)
        utime.sleep_us(10)
        print('2')
        d5.value(0)
    elif data == '3':
        d6.value(1)
        utime.sleep_us(10)
        print('3')
        d6.value(0)
    elif data == '4':
        d7.value(1)
        utime.sleep_us(10)
        print('4')
        d7.value(0)
    elif data == '5':
        d8.value(1)
        utime.sleep_us(10)
        print('5')
        d8.value(0)

    cl.close()
