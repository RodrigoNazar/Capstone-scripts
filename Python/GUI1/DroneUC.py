from mainwindow import Ui_MainWindow
from PyQt5 import QtWidgets
from client import conectar_motores, test_motores, enviar_altura


class VentanaPrincipal(Ui_MainWindow):
    def setupVentana(self):
        self.botonMotores.clicked.connect(self.boton_motores)
        self.botonTest.clicked.connect(self.boton_test)
        self.botonAltura.clicked.connect(self.boton_altura)
        self.consola_text = ''
        self.motores_conectados = False

    def boton_motores(self):
        self.consola_text += '\nConectando motores...'
        self.actualizar_consola()
        conectar_motores()
        self.consola_text += '\tListo\n'
        self.motores_conectados = True
        self.actualizar_consola()

    def boton_altura(self):
        self.consola_text += '\nEnviando altura...'
        self.actualizar_consola()
        if self.boxAltura.text():
            enviar_altura(self.boxAltura.text())
            self.consola_text += '\tListo\n'
            self.motores_conectados = True
            self.actualizar_consola()
        else:
            self.consola_text += '\tNo ha ingresado una altura\n'
            self.actualizar_consola()

    def boton_test(self):
        if self.motores_conectados:
            self.consola_text += '\nEjecutando test...'
            self.actualizar_consola()
            test_motores()
            self.consola_text += '\tListo\n'
            self.actualizar_consola()
        else:
            self.consola_text += '\nMotores no conectados!\n'
            self.actualizar_consola()

    def actualizar_consola(self):
        self.consola.setText(self.consola_text)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = VentanaPrincipal()
    ui.setupUi(MainWindow)
    ui.setupVentana()
    MainWindow.show()
    sys.exit(app.exec_())
