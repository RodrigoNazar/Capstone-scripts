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
        MainWindow.resize(897, 727)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Titulo = QtWidgets.QLabel(self.centralwidget)
        self.Titulo.setGeometry(QtCore.QRect(270, 90, 361, 61))
        self.Titulo.setStyleSheet("font: 8pt \"Swis721 Blk BT\";\n"
                                  "color: rgb(170, 11, 11);")
        self.Titulo.setObjectName("Titulo")
        # self.consola = QtWidgets.QTextEdit(self.centralwidget)
        self.consola = QtWidgets.QLabel(self.centralwidget)
        self.consola.setGeometry(QtCore.QRect(210, 390, 511, 241))
        self.consola.setStyleSheet("border-color: rgb(0, 0, 0);\n"
                                   "background-color: rgb(200, 200, 200);"
                                   )
        self.consola.setObjectName("consola")
        self.conectarBoton = QtWidgets.QPushButton(self.centralwidget)
        self.conectarBoton.setGeometry(QtCore.QRect(350, 260, 191, 61))
        self.conectarBoton.setStyleSheet("background-color: rgb(0, 0, 127);\n"
                                         "font: 20pt \"Arial\";\n"
                                         "color: rgb(255, 255, 255);")
        self.conectarBoton.setObjectName("conectarBoton")
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
        self.conectarBoton.setText(_translate("MainWindow", "Conectar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
