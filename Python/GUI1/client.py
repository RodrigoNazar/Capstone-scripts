import socket


def conectar_motores():

    IP_ESP = "172.20.10.9"
    ESP_PORT = 80

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((IP_ESP, ESP_PORT))

    sock.sendall('Conecta motores!\n\n\n'.encode('ascii'))

    sock.close()


def enviar_altura(altura):
    IP_ESP = "172.20.10.9"
    ESP_PORT = 80

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((IP_ESP, ESP_PORT))

    sock.sendall(f'Nueva altura: {altura}\n\n\n'.encode('ascii'))

    sock.close()


def test_motores():
    IP_ESP = "172.20.10.9"
    ESP_PORT = 80

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((IP_ESP, ESP_PORT))

    sock.sendall(f'Realiza test de motores!\n\n\n'.encode('ascii'))

    sock.close()
