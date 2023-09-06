import sys
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QSizePolicy,
    QSpinBox, QStatusBar, QWidget)

from input_ui import Ui_inputProcess
from Data_ui import Ui_Data
from TableData import Ui_TableData

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = Ui_inputProcess()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec())