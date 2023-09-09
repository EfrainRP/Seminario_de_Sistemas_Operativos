# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'emergente.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_Emergente(object):
    def setupUi(self, Emergente):
        if not Emergente.objectName():
            Emergente.setObjectName(u"Emergente")
        Emergente.resize(252, 168)
        self.message = QLabel(Emergente)
        self.message.setObjectName(u"message")
        self.message.setGeometry(QRect(8, 10, 231, 71))
        self.message.setLayoutDirection(Qt.LeftToRight)
        self.pushEnter = QPushButton(Emergente)
        self.pushEnter.setObjectName(u"pushEnter")
        self.pushEnter.setGeometry(QRect(90, 110, 75, 24))

        self.retranslateUi(Emergente)

        QMetaObject.connectSlotsByName(Emergente)
    # setupUi

    def retranslateUi(self, Emergente):
        Emergente.setWindowTitle(QCoreApplication.translate("Emergente", u"Form", None))
        self.message.setText("")
        self.pushEnter.setText(QCoreApplication.translate("Emergente", u"Enter", None))
    # retranslateUi

