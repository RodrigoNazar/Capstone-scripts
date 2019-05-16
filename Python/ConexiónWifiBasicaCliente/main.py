# from server import set_up_server
import socket
from motores import Motores
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)

motores = Motores()

while True:
    cl, addr = s.accept()
    data = cl.recv(1024).decode('ascii')
    if data == '1':
        motores.increase_duty_all()
    elif data == '0':
        motores.decrease_duty_all()
    cl.close()
