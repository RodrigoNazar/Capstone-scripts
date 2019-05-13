import socket


def conectarESP():

    IP_ESP = "192.168.4.1"
    ESP_PORT = 80

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((IP_ESP, ESP_PORT))

    sock.sendall('Hola mundo\n\n\n'.encode('ascii'))

    sock.close()
