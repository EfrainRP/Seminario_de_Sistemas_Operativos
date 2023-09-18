# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Data.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpinBox, QSplitter, QWidget)

class Ui_Data(object):
    def setupUi(self, Data):
        if not Data.objectName():
            Data.setObjectName(u"Data")
        Data.resize(221, 253)
        self.pushButton = QPushButton(Data)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(70, 220, 75, 24))
        self.label_7 = QLabel(Data)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setEnabled(True)
        self.label_7.setGeometry(QRect(8, 189, 201, 31))
        self.label_7.setLayoutDirection(Qt.LeftToRight)
        self.label_7.setAutoFillBackground(False)
        self.splitter_6 = QSplitter(Data)
        self.splitter_6.setObjectName(u"splitter_6")
        self.splitter_6.setGeometry(QRect(20, 21, 177, 161))
        self.splitter_6.setOrientation(Qt.Vertical)
        self.splitter = QSplitter(self.splitter_6)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.label = QLabel(self.splitter)
        self.label.setObjectName(u"label")
        self.splitter.addWidget(self.label)
        self.lineEdit = QLineEdit(self.splitter)
        self.lineEdit.setObjectName(u"lineEdit")
        self.splitter.addWidget(self.lineEdit)
        self.splitter_6.addWidget(self.splitter)
        self.widget = QWidget(self.splitter_6)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.spinBox_2 = QSpinBox(self.widget)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setMaximum(999999)

        self.horizontalLayout.addWidget(self.spinBox_2)

        self.splitter_6.addWidget(self.widget)
        self.splitter_3 = QSplitter(self.splitter_6)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Horizontal)
        self.label_3 = QLabel(self.splitter_3)
        self.label_3.setObjectName(u"label_3")
        self.splitter_3.addWidget(self.label_3)
        self.spinBox_3 = QSpinBox(self.splitter_3)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setMinimum(-999999)
        self.spinBox_3.setMaximum(999999)
        self.splitter_3.addWidget(self.spinBox_3)
        self.splitter_6.addWidget(self.splitter_3)
        self.splitter_4 = QSplitter(self.splitter_6)
        self.splitter_4.setObjectName(u"splitter_4")
        self.splitter_4.setOrientation(Qt.Horizontal)
        self.label_4 = QLabel(self.splitter_4)
        self.label_4.setObjectName(u"label_4")
        self.splitter_4.addWidget(self.label_4)
        self.spinBox_4 = QSpinBox(self.splitter_4)
        self.spinBox_4.setObjectName(u"spinBox_4")
        self.spinBox_4.setMinimum(-999999)
        self.spinBox_4.setMaximum(999999)
        self.splitter_4.addWidget(self.spinBox_4)
        self.splitter_6.addWidget(self.splitter_4)
        self.splitter_5 = QSplitter(self.splitter_6)
        self.splitter_5.setObjectName(u"splitter_5")
        self.splitter_5.setOrientation(Qt.Horizontal)
        self.label_5 = QLabel(self.splitter_5)
        self.label_5.setObjectName(u"label_5")
        self.splitter_5.addWidget(self.label_5)
        self.comboBox = QComboBox(self.splitter_5)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setEditable(False)
        self.comboBox.setMaxVisibleItems(5)
        self.comboBox.setMaxCount(5)
        self.splitter_5.addWidget(self.comboBox)
        self.splitter_6.addWidget(self.splitter_5)
        self.splitter_2 = QSplitter(self.splitter_6)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.label_6 = QLabel(self.splitter_2)
        self.label_6.setObjectName(u"label_6")
        self.splitter_2.addWidget(self.label_6)
        self.spinBox = QSpinBox(self.splitter_2)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(99999999)
        self.splitter_2.addWidget(self.spinBox)
        self.splitter_6.addWidget(self.splitter_2)

        self.retranslateUi(Data)

        QMetaObject.connectSlotsByName(Data)
    # setupUi

    def retranslateUi(self, Data):
        Data.setWindowTitle(QCoreApplication.translate("Data", u"Dialog", None))
        self.pushButton.setText(QCoreApplication.translate("Data", u"Enter", None))
        self.label_7.setText("")
        self.label.setText(QCoreApplication.translate("Data", u"Nombre", None))
        self.label_2.setText(QCoreApplication.translate("Data", u"ID:", None))
        self.label_3.setText(QCoreApplication.translate("Data", u"Cifra #1: ", None))
        self.label_4.setText(QCoreApplication.translate("Data", u"Cifra #2:", None))
        self.label_5.setText(QCoreApplication.translate("Data", u"Operaci\u00f3n", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Data", u"+", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Data", u"-", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Data", u"*", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Data", u"/", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Data", u"%", None))

        self.comboBox.setCurrentText(QCoreApplication.translate("Data", u"+", None))
        self.label_6.setText(QCoreApplication.translate("Data", u"Tiempo Aprox.:", None))
    # retranslateUi

