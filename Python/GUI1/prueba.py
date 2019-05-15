from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton, QScrollArea, QApplication, QMainWindow
from PyQt5.QtCore import Qt


class VentanaChat(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Señales
        # self.servidor_signal = servidor_signal
        # self.terminar_conexion_signal = terminar_conexion_signal

        # Log
        self.chat_log = ""

        # instancias de UI
        self.setWindowTitle("DCChat")
        self.setGeometry(400, 200, 640, 480)

        self.label_titulo = QLabel("DCChat", self)
        label_titulo_font = self.label_titulo.font()
        label_titulo_font.setBold(True)
        label_titulo_font.setPointSize(48)
        self.label_titulo.setFont(label_titulo_font)
        self.label_titulo.setStyleSheet("color: darkblue")

        self.chat_log_label = QLabel("", self)
        chat_log_label_font = self.chat_log_label.font()
        chat_log_label_font.setPointSize(12)
        self.chat_log_label.setFont(chat_log_label_font)
        self.chat_log_label.setStyleSheet("color: darkblue")

        self.users_scroll = QScrollArea(self)
        self.users_scroll.setWidgetResizable(True)
        self.users_scroll.setStyleSheet("background-color: transparent")

        self.usuario_line_edit = QLineEdit("", self)
        usuario_line_edit_font = self.usuario_line_edit.font()
        usuario_line_edit_font.setPointSize(12)
        self.usuario_line_edit.setFont(usuario_line_edit_font)
        self.usuario_line_edit.setStyleSheet("color: darkblue")

        self.boton_usuario = QPushButton("\t\tEnviar\t\t", self)
        boton_usuario_font = self.boton_usuario.font()
        boton_usuario_font.setBold(True)
        boton_usuario_font.setPointSize(12)
        self.boton_usuario.setFont(boton_usuario_font)
        self.boton_usuario.setStyleSheet(
            "QPushButton{color: darkblue; background: transparent; border: 2px solid darkblue; border-radius: 8px}"
            "QPushButton:pressed{color: #fcf7e3; background-color: darkblue}")
        self.boton_usuario.clicked.connect(self.manejo_boton)

        # Alineación de UI
        self.init_setUp()

    def init_setUp(self):

        self.label_titulo.setGeometry(250, 20, 100, 50)
        self.chat_log_label.setGeometry(90, 80, 300, 300)
        self.users_scroll.setWidget(self.chat_log_label)
        self.users_scroll.setGeometry(90, 80, 300, 300)
        self.chat_log_label.setAlignment(Qt.AlignTop)
        self.usuario_line_edit.setGeometry(90, 400, 350, 50)
        self.usuario_line_edit.setFocus()
        self.boton_usuario.setGeometry(475, 400, 80, 50)

    def manejo_boton(self):
        mensaje = {"status": "mensaje", "data": {"usuario": self.nombre_usuario,
                                                 "contenido": self.usuario_line_edit.text()}}
        # self.servidor_signal.emit(mensaje)
        self.usuario_line_edit.setText("")

    def actualizar_chat(self, contenido):
        print(contenido)
        self.chat_log += f"{contenido}\n"
        self.chat_log_label.setText(self.chat_log)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = VentanaChat()
    # ui.setupUi(MainWindow)
    # ui.setupVentana()
    MainWindow.show()
    sys.exit(app.exec_())
