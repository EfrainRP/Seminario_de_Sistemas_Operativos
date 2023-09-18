# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TableProcess.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QHeaderView,
    QLCDNumber, QLabel, QPushButton, QSizePolicy,
    QSpinBox, QTabWidget, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(839, 333)
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QRect(-4, -1, 841, 321))
        self.Entradas = QWidget()
        self.Entradas.setObjectName(u"Entradas")
        self.Entradas.setEnabled(True)
        self.pushCountProcess = QPushButton(self.Entradas)
        self.pushCountProcess.setObjectName(u"pushCountProcess")
        self.pushCountProcess.setGeometry(QRect(390, 140, 81, 51))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.pushCountProcess.setFont(font)
        self.CountProcess = QSpinBox(self.Entradas)
        self.CountProcess.setObjectName(u"CountProcess")
        self.CountProcess.setGeometry(QRect(390, 90, 81, 31))
        font1 = QFont()
        font1.setPointSize(14)
        self.CountProcess.setFont(font1)
        self.tabWidget.addTab(self.Entradas, "")
        self.Tablas = QWidget()
        self.Tablas.setObjectName(u"Tablas")
        self.tableActual = QTableWidget(self.Tablas)
        if (self.tableActual.columnCount() < 3):
            self.tableActual.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableActual.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableActual.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableActual.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tableActual.rowCount() < 5):
            self.tableActual.setRowCount(5)
        font2 = QFont()
        font2.setBold(False)
        font2.setKerning(True)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem3.setFont(font2);
        __qtablewidgetitem3.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableActual.setItem(0, 0, __qtablewidgetitem3)
        self.tableActual.setObjectName(u"tableActual")
        self.tableActual.setEnabled(True)
        self.tableActual.setGeometry(QRect(10, 77, 321, 181))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableActual.sizePolicy().hasHeightForWidth())
        self.tableActual.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setBold(True)
        self.tableActual.setFont(font3)
        self.tableActual.setFrameShadow(QFrame.Sunken)
        self.tableActual.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableActual.setAlternatingRowColors(True)
        self.tableActual.setShowGrid(True)
        self.tableActual.setSortingEnabled(False)
        self.tableActual.horizontalHeader().setCascadingSectionResizes(False)
        self.tableActual.horizontalHeader().setMinimumSectionSize(39)
        self.countTime = QLabel(self.Tablas)
        self.countTime.setObjectName(u"countTime")
        self.countTime.setGeometry(QRect(331, 11, 76, 21))
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        self.countTime.setFont(font4)
        self.tableFinishing = QTableWidget(self.Tablas)
        if (self.tableFinishing.columnCount() < 3):
            self.tableFinishing.setColumnCount(3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableFinishing.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableFinishing.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableFinishing.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        if (self.tableFinishing.rowCount() < 1):
            self.tableFinishing.setRowCount(1)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableFinishing.setVerticalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignCenter);
        self.tableFinishing.setItem(0, 0, __qtablewidgetitem8)
        self.tableFinishing.setObjectName(u"tableFinishing")
        self.tableFinishing.setGeometry(QRect(520, 77, 311, 192))
        self.tableFinishing.setFont(font3)
        self.tableFinishing.setAlternatingRowColors(True)
        self.processInExcute = QLabel(self.Tablas)
        self.processInExcute.setObjectName(u"processInExcute")
        self.processInExcute.setGeometry(QRect(340, 50, 161, 21))
        self.processInExcute.setFont(font4)
        self.contTime = QLCDNumber(self.Tablas)
        self.contTime.setObjectName(u"contTime")
        self.contTime.setGeometry(QRect(467, 11, 64, 23))
        self.contTime.setFrameShadow(QFrame.Plain)
        self.contTime.setDigitCount(1)
        self.contTime.setSegmentStyle(QLCDNumber.Filled)
        self.contTime.setProperty("intValue", 0)
        self.Finishing = QLabel(self.Tablas)
        self.Finishing.setObjectName(u"Finishing")
        self.Finishing.setGeometry(QRect(520, 50, 89, 21))
        self.Finishing.setFont(font4)
        self.tableEnEjecucion = QTableWidget(self.Tablas)
        if (self.tableEnEjecucion.columnCount() < 1):
            self.tableEnEjecucion.setColumnCount(1)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableEnEjecucion.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        if (self.tableEnEjecucion.rowCount() < 5):
            self.tableEnEjecucion.setRowCount(5)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableEnEjecucion.setVerticalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableEnEjecucion.setVerticalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableEnEjecucion.setVerticalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableEnEjecucion.setVerticalHeaderItem(3, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableEnEjecucion.setVerticalHeaderItem(4, __qtablewidgetitem14)
        self.tableEnEjecucion.setObjectName(u"tableEnEjecucion")
        self.tableEnEjecucion.setGeometry(QRect(340, 80, 171, 161))
        self.tableEnEjecucion.setFont(font3)
        self.tableEnEjecucion.setFrameShadow(QFrame.Sunken)
        self.tableEnEjecucion.setAutoScroll(True)
        self.tableEnEjecucion.setAlternatingRowColors(True)
        self.tableEnEjecucion.setSortingEnabled(False)
        self.tableEnEjecucion.horizontalHeader().setVisible(False)
        self.LoteActual = QLabel(self.Tablas)
        self.LoteActual.setObjectName(u"LoteActual")
        self.LoteActual.setGeometry(QRect(10, 50, 141, 21))
        self.LoteActual.setFont(font4)
        self.tabWidget.addTab(self.Tablas, "")

        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushCountProcess.setText(QCoreApplication.translate("Form", u"Enter", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Entradas), QCoreApplication.translate("Form", u"Entradas", None))
        ___qtablewidgetitem = self.tableActual.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID", None));
        ___qtablewidgetitem1 = self.tableActual.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"TME", None));
        ___qtablewidgetitem2 = self.tableActual.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"TT", None));

        __sortingEnabled = self.tableActual.isSortingEnabled()
        self.tableActual.setSortingEnabled(False)
        self.tableActual.setSortingEnabled(__sortingEnabled)

        self.countTime.setText(QCoreApplication.translate("Form", u"Contador:", None))
        ___qtablewidgetitem3 = self.tableFinishing.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"ID", None));
        ___qtablewidgetitem4 = self.tableFinishing.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Resultado", None));
        ___qtablewidgetitem5 = self.tableFinishing.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"NL", None));

        __sortingEnabled1 = self.tableFinishing.isSortingEnabled()
        self.tableFinishing.setSortingEnabled(False)
        self.tableFinishing.setSortingEnabled(__sortingEnabled1)

        self.processInExcute.setText(QCoreApplication.translate("Form", u"Proceso en ejecuci\u00f3n", None))
        self.Finishing.setText(QCoreApplication.translate("Form", u"Terminados", None))
        ___qtablewidgetitem6 = self.tableEnEjecucion.verticalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"ID", None));
        ___qtablewidgetitem7 = self.tableEnEjecucion.verticalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"Operaci\u00f3n", None));
        ___qtablewidgetitem8 = self.tableEnEjecucion.verticalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"TME", None));
        ___qtablewidgetitem9 = self.tableEnEjecucion.verticalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form", u"TT", None));
        ___qtablewidgetitem10 = self.tableEnEjecucion.verticalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Form", u"TR", None));
        self.LoteActual.setText(QCoreApplication.translate("Form", u"Procesos Actuales", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tablas), QCoreApplication.translate("Form", u"Tablas", None))
    # retranslateUi

