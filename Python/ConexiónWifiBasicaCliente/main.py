# from server import set_up_server
import socket

addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)

print('\n\nlistening on', addr)

while True:
    cl, addr = s.accept()
    # print('Client connected from', addr)
    data = cl.recv(1024).decode('ascii')
    print('Data collected:', data)
    # cl.sendall(data)
    cl.close()
