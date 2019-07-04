from mainwindow import Ui_MainWindow
from PyQt5 import QtWidgets
from client import (apagar_motores,
                    c_subir_potencia,
                    c_bajar_potencia,
                    c_subir_ref,
                    c_bajar_ref)


class VentanaPrincipal(Ui_MainWindow):
    def setupVentana(self):
        self.Boton_apagar.clicked.connect(self.boton_apagar_motores)
        self.Boton_Subir_Potencia.clicked.connect(self.subir_potencia)
        self.Boton_Bajar_Potencia.clicked.connect(self.bajar_potencia)
        self.Boton_Subir_Ref.clicked.connect(self.subir_ref)
        self.Boton_Bajar_Ref.clicked.connect(self.bajar_ref)
        self.potencia = 140
        self.referencia = 5
        self.consola_text = ''

    def boton_apagar_motores(self):
        self.consola_text += '\nApagando motores...'
        self.actualizar_consola()
        apagar_motores()
        self.consola_text += '\tListo...\n'
        self.actualizar_consola()

    def subir_potencia(self):
        self.consola_text += '\nSubiendo potencia...'
        self.actualizar_consola()
        self.potencia += 1 if self.potencia < 190 else 0
        self.consola_text += '\nNueva potencia = ' + str(self.potencia)
        self.actualizar_consola()
        if self.potencia < 190:
            c_subir_potencia()
        self.consola_text += '\tListo\n'
        self.actualizar_consola()

    def subir_ref(self):
        self.consola_text += '\nSubiendo referencia...'
        self.actualizar_consola()
        self.referencia += 10 if self.referencia < 120 else 0
        self.consola_text += '\nNueva referencia = ' + str(self.referencia) + ' cm'
        self.actualizar_consola()
        if self.referencia < 120:
            c_subir_ref()
        self.consola_text += '\tListo\n'
        self.actualizar_consola()

    def bajar_potencia(self):
        self.consola_text += '\nBajando potencia...'
        self.actualizar_consola()
        self.potencia -= 1 if self.potencia > 42 else 0
        self.consola_text += '\nNueva potencia = ' + str(self.potencia)
        self.actualizar_consola()
        if self.potencia > 42:
            c_bajar_potencia()
        self.consola_text += '\tListo\n'
        self.actualizar_consola()

    def bajar_ref(self):
        self.consola_text += '\nBajando referencia...'
        self.actualizar_consola()
        self.referencia -= 10 if self.referencia > 20 else 0
        self.consola_text += '\nNueva referencia = ' + str(self.referencia) + ' cm'
        self.actualizar_consola()
        if self.referencia > 20:
            c_bajar_ref()
        self.consola_text += '\tListo\n'
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
