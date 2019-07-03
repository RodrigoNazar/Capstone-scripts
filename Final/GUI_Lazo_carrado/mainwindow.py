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
        MainWindow.resize(1100, 510)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Titulo = QtWidgets.QLabel(self.centralwidget)
        self.Titulo.setGeometry(QtCore.QRect(390, 100, 361, 61))
        self.Titulo.setStyleSheet("font: 8pt \"Swis721 Blk BT\";\n"
"color: rgb(170, 11, 11);")
        self.Titulo.setObjectName("Titulo")
        self.Boton_apagar = QtWidgets.QPushButton(self.centralwidget)
        self.Boton_apagar.setGeometry(QtCore.QRect(470, 250, 191, 51))
        self.Boton_apagar.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.Boton_apagar.setObjectName("Boton_apagar")
        self.Consola = QtWidgets.QLabel(self.centralwidget)
        self.Consola.setGeometry(QtCore.QRect(90, 390, 911, 61))
        self.Consola.setText("")
        self.Consola.setObjectName("Consola")
        self.Boton_Subir_Potencia = QtWidgets.QPushButton(self.centralwidget)
        self.Boton_Subir_Potencia.setGeometry(QtCore.QRect(190, 240, 201, 41))
        self.Boton_Subir_Potencia.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.Boton_Subir_Potencia.setObjectName("Boton_Subir_Potencia")
        self.Boton_Bajar_Potencia = QtWidgets.QPushButton(self.centralwidget)
        self.Boton_Bajar_Potencia.setGeometry(QtCore.QRect(190, 310, 201, 41))
        self.Boton_Bajar_Potencia.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.Boton_Bajar_Potencia.setObjectName("Boton_Bajar_Potencia")
        self.Boton_Subir_Ref = QtWidgets.QPushButton(self.centralwidget)
        self.Boton_Subir_Ref.setGeometry(QtCore.QRect(740, 240, 201, 41))
        self.Boton_Subir_Ref.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.Boton_Subir_Ref.setObjectName("Boton_Subir_Ref")
        self.Boton_Bajar_Ref = QtWidgets.QPushButton(self.centralwidget)
        self.Boton_Bajar_Ref.setGeometry(QtCore.QRect(740, 310, 201, 41))
        self.Boton_Bajar_Ref.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.Boton_Bajar_Ref.setObjectName("Boton_Bajar_Ref")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Titulo.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt;\">DRONE UC</span></p></body></html>"))
        self.Boton_apagar.setText(_translate("MainWindow", "Apagar Motores"))
        self.Boton_Subir_Potencia.setText(_translate("MainWindow", "Subir Potencia"))
        self.Boton_Bajar_Potencia.setText(_translate("MainWindow", "Bajar Potencia"))
        self.Boton_Subir_Ref.setText(_translate("MainWindow", "Subir Referencia"))
        self.Boton_Bajar_Ref.setText(_translate("MainWindow", "Bajar Referencia"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
