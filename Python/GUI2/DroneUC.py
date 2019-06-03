from mainwindow import Ui_MainWindow
from PyQt5 import QtWidgets
from client import (calibrar, motor1, motor2, motor3,
                    motor4, apagar_motores, mover_motores)


class VentanaPrincipal(Ui_MainWindow):
    def setupVentana(self):
        self.Boton_calibracion.clicked.connect(self.boton_calibrado)
        self.Boton_apagar.clicked.connect(self.boton_apagar_motores)
        self.motor1_slide.valueChanged.connect(self.cambio_slide_m1)
        self.motor2_slide.valueChanged.connect(self.cambio_slide_m2)
        self.motor3_slide.valueChanged.connect(self.cambio_slide_m3)
        self.motor4_slide.valueChanged.connect(self.cambio_slide_m4)
        self.motores_slide.valueChanged.connect(self.cambio_slide_motores)
        self.consola_text = ''
        self.motores_conectados = False

    def cambio_slide_m1(self):
        motor1(self.motor1_slide.value())
        # print('Valor motor 1:', self.motor1_slide.value())

    def cambio_slide_m2(self):
        motor2(self.motor2_slide.value())
        # print('Valor motor 2:', self.motor2_slide.value())

    def cambio_slide_m3(self):
        motor3(self.motor3_slide.value())
        # print('Valor motor 3:', self.motor3_slide.value())

    def cambio_slide_m4(self):
        motor4(self.motor4_slide.value())
        # print('Valor motor 4:', self.motor4_slide.value())

    def cambio_slide_motores(self):
        self.motor1_slide.setValue(self.motores_slide.value())
        self.motor3_slide.setValue(self.motores_slide.value())
        self.motor2_slide.setValue(self.motores_slide.value())
        self.motor4_slide.setValue(self.motores_slide.value())

        mover_motores(self.motores_slide.value())
        # print('Valor motores:', self.motores_slide.value())

    def boton_calibrado(self):
        self.consola_text += '\nCalibrando motores...'
        self.actualizar_consola()
        calibrar()
        self.consola_text += '\tListo\n'
        self.motores_conectados = True
        self.actualizar_consola()

    def boton_apagar_motores(self):
        self.consola_text += '\nApagando motores...'
        self.actualizar_consola()
        apagar_motores()
        self.consola_text += '\tListo...\n'
        self.actualizar_consola()

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
