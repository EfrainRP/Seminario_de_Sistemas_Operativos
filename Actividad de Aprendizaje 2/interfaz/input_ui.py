# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'input.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpinBox, QStatusBar,
    QWidget)

from Data_ui import Ui_Data

class Ui_inputProcess(object):
    def setupUi(self, inputProcess):
        if not inputProcess.objectName():
            inputProcess.setObjectName(u"inputProcess")
        inputProcess.resize(316, 88)
        icon = QIcon()
        icon.addFile(u"Actividad de Aprendizaje 2\interfaz\Images\input.png", QSize(), QIcon.Normal, QIcon.Off)
        inputProcess.setWindowIcon(icon)
        self.centralwidget = QWidget(inputProcess)
        self.centralwidget.setObjectName(u"centralwidget")
        self.enterInput1 = QPushButton(self.centralwidget)
        self.enterInput1.setObjectName(u"enterInput1")
        self.enterInput1.setGeometry(QRect(120, 40, 75, 24))
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 297, 24))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.process = QSpinBox(self.layoutWidget)
        self.process.setObjectName(u"process")
        self.process.setMinimum(1)
        self.process.setMaximum(99999999)

        self.horizontalLayout.addWidget(self.process)

        inputProcess.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(inputProcess)
        self.statusbar.setObjectName(u"statusbar")
        inputProcess.setStatusBar(self.statusbar)

        self.retranslateUi(inputProcess)
        
        QMetaObject.connectSlotsByName(inputProcess)

        self.windowData = QWidget()
        self.enterInput1.clicked.connect(self.clicked_button1)
        

    # setupUi

    def retranslateUi(self, inputProcess):
        inputProcess.setWindowTitle(QCoreApplication.translate("inputProcess", u"Entrada de datos", None))
        self.enterInput1.setText(QCoreApplication.translate("inputProcess", u"Enter", None))
        self.label.setText(QCoreApplication.translate("inputProcess", u"Ingrese la cantidad de procesos a realizar: ", None))
    # retranslateUi

    def clicked_button1(self):
        self.ui = Ui_Data()
        process = self.process.value()
        print(process)
        self.ui.setupUi(self.windowData,process)
        self.windowData.show()

    def exit(self, event):
        self.windowData.close()
