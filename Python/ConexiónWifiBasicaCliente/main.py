import socket
from machine import freq, UART

freq(160000000)

uart = UART(0)                                  # init with given baudrate
uart.init(57600, bits=8, parity=None, stop=1)   # init with given parameters

uart1 = UART(1)                                 # init with given baudrate
uart1.init(57600, bits=8, parity=None, stop=1)  # init with given parameters

addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)

micro1 = False
micro2 = False

while True:
    cl, addr = s.accept()
    data = cl.recv(1024)

    '''
    Envío la información al respectivo micro
    '''

    if micro1:
        uart.write(data)
        micro1 = False
    elif micro2:
        uart1.write(data)
        micro2 = False

    '''
    Si recibo un valor como 0, 1, 2, 3, 4, prendo los respectivos flags
    '''
    if data == b'\x01' or data == b'\x02':
        uart.write(data)
        micro1 = True
    elif data == b'\x03' or data == b'\x04':
        uart1.write(data)
        micro2 = True
    elif data == b'\x00':
        uart.write(data)
        uart1.write(data)

    cl.close()
