import time
from PyQt6 import QtCore, QtWidgets



class Worker(QtCore.QObject):
    started = QtCore.pyqtSignal()
    finished = QtCore.pyqtSignal()
    data = QtCore.pyqtSignal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.running = False

    @QtCore.pyqtSlot()
    def read_data_from_sensor(self):
        self.started.emit()
        while self.running:
            dt  = time.strftime("%Y-%m-%d %H:%M:%S")
            self.data.emit(dt)
            time.sleep(1) # Simulamos proceso bloqueante
        self.finished.emit()


class App(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Implementación mediante hilo")
        self.setGeometry(100, 100, 400, 300)

        self.boton_iniciar = QtWidgets.QPushButton('Iniciar', self)
        self.boton_iniciar.move(150, 150) 
        self.boton_iniciar.clicked.connect(self.read_data)

        self.label_data = QtWidgets.QLabel(self)
        self.label_data.setGeometry(160, 80,  400, 50)
        self.label_data.setText('En espera')

        self._worker = Worker()
        self._worker.started.connect(self.on_started)
        self._worker.finished.connect(self.on_finished)
        self._worker.data.connect(self.update_label)

        self._thread = QtCore.QThread(self)
        self._thread.start()
        self._worker.moveToThread(self._thread)

    @QtCore.pyqtSlot()
    def on_started(self):
        """Será llamada cuando se inicie la recoleccion de datos"""
        self.label_data.setText("Iniciando lectura")
        self.boton_iniciar.setText("Detener")
        self.boton_iniciar.setEnabled(True)

    @QtCore.pyqtSlot()
    def on_finished(self):
        """Será llamada cuando finalize la recolección de datos"""
        self.label_data.setText("En espera")
        self.boton_iniciar.setText("Iniciar")
        self.boton_iniciar.setEnabled(True)

    @QtCore.pyqtSlot()
    def read_data(self):
        """Iniciar/detener lectura al pulsar el botón"""
        if self._worker.running:
            self._worker.running = False
        else:
            self._worker.running = True
            QtCore.QTimer.singleShot(0, self._worker.read_data_from_sensor)
        self.boton_iniciar.setEnabled(False)

    @QtCore.pyqtSlot(str)
    def update_label(self, data):
        """Será llamada cuando existan nuevos datos a mostrar en el label"""
        self.label_data.setText(data)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ventana = App()
    ventana.show()
    sys.exit(app.exec())