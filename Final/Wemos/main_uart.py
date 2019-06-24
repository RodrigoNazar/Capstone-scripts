import socket
from machine import freq, UART

freq(160000000)

uart = UART(0)                                  # init with given baudrate
uart.init(57600, bits=8, parity=None, stop=1)   # init with given parameters

addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)


while True:
    cl, addr = s.accept()
    data = cl.recv(1024)

    '''
    Si recibo un valor como 0, 1, 2, 3, 4, prendo los respectivos flags
    '''

    uart.write(data)

    cl.close()
