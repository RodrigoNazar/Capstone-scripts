# from server import set_up_server
import socket
import network


ap_if = network.WLAN(network.AP_IF)
ap_if.config(essid='DroneUC', authmode=network.AUTH_WPA_WPA2_PSK,
             password="droneucconnect")

print('\n\nDireccion IP:', ap_if.ifconfig()[0])

# Do not use this code in real projects! Read
# http_server_simplistic_commented.py for details.
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)

print('\n\nlistening on', addr)

while True:
    cl, addr = s.accept()
    print('Client connected from', addr)
    data = cl.recv(1024).decode('ascii')
    print('Data collected:', data)
    # cl.sendall(data)
    cl.close()
