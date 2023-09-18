from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QHeaderView,
    QLCDNumber, QLabel, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

from TableProcess_ui import *
from proceso import *

import time
import random
import keyboard

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.__listProcess = [] #Procesos actuales
        self.__lenProcess = 0
        self.__terminados = [] #Procesos terminados
        self.__contador = 0

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushCountProcess.clicked.connect(self.inputData)
    
    def inputData(self):
        self.__lenProcess = self.ui.CountProcess.value()



