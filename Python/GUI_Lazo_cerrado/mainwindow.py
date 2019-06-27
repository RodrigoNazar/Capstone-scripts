# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DroneUC.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 883)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 490, 931, 111))
        self.label.setStyleSheet("background-color: rgb(0, 0, 127);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.Boton_calibracion = QtWidgets.QPushButton(self.centralwidget)
        self.Boton_calibracion.setGeometry(QtCore.QRect(250, 250, 191, 51))
        self.Boton_calibracion.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.Boton_calibracion.setObjectName("Boton_calibracion")
        self.Titulo = QtWidgets.QLabel(self.centralwidget)
        self.Titulo.setGeometry(QtCore.QRect(390, 100, 361, 61))
        self.Titulo.setStyleSheet("font: 8pt \"Swis721 Blk BT\";\n"
"color: rgb(170, 11, 11);")
        self.Titulo.setObjectName("Titulo")
        self.Boton_apagar = QtWidgets.QPushButton(self.centralwidget)
        self.Boton_apagar.setGeometry(QtCore.QRect(670, 250, 191, 51))
        self.Boton_apagar.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.Boton_apagar.setObjectName("Boton_apagar")
        self.Consola = QtWidgets.QLabel(self.centralwidget)
        self.Consola.setGeometry(QtCore.QRect(90, 750, 911, 61))
        self.Consola.setText("")
        self.Consola.setObjectName("Consola")
        self.Texto_Kp = QtWidgets.QLineEdit(self.centralwidget)
        self.Texto_Kp.setGeometry(QtCore.QRect(140, 530, 113, 22))
        self.Texto_Kp.setObjectName("Texto_Kp")
        self.Texto_Ki = QtWidgets.QLineEdit(self.centralwidget)
        self.Texto_Ki.setGeometry(QtCore.QRect(330, 530, 113, 22))
        self.Texto_Ki.setObjectName("Texto_Ki")
        self.Texto_Kd = QtWidgets.QLineEdit(self.centralwidget)
        self.Texto_Kd.setGeometry(QtCore.QRect(530, 530, 113, 22))
        self.Texto_Kd.setObjectName("Texto_Kd")
        self.Texto_Altura = QtWidgets.QLineEdit(self.centralwidget)
        self.Texto_Altura.setGeometry(QtCore.QRect(830, 530, 121, 22))
        self.Texto_Altura.setObjectName("Texto_Altura")
        self.Boton_Kp = QtWidgets.QPushButton(self.centralwidget)
        self.Boton_Kp.setGeometry(QtCore.QRect(140, 630, 111, 41))
        self.Boton_Kp.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.Boton_Kp.setObjectName("Boton_Kp")
        self.Boton_Ki = QtWidgets.QPushButton(self.centralwidget)
        self.Boton_Ki.setGeometry(QtCore.QRect(330, 630, 111, 41))
        self.Boton_Ki.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.Boton_Ki.setObjectName("Boton_Ki")
        self.Boton_Kd = QtWidgets.QPushButton(self.centralwidget)
        self.Boton_Kd.setGeometry(QtCore.QRect(530, 630, 111, 41))
        self.Boton_Kd.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.Boton_Kd.setObjectName("Boton_Kd")
        self.Boton_altura = QtWidgets.QPushButton(self.centralwidget)
        self.Boton_altura.setGeometry(QtCore.QRect(840, 630, 111, 41))
        self.Boton_altura.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.Boton_altura.setObjectName("Boton_altura")
        self.Titulo_5 = QtWidgets.QLabel(self.centralwidget)
        self.Titulo_5.setGeometry(QtCore.QRect(810, 400, 161, 61))
        self.Titulo_5.setStyleSheet("font: 8pt \"Swis721 Blk BT\";\n"
"color: rgb(170, 11, 11);")
        self.Titulo_5.setObjectName("Titulo_5")
        self.Titulo_6 = QtWidgets.QLabel(self.centralwidget)
        self.Titulo_6.setGeometry(QtCore.QRect(510, 400, 161, 61))
        self.Titulo_6.setStyleSheet("font: 8pt \"Swis721 Blk BT\";\n"
"color: rgb(170, 11, 11);")
        self.Titulo_6.setObjectName("Titulo_6")
        self.Titulo_7 = QtWidgets.QLabel(self.centralwidget)
        self.Titulo_7.setGeometry(QtCore.QRect(310, 400, 161, 61))
        self.Titulo_7.setStyleSheet("font: 8pt \"Swis721 Blk BT\";\n"
"color: rgb(170, 11, 11);")
        self.Titulo_7.setObjectName("Titulo_7")
        self.Titulo_8 = QtWidgets.QLabel(self.centralwidget)
        self.Titulo_8.setGeometry(QtCore.QRect(110, 400, 161, 71))
        self.Titulo_8.setStyleSheet("font: 8pt \"Swis721 Blk BT\";\n"
"color: rgb(170, 11, 11);")
        self.Titulo_8.setObjectName("Titulo_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Boton_calibracion.setText(_translate("MainWindow", "Calibración"))
        self.Titulo.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt;\">DRONE UC</span></p></body></html>"))
        self.Boton_apagar.setText(_translate("MainWindow", "Apagar Motores"))
        self.Boton_Kp.setText(_translate("MainWindow", "Enviar Kp"))
        self.Boton_Ki.setText(_translate("MainWindow", "Enviar Ki"))
        self.Boton_Kd.setText(_translate("MainWindow", "Enviar Kd"))
        self.Boton_altura.setText(_translate("MainWindow", "Enviar Altura"))
        self.Titulo_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Referencia</span></p><p align=\"center\"><span style=\" font-size:14pt;\">de Altura</span></p></body></html>"))
        self.Titulo_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Cambio</span></p><p align=\"center\"><span style=\" font-size:14pt;\">de Kd</span></p></body></html>"))
        self.Titulo_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Cambio</span></p><p align=\"center\"><span style=\" font-size:14pt;\">de Ki</span></p></body></html>"))
        self.Titulo_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Cambio</span></p><p align=\"center\"><span style=\" font-size:14pt;\">de Kp</span></p></body></html>"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
