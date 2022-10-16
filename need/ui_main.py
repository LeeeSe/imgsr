# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainmrOGUu.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(151, 144)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(12, 8, 128, 125))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pb_init = QPushButton(self.widget)
        self.pb_init.setObjectName(u"pb_init")

        self.verticalLayout.addWidget(self.pb_init)

        self.pb_choice = QPushButton(self.widget)
        self.pb_choice.setObjectName(u"pb_choice")

        self.verticalLayout.addWidget(self.pb_choice)

        self.pb_predict = QPushButton(self.widget)
        self.pb_predict.setObjectName(u"pb_predict")

        self.verticalLayout.addWidget(self.pb_predict)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_status = QLabel(self.widget)
        self.label_status.setObjectName(u"label_status")

        self.horizontalLayout.addWidget(self.label_status)

        self.label_now = QLabel(self.widget)
        self.label_now.setObjectName(u"label_now")

        self.horizontalLayout.addWidget(self.label_now)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pb_init.setText(QCoreApplication.translate("MainWindow", u"\u521d\u59cb\u5316\u6a21\u578b", None))
        self.pb_choice.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u56fe\u50cf", None))
        self.pb_predict.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u4f18\u5316", None))
        self.label_status.setText(QCoreApplication.translate("MainWindow", u"\u72b6\u6001:", None))
        self.label_now.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u521d\u59cb\u5316\u6a21\u578b", None))
    # retranslateUi

