from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QPushButton, QLabel

class VentanaEmergente(QDialog):
    def __init__(self, message):
        super().__init__()

        self.setWindowTitle("Ventana Emergente")
        self.setGeometry(100, 100, 200, 100)

        layout = QVBoxLayout(self)

        etiqueta = QLabel(message)
        layout.addWidget(etiqueta)

        cerrar_button = QPushButton("Cerrar")
        cerrar_button.clicked.connect(self.accept)
        layout.addWidget(cerrar_button)