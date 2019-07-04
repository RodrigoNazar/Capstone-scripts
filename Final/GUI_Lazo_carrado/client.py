import socket


def enviar_caracter(valor):
    # IP_ESP = "192.168.43.9"
    # IP_ESP = "172.20.10.9"

    # IP_ESP = "255.255.255.240"
    # IP_ESP = "172.20.10.1"

    IP_ESP = "172.20.10.12"
    ESP_PORT = 80

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((IP_ESP, ESP_PORT))

    # valor = bytes([valor])
    sock.sendall(valor.encode('ascii'))

    sock.close()


def apagar_motores():
    enviar_caracter('1')


def c_subir_potencia():
    enviar_caracter('2')


def c_bajar_potencia():
    enviar_caracter('3')


def c_subir_ref():
    enviar_caracter('4')


def c_bajar_ref():
    enviar_caracter('5')
