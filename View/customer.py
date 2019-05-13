# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'customer.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.typesComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.typesComboBox.setObjectName("typesComboBox")
        self.horizontalLayout_4.addWidget(self.typesComboBox)
        self.minusButton = QtWidgets.QPushButton(self.centralwidget)
        self.minusButton.setObjectName("minusButton")
        self.horizontalLayout_4.addWidget(self.minusButton)
        self.plusButon = QtWidgets.QPushButton(self.centralwidget)
        self.plusButon.setObjectName("plusButon")
        self.horizontalLayout_4.addWidget(self.plusButon)
        self.horizontalLayout_4.setStretch(0, 90)
        self.horizontalLayout_4.setStretch(1, 5)
        self.horizontalLayout_4.setStretch(2, 5)
        self.verticalLayout_9.addLayout(self.horizontalLayout_4)
        self.menuTableView = QtWidgets.QTableView(self.centralwidget)
        self.menuTableView.setObjectName("menuTableView")
        self.verticalLayout_9.addWidget(self.menuTableView)
        self.horizontalLayout.addLayout(self.verticalLayout_9)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Lobster")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.mainMenuButton = QtWidgets.QPushButton(self.centralwidget)
        self.mainMenuButton.setObjectName("mainMenuButton")
        self.horizontalLayout_2.addWidget(self.mainMenuButton)
        self.horizontalLayout_2.setStretch(0, 3)
        self.verticalLayout_8.addLayout(self.horizontalLayout_2)
        self.billTableView = QtWidgets.QTableView(self.centralwidget)
        self.billTableView.setObjectName("billTableView")
        self.verticalLayout_8.addWidget(self.billTableView)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.cancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout_5.addWidget(self.cancelButton)
        self.confirmButton = QtWidgets.QPushButton(self.centralwidget)
        self.confirmButton.setObjectName("confirmButton")
        self.horizontalLayout_5.addWidget(self.confirmButton)
        self.verticalLayout_8.addLayout(self.horizontalLayout_5)
        self.horizontalLayout.addLayout(self.verticalLayout_8)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.minusButton.setText(_translate("MainWindow", "-"))
        self.plusButon.setText(_translate("MainWindow", "+"))
        self.label.setText(_translate("MainWindow", "Ваш заказ"))
        self.mainMenuButton.setText(_translate("MainWindow", "Главное меню"))
        self.cancelButton.setText(_translate("MainWindow", "Отменить заказ"))
        self.confirmButton.setText(_translate("MainWindow", "Подтвердить заказ"))

