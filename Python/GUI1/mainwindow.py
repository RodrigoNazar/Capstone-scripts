# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DroneUc.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(897, 727)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Titulo = QtWidgets.QLabel(self.centralwidget)
        self.Titulo.setGeometry(QtCore.QRect(270, 90, 361, 61))
        self.Titulo.setStyleSheet("font: 8pt \"Swis721 Blk BT\";\n"
                                  "color: rgb(170, 11, 11);")
        self.Titulo.setObjectName("Titulo")
        self.consola = QtWidgets.QTextEdit(self.centralwidget)
        self.consola.setGeometry(QtCore.QRect(210, 390, 511, 241))
        self.consola.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.consola.setObjectName("consola")
        self.botonAltura = QtWidgets.QPushButton(self.centralwidget)
        self.botonAltura.setGeometry(QtCore.QRect(370, 280, 191, 61))
        self.botonAltura.setStyleSheet("background-color: rgb(0, 0, 127);\n"
                                       "font: 20pt \"Arial\";\n"
                                       "color: rgb(255, 255, 255);")
        self.botonAltura.setObjectName("botonAltura")
        self.boxAltura = QtWidgets.QLineEdit(self.centralwidget)
        self.boxAltura.setGeometry(QtCore.QRect(410, 230, 141, 31))
        self.boxAltura.setText("")
        self.boxAltura.setObjectName("boxAltura")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(350, 240, 55, 16))
        self.label.setObjectName("label")
        self.botonMotores = QtWidgets.QPushButton(self.centralwidget)
        self.botonMotores.setGeometry(QtCore.QRect(130, 280, 191, 61))
        self.botonMotores.setStyleSheet("background-color: rgb(0, 0, 127);\n"
                                        "font: 12pt \"Arial\";\n"
                                        "color: rgb(255, 255, 255);")
        self.botonMotores.setObjectName("botonMotores")
        self.botonTest = QtWidgets.QPushButton(self.centralwidget)
        self.botonTest.setGeometry(QtCore.QRect(610, 280, 191, 61))
        self.botonTest.setStyleSheet("background-color: rgb(0, 0, 127);\n"
                                     "font: 10pt \"Arial\";\n"
                                     "color: rgb(255, 255, 255);")
        self.botonTest.setObjectName("botonTest")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Titulo.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:36pt;\">DRONE UC</span></p></body></html>"))
        self.botonAltura.setText(_translate("MainWindow", "Enviar"))
        self.label.setText(_translate("MainWindow", "Altura:"))
        self.botonMotores.setText(_translate("MainWindow", "Conectar Motores"))
        self.botonTest.setText(_translate(
            "MainWindow", "Ejecutar test de motores"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
