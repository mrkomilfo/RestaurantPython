# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'enter.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(129, -1, 351, 401))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(0, 20))
        self.label.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Lobster")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.employeeButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.employeeButton.setMinimumSize(QtCore.QSize(0, 20))
        self.employeeButton.setMaximumSize(QtCore.QSize(16777215, 65))
        font = QtGui.QFont()
        font.setFamily("Lobster")
        font.setPointSize(20)
        self.employeeButton.setFont(font)
        self.employeeButton.setObjectName("employeeButton")
        self.verticalLayout_2.addWidget(self.employeeButton)
        self.guestButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.guestButton.setMinimumSize(QtCore.QSize(0, 20))
        self.guestButton.setMaximumSize(QtCore.QSize(16777215, 65))
        font = QtGui.QFont()
        font.setFamily("Lobster")
        font.setPointSize(20)
        self.guestButton.setFont(font)
        self.guestButton.setObjectName("guestButton")
        self.verticalLayout_2.addWidget(self.guestButton)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Enter"))
        self.label.setText(_translate("MainWindow", "                Кто вы?"))
        self.employeeButton.setText(_translate("MainWindow", "Сотрудник"))
        self.guestButton.setText(_translate("MainWindow", "Гость"))

