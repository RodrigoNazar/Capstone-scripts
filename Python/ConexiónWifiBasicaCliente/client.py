import socket


def enviar_caracter(valor):
    IP_ESP = "172.20.10.9"
    ESP_PORT = 80

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((IP_ESP, ESP_PORT))

    valor = bytes([valor])
    # sock.sendall(f'{valor}')
    sock.sendall(valor)

    sock.close()


def calibrar():
    enviar_caracter(0)


def motor1(valor):

    enviar_caracter(1)
    enviar_caracter(valor)


def motor2(valor):

    enviar_caracter(2)
    enviar_caracter(valor)


def motor3(valor):

    enviar_caracter(3)
    enviar_caracter(valor)


def motor4(valor):

    enviar_caracter(4)
    enviar_caracter(valor)
