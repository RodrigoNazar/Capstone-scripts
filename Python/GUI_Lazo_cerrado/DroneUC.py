from mainwindow import Ui_MainWindow
from PyQt5 import QtWidgets
from client import (calibrar, apagar_motores, enviar_kp,
                    enviar_ki, enviar_kd, enviar_altura)


class VentanaPrincipal(Ui_MainWindow):
    def setupVentana(self):
        self.Boton_calibracion.clicked.connect(self.boton_calibrado)
        self.Boton_apagar.clicked.connect(self.boton_apagar_motores)
        self.Boton_Kp.clicked.connect(self.boton_enviar_kp)
        self.Boton_Ki.clicked.connect(self.boton_enviar_ki)
        self.Boton_Kd.clicked.connect(self.boton_enviar_kd)
        self.Boton_altura.clicked.connect(self.boton_enviar_altura)

        self.consola_text = ''

    def boton_calibrado(self):
        self.consola_text += '\nCalibrando motores...'
        self.actualizar_consola()
        calibrar()
        self.consola_text += '\tListo\n'
        self.actualizar_consola()

    def boton_apagar_motores(self):
        self.consola_text += '\nApagando motores...'
        self.actualizar_consola()
        apagar_motores()
        self.consola_text += '\tListo...\n'
        self.actualizar_consola()

    def boton_enviar_kp(self):
        kp = self.Texto_Kp.text()
        self.consola_text += '\nEnviando Kp...'
        self.actualizar_consola()
        enviar_kp(kp)
        self.consola_text += '\tListo\n'
        self.actualizar_consola()

    def boton_enviar_kd(self):
        kd = self.Texto_Kd.text()
        self.consola_text += '\nEnviando Kd...'
        self.actualizar_consola()
        enviar_kd(kd)
        self.consola_text += '\tListo\n'
        self.actualizar_consola()

    def boton_enviar_ki(self):
        ki = self.Texto_Ki.text()
        self.consola_text += '\nEnviando Ki...'
        self.actualizar_consola()
        enviar_ki(ki)
        self.consola_text += '\tListo\n'
        self.actualizar_consola()

    def boton_enviar_altura(self):
        altura = self.Texto_Altura.text()
        self.consola_text += '\nEnviando Altura...'
        self.actualizar_consola()
        enviar_altura(altura)
        self.consola_text += '\tListo\n'
        self.actualizar_consola()
        pass

    def actualizar_consola(self):
        self.Consola.setText(self.consola_text)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = VentanaPrincipal()
    ui.setupUi(MainWindow)
    ui.setupVentana()
    MainWindow.show()
    sys.exit(app.exec_())
