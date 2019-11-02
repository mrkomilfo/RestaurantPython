from PyQt5 import QtGui, QtWidgets, QtCore
from View.customer import Ui_MainWindow
import Control.enterWindow as EnterWindow
from Models.Menu import Menu
from Models.Section import Section
from Models.Bill import Bill
from Models.Order import Order
from DB.dbHandler import dbHandler as DB
import datetime


class CustomerWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(CustomerWindow, self).__init__()
        self.enter_window = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.bill = Bill()
        loaded_menu = DB.get_menu()
        self.menu = dict()
        self.menu.setdefault("Холодные закуски", Menu())
        self.menu.setdefault("Первое блюдо", Menu())
        self.menu.setdefault("Гарниры", Menu())
        self.menu.setdefault("Горячие блюда", Menu())
        self.menu.setdefault("Напитки", Menu())
        self.menu.setdefault("Десерты", Menu())
        for dish in loaded_menu.values():
            self.menu[dish.dish_type].add(dish)
        self.ui.typesComboBox.addItem("Не выбрано")
        self.ui.typesComboBox.addItem("Холодные закуски")
        self.ui.typesComboBox.addItem("Первое блюдо")
        self.ui.typesComboBox.addItem("Гарниры")
        self.ui.typesComboBox.addItem("Горячие блюда")
        self.ui.typesComboBox.addItem("Напитки")
        self.ui.typesComboBox.addItem("Десерты")

        self.ui.typesComboBox.currentTextChanged.connect(self.comboboxChanged)
        self.ui.mainMenuButton.clicked.connect(self.openEnterPage)
        self.ui.plusButon.clicked.connect(self.addDish)
        self.ui.minusButton.clicked.connect(self.removeDish)
        self.ui.confirmButton.clicked.connect(self.confirmOrder)
        self.ui.cancelButton.clicked.connect(self.cancelOrder)

    def openEnterPage(self):
        self.enter_window = EnterWindow.EnterWindow()
        self.enter_window.show()
        self.close()

    def comboboxChanged(self, value):
        if value == "Не выбрано":
            self.ui.menuTableWidget.setRowCount(0)
        else:
            row = 0
            self.ui.menuTableWidget.setRowCount(len(self.menu.get(value)))
            for dish in self.menu.get(value).values():
                item = QtWidgets.QTableWidgetItem(dish.name)
                item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.ui.menuTableWidget.setItem(row, 0, item)
                item = QtWidgets.QTableWidgetItem(str(dish.output))
                item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.ui.menuTableWidget.setItem(row, 1, item)
                item = QtWidgets.QTableWidgetItem(str(dish.price))
                item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.ui.menuTableWidget.setItem(row, 2, item)
                row += 1

    def showBill(self):
        self.ui.billTableWidget.setRowCount(0)
        row_counter = len(self.bill)
        self.ui.billTableWidget.setRowCount(row_counter)
        row = 0
        for section in self.bill.values():
            item = QtWidgets.QTableWidgetItem(section.name)
            item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.ui.billTableWidget.setItem(row, 0, item)
            item = QtWidgets.QTableWidgetItem(str(section.output))
            item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.ui.billTableWidget.setItem(row, 1, item)
            item = QtWidgets.QTableWidgetItem(str(section.number))
            item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.ui.billTableWidget.setItem(row, 2, item)
            item = QtWidgets.QTableWidgetItem(str(section.get_cost()))
            item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.ui.billTableWidget.setItem(row, 3, item)
            row += 1
        self.ui.priceLabel.setText(str(self.bill.getCost()))

    def addDish(self):
        indexes = self.ui.menuTableWidget.selectedIndexes()
        for index in indexes:
            dish_name = self.ui.menuTableWidget.item(index.row(), 0).text()
            dish_type = self.ui.typesComboBox.currentText()
            self.bill.add(Section(self.menu[dish_type][dish_name]))
        self.showBill()

    def removeDish(self):
        indexes = self.ui.billTableWidget.selectedIndexes()
        for index in indexes:
            dish_name = self.ui.billTableWidget.item(index.row(), 0).text()
            self.bill.remove(dish_name)
        self.showBill()

    def confirmOrder(self):
        time = datetime.datetime.now()
        id = str(time.day)+str(time.month)+str(time.year)+str(time.hour)+str(time.minute)+str(time.second)
        DB.add_order(Order(id, str(time)[:19], self.bill))
        self.bill.clear()
        self.ui.billTableWidget.setRowCount(0)

    def cancelOrder(self):
        self.bill.clear()
        self.ui.billTableWidget.setRowCount(0)
        self.showBill()
