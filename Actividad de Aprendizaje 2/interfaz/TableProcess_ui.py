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
    QLCDNumber, QLabel, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

from queue import Queue
import time, os

class Ui_TableProcess(object):
    def __init__(self, Data, batch):
        self.dictProcess = Data
        self.batch = batch

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(940, 286)
        self.LotePend = QLabel(Form)
        self.LotePend.setObjectName(u"LotePend")
        self.LotePend.setGeometry(QRect(20, 10, 171, 20))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.LotePend.setFont(font)
        self.tableActual = QTableWidget(Form)
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
        font1 = QFont()
        font1.setBold(False)
        font1.setKerning(True)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem3.setFont(font1);
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
        font2 = QFont()
        font2.setBold(True)
        self.tableActual.setFont(font2)
        self.tableActual.setFrameShadow(QFrame.Sunken)
        self.tableActual.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableActual.setAlternatingRowColors(True)
        self.tableActual.setShowGrid(True)
        self.tableActual.setSortingEnabled(False)
        self.tableActual.horizontalHeader().setCascadingSectionResizes(False)
        self.tableActual.horizontalHeader().setMinimumSectionSize(39)
        self.LoteActual = QLabel(Form)
        self.LoteActual.setObjectName(u"LoteActual")
        self.LoteActual.setGeometry(QRect(10, 50, 86, 21))
        self.LoteActual.setFont(font)
        self.processInExcute = QLabel(Form)
        self.processInExcute.setObjectName(u"processInExcute")
        self.processInExcute.setGeometry(QRect(340, 53, 161, 21))
        self.processInExcute.setFont(font)
        self.tableEnEjecucion = QTableWidget(Form)
        if (self.tableEnEjecucion.columnCount() < 2):
            self.tableEnEjecucion.setColumnCount(2)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableEnEjecucion.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableEnEjecucion.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        if (self.tableEnEjecucion.rowCount() < 5):
            self.tableEnEjecucion.setRowCount(5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableEnEjecucion.setVerticalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableEnEjecucion.setVerticalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableEnEjecucion.setVerticalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableEnEjecucion.setVerticalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableEnEjecucion.setVerticalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setTextAlignment(Qt.AlignCenter);
        self.tableEnEjecucion.setItem(0, 0, __qtablewidgetitem11)
        self.tableEnEjecucion.setObjectName(u"tableEnEjecucion")
        self.tableEnEjecucion.setGeometry(QRect(340, 80, 271, 161))
        self.tableEnEjecucion.setFont(font2)
        self.tableEnEjecucion.setFrameShadow(QFrame.Sunken)
        self.tableEnEjecucion.setAutoScroll(True)
        self.tableEnEjecucion.setAlternatingRowColors(True)
        self.tableEnEjecucion.setSortingEnabled(False)
        self.tableEnEjecucion.horizontalHeader().setVisible(False)
        self.tableFinishing = QTableWidget(Form)
        if (self.tableFinishing.columnCount() < 3):
            self.tableFinishing.setColumnCount(3)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableFinishing.setHorizontalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableFinishing.setHorizontalHeaderItem(1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableFinishing.setHorizontalHeaderItem(2, __qtablewidgetitem14)
        if (self.tableFinishing.rowCount() < 1):
            self.tableFinishing.setRowCount(1)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableFinishing.setVerticalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setTextAlignment(Qt.AlignCenter);
        self.tableFinishing.setItem(0, 0, __qtablewidgetitem16)
        self.tableFinishing.setObjectName(u"tableFinishing")
        self.tableFinishing.setGeometry(QRect(620, 77, 311, 192))
        self.tableFinishing.setFont(font2)
        self.tableFinishing.setAlternatingRowColors(True)
        self.Finishing = QLabel(Form)
        self.Finishing.setObjectName(u"Finishing")
        self.Finishing.setGeometry(QRect(620, 50, 89, 21))
        self.Finishing.setFont(font)
        self.contTime_2 = QLCDNumber(Form)
        self.contTime_2.setObjectName(u"contTime_2")
        self.contTime_2.setGeometry(QRect(190, 10, 31, 23))
        self.contTime_2.setFrameShadow(QFrame.Plain)
        self.contTime_2.setMidLineWidth(0)
        self.contTime_2.setDigitCount(1)
        self.countTime = QLabel(Form)
        self.countTime.setObjectName(u"countTime")
        self.countTime.setGeometry(QRect(331, 11, 76, 21))
        self.countTime.setFont(font)
        self.contTime = QLCDNumber(Form)
        self.contTime.setObjectName(u"contTime")
        self.contTime.setGeometry(QRect(467, 11, 64, 23))
        self.contTime.setFrameShadow(QFrame.Plain)
        self.contTime.setDigitCount(1)
        self.contTime.setSegmentStyle(QLCDNumber.Filled)
        self.contTime.setProperty("intValue", 0)

        for r, element in enumerate(self.dictProcess.items()):
            print(r, element)
            self.tableActual.setItem(r, 0, QTableWidgetItem(str(element[0])))
            self.tableActual.setItem(r, 1, QTableWidgetItem(str(element[1][2])))
            self.tableActual.setItem(r, 2, QTableWidgetItem(str(element[1][3])))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.LotePend.setText(QCoreApplication.translate("Form", u"N# Lotes Pendientes: ", None))
        ___qtablewidgetitem = self.tableActual.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID", None));
        ___qtablewidgetitem1 = self.tableActual.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"TME", None));
        ___qtablewidgetitem2 = self.tableActual.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"TT", None));

        __sortingEnabled = self.tableActual.isSortingEnabled()
        self.tableActual.setSortingEnabled(False)
        self.tableActual.setSortingEnabled(__sortingEnabled)

        self.LoteActual.setText(QCoreApplication.translate("Form", u"Lote Actual", None))
        self.processInExcute.setText(QCoreApplication.translate("Form", u"Proceso en ejecuci\u00f3n", None))
        ___qtablewidgetitem3 = self.tableEnEjecucion.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"ID", None));
        ___qtablewidgetitem4 = self.tableEnEjecucion.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Operaci\u00f3n", None));
        ___qtablewidgetitem5 = self.tableEnEjecucion.verticalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"TME", None));
        ___qtablewidgetitem6 = self.tableEnEjecucion.verticalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"TT", None));
        ___qtablewidgetitem7 = self.tableEnEjecucion.verticalHeaderItem(4)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"TR", None));

        __sortingEnabled1 = self.tableEnEjecucion.isSortingEnabled()
        self.tableEnEjecucion.setSortingEnabled(False)
        self.tableEnEjecucion.setSortingEnabled(__sortingEnabled1)

        ___qtablewidgetitem8 = self.tableFinishing.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"ID", None));
        ___qtablewidgetitem9 = self.tableFinishing.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form", u"Resultado", None));
        ___qtablewidgetitem10 = self.tableFinishing.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Form", u"NL", None));

        __sortingEnabled2 = self.tableFinishing.isSortingEnabled()
        self.tableFinishing.setSortingEnabled(False)
        self.tableFinishing.setSortingEnabled(__sortingEnabled2)

        self.Finishing.setText(QCoreApplication.translate("Form", u"Terminados", None))
        self.countTime.setText(QCoreApplication.translate("Form", u"Contador:", None))
    # retranslateUi

    def runProcess(self):
        cola = Queue() #Lotes en espera
        lis = []      #Lotes Terminados
        lotes = self.batch     #Variable que indica la cantidad de lotes por realizar
        contador = 0  #Contador global

'''
 #               fila += 1
            #--------------------------------------------------------------------------------------------------------
            limpiar(8,13)   #Limpia las filas en ejecucion
            imprimir_en_posicion(8, 0, '-------------------- < Proceso en ejecución > --------------------')
            imprimir_en_posicion(9, 0, f'>Programador: {ejecucion[1][0]}')
            imprimir_en_posicion(10, 0, f'-ID: {ejecucion[0]}')
            imprimir_en_posicion(11, 0, f'-Operacion-> {ejecucion[1][1]}')
            imprimir_en_posicion(12, 0, f'-Tiempo MXE: {ejecucion[1][3]}')
            TT = 0
            while TT < ejecucion[1][3]:
                TT += 1
                imprimir_en_posicion(13, 0, f'-Tiempo TRA: {TT}')
                imprimir_en_posicion(14, 0, '                 ')  #Limpia antes de mostrar
                imprimir_en_posicion(14, 0, f'-Tiempo RES: {ejecucion[1][3]-TT}')
                contador += 1
                imprimir_en_posicion(8, 80, f' < Contador: {contador} >')  #Muestra el contador
                time.sleep(1)
            lis.append(ejecucion)
            #limpiar(16,100) #Limpia los terminados
            imprimir_en_posicion(16, 1, '------------------------- < Terminados > --------------------------')
            imprimir_en_posicion(17, 1, '>ID\t\t>Operacion\t\t\t>Resultado\t>NL')
            fila_term = 18
            for terminados in lis:   #Muestra cada uno de los procesos terminadt\tos
                idString = resize_string(' ' + str(terminados[0]),18)
                operationString = resize_string(terminados[1][1],32)
                resultString = resize_string(' ' + str(terminados[1][2]),14)
                NL_String = resize_string(' ' + str(terminados[1][4]),4)
                imprimir_en_posicion(fila_term, 1, f'{idString}{operationString}{resultString}{NL_String}')
                fila_term += 1'''
