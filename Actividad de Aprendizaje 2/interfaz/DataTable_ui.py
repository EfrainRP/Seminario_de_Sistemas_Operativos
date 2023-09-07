# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DataTable.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_DataTable(object):
    def __init__(self, Data):
        self.dictProcess = Data
        
    def setupUi(self, DataTable):
        if not DataTable.objectName():
            DataTable.setObjectName(u"DataTable")
        DataTable.resize(847, 649)
        self.label_6 = QLabel(DataTable)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setEnabled(True)
        self.label_6.setGeometry(QRect(260, 20, 81, 16))
        font = QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.layoutWidget = QWidget(DataTable)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 60, 788, 531))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.label.setFont(font1)

        self.verticalLayout.addWidget(self.label)

        self.tableWidget = QTableWidget(self.layoutWidget)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout.addWidget(self.tableWidget)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_2)

        self.tableWidget_2 = QTableWidget(self.layoutWidget)
        self.tableWidget_2.setObjectName(u"tableWidget_2")

        self.verticalLayout_2.addWidget(self.tableWidget_2)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_3)

        self.tableWidget_3 = QTableWidget(self.layoutWidget)
        self.tableWidget_3.setObjectName(u"tableWidget_3")

        self.verticalLayout_3.addWidget(self.tableWidget_3)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.label_4 = QLabel(DataTable)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(82, 20, 171, 20))
        self.label_4.setFont(font1)
        self.layoutWidget_2 = QWidget(DataTable)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(470, 20, 268, 23))
        self.layoutWidget_2.setFont(font)
        self.gridLayout = QGridLayout(self.layoutWidget_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)

        self.label_7 = QLabel(self.layoutWidget_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setEnabled(True)
        self.label_7.setFont(font)

        self.gridLayout.addWidget(self.label_7, 0, 1, 1, 1)

        self.pushButton = QPushButton(DataTable)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(370, 600, 111, 31))

        self.retranslateUi(DataTable)

        QMetaObject.connectSlotsByName(DataTable)
    # setupUi

    def retranslateUi(self, DataTable):
        DataTable.setWindowTitle(QCoreApplication.translate("DataTable", u"Form", None))
        self.label_6.setText("")
        self.label.setText(QCoreApplication.translate("DataTable", u"Lote Actual", None))
        self.label_2.setText(QCoreApplication.translate("DataTable", u"Proceso en ejecuci\u00f3n", None))
        self.label_3.setText(QCoreApplication.translate("DataTable", u"Terminados", None))
        self.label_4.setText(QCoreApplication.translate("DataTable", u"N# Lotes Pendientes: ", None))
        self.label_5.setText(QCoreApplication.translate("DataTable", u"Contador:", None))
        self.label_7.setText("")
        self.pushButton.setText(QCoreApplication.translate("DataTable", u"Exit", None))
    # retranslateUi

