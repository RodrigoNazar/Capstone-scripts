from mainwindow import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from client import conectarESP


class VentanaPrincipal(Ui_MainWindow):
    def setupVentana(self):
        self.conectarBoton.clicked.connect(self.boton_clickeado)
        self.consola_text = ''

    def boton_clickeado(self):
        self.consola_text += '\nConectando con el Dron'
        self.actualizar_consola()
        conectarESP()
        self.consola_text += '\nConexión terminada\n'
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
