# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newDish.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 460)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 401, 461))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 4, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Lobster")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(16, 32, 16, 32)
        self.gridLayout.setHorizontalSpacing(16)
        self.gridLayout.setVerticalSpacing(40)
        self.gridLayout.setObjectName("gridLayout")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)
        self.nameEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nameEdit.setFont(font)
        self.nameEdit.setObjectName("nameEdit")
        self.gridLayout.addWidget(self.nameEdit, 0, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 4, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)
        self.typeComboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.typeComboBox.setFont(font)
        self.typeComboBox.setObjectName("typeComboBox")
        self.gridLayout.addWidget(self.typeComboBox, 1, 1, 1, 1)
        self.outputEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.outputEdit.setFont(font)
        self.outputEdit.setObjectName("outputEdit")
        self.gridLayout.addWidget(self.outputEdit, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.energyEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.energyEdit.setFont(font)
        self.energyEdit.setObjectName("energyEdit")
        self.gridLayout.addWidget(self.energyEdit, 3, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.priceEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.priceEdit.setFont(font)
        self.priceEdit.setObjectName("priceEdit")
        self.horizontalLayout_2.addWidget(self.priceEdit)
        self.predictPriceButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.predictPriceButton.setObjectName("predictPriceButton")
        self.horizontalLayout_2.addWidget(self.predictPriceButton)
        self.horizontalLayout_2.setStretch(0, 1)
        self.gridLayout.addLayout(self.horizontalLayout_2, 4, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(4, -1, 4, 4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cancelButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        self.addButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.addButton.setObjectName("addButton")
        self.horizontalLayout.addWidget(self.addButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "                 Новое блюдо"))
        self.label_7.setText(_translate("MainWindow", "Тип"))
        self.label_8.setText(_translate("MainWindow", "Выход"))
        self.label_9.setText(_translate("MainWindow", "Цена"))
        self.label_6.setText(_translate("MainWindow", "Название"))
        self.label_2.setText(_translate("MainWindow", "Калорийность"))
        self.predictPriceButton.setText(_translate("MainWindow", "⭐"))
        self.cancelButton.setText(_translate("MainWindow", "Отмена"))
        self.addButton.setText(_translate("MainWindow", "Добавить"))

