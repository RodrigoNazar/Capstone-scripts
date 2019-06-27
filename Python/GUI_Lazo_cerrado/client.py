import socket


def enviar_caracter(valor):
    # IP_ESP = "192.168.43.9"
    IP_ESP = "172.20.10.9"
    ESP_PORT = 80

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((IP_ESP, ESP_PORT))

    valor = bytes([valor])
    sock.sendall(valor)

    sock.close()


def calibrar():
    enviar_caracter(0)


def apagar_motores():
    enviar_caracter(7)
    enviar_caracter(42)


def enviar_kp(kp):
    # enviar_caracter(7)
    enviar_caracter(kp)


def enviar_ki(ki):
    # enviar_caracter(7)
    enviar_caracter(ki)


def enviar_kd(kd):
    # enviar_caracter(7)
    enviar_caracter(kd)


def enviar_altura(altura):
    # enviar_caracter()
    enviar_caracter(altura)
