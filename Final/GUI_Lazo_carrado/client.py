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


def apagar_motores():
    enviar_caracter(42)


def c_subir_potencia():
    enviar_caracter()


def c_bajar_potencia(ki):
    enviar_caracter()


def c_subir_ref(kd):
    enviar_caracter()


def c_bajar_ref(altura):
    enviar_caracter()
