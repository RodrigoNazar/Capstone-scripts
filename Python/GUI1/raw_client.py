import socket


def enviar_caracter(valor):
    IP_ESP = "172.20.10.9"
    ESP_PORT = 80

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((IP_ESP, ESP_PORT))

    sock.sendall(f'{valor}'.encode('ascii'))

    sock.close()
