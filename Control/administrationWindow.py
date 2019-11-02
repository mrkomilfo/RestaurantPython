from PyQt5 import QtGui, QtWidgets, QtCore

from Models.Menu import Menu
from Models.Dish import Dish
from Models.Employee import Employee
from View.administration import Ui_MainWindow
import Control.authorizationWindow as AuthorizationWindow
import Control.newDishWindow as NewDishWindow
import Control.newEmployeeWindow as NewEmployeeWindow
import Control.changePasswordWindow as ChangePasswordWindow
from DB.dbHandler import dbHandler as DB


class AdministrationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(AdministrationWindow, self).__init__()
        self.account = DB.get_account()
        loaded_menu = DB.get_menu()
        self.staff = DB.get_staff()
        self.orders = DB.get_orders()

        self.authorization_window = None
        self.new_dish_window = None
        self.new_employee_window = None
        self.change_password_window = None

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.backButton.clicked.connect(self.open_authorization_page)
        self.ui.addDishButton.clicked.connect(self.open_new_dish_page)
        self.ui.addEmployeeButton.clicked.connect(self.open_new_employee_page)
        self.ui.changePasswordButton.clicked.connect(self.open_change_password_page)
        self.ui.closeOrderButton.clicked.connect(self.close_order)
        self.ui.deleteDishButton.clicked.connect(self.delete_dish)
        self.ui.deleteEmployeeButton.clicked.connect(self.delete_employee)
        self.ui.editDishButton.clicked.connect(self.edit_dish)
        self.ui.editDishButton.clicked.connect(self.edit_employee)
        self.ui.menuCheckBox.stateChanged.connect(self.menu_access_changed)
        self.ui.menuReadOnlyCheckBox.stateChanged.connect(self.menu_readonly_changed)
        self.ui.employeesCheckBox.stateChanged.connect(self.staff_access_changed)
        self.ui.employeesReadOnlyCheckBox.stateChanged.connect(self.staff_readonly_changed)
        self.ui.ordersCheckBox.stateChanged.connect(self.orders_access_changed)
        self.ui.ordersReadOnlyCheckBox.stateChanged.connect(self.orders_readonly_changed)

        self.ui.tabWidget.setCurrentIndex(0)
        self.ui.surnameLabel.setText(self.account.surname)
        self.ui.nameLabel.setText(self.account.name)
        self.ui.patronymicLabel.setText(self.account.patronymic)
        self.ui.birthdateLabel.setText(str(self.account.birth_date))
        self.ui.positionLabel.setText(self.account.position)
        self.ui.salaryLabel.setText(str(self.account.salary))
        self.ui.loginLabel.setText(self.account.login)
        self.ui.passwordLabel.setText(self.account.password)

        if not self.account.menu_access:
            self.ui.menuTab.setEnabled(False)
        elif self.account.menu_readonly:
            self.ui.addDishButton.setEnabled(False)
            self.ui.deleteDishButton.setEnabled(False)
            self.ui.editDishButton.setEnabled(False)
        if not self.account.staff_access:
            self.ui.staffTab.setEnabled(False)
        elif self.account.staff_readonly:
            self.ui.addEmployeeButton.setEnabled(False)
            self.ui.deleteEmployeeButton.setEnabled(False)
            self.ui.editEmployeeButton.setEnabled(False)
        if not self.account.orders_access:
            self.ui.menuTab.setEnabled(False)
        elif self.account.orders_readonly:
            self.ui.closeOrderButton.setEnabled(False)

        self.ui.ordersTable.itemSelectionChanged.connect(self.show_order)
        self.show_orders()

        self.menu = dict()
        self.menu.setdefault("Холодные закуски", Menu())
        self.menu.setdefault("Первое блюдо", Menu())
        self.menu.setdefault("Гарниры", Menu())
        self.menu.setdefault("Горячие блюда", Menu())
        self.menu.setdefault("Напитки", Menu())
        self.menu.setdefault("Десерты", Menu())
        for dish in loaded_menu.values():
            self.menu[dish.dish_type].add(dish)
        self.ui.menuTypeComboBox.addItem("Не выбрано")
        self.ui.menuTypeComboBox.addItem("Холодные закуски")
        self.ui.menuTypeComboBox.addItem("Первое блюдо")
        self.ui.menuTypeComboBox.addItem("Гарниры")
        self.ui.menuTypeComboBox.addItem("Горячие блюда")
        self.ui.menuTypeComboBox.addItem("Напитки")
        self.ui.menuTypeComboBox.addItem("Десерты")

        self.ui.dishTypeComboBox.addItem("Не выбрано")
        self.ui.dishTypeComboBox.addItem("Холодные закуски")
        self.ui.dishTypeComboBox.addItem("Первое блюдо")
        self.ui.dishTypeComboBox.addItem("Гарниры")
        self.ui.dishTypeComboBox.addItem("Горячие блюда")
        self.ui.dishTypeComboBox.addItem("Напитки")
        self.ui.dishTypeComboBox.addItem("Десерты")

        self.ui.menuTypeComboBox.currentTextChanged.connect(self.combobox_changed)
        self.ui.menuTable.itemSelectionChanged.connect(self.show_dish)
        self.show_orders()

        self.ui.employeeLoginEdit.setEnabled(False)
        self.ui.employeesTable.itemSelectionChanged.connect(self.show_employee)
        self.show_staff()


    def open_authorization_page(self):
        self.authorization_window = AuthorizationWindow.AuthorizationWindow()
        self.authorization_window.show()
        self.close()

    def open_new_dish_page(self):
        self.new_dish_window = NewDishWindow.NewDishWindow()
        self.new_dish_window.show()
        self.close()

    def open_new_employee_page(self):
        self.new_employee_window = NewEmployeeWindow.NewEmployeeWindow()
        self.new_employee_window.show()
        self.close()

    def open_change_password_page(self):
        self.change_password_window = ChangePasswordWindow.ChangePasswordWindow()
        self.change_password_window.show()
        self.close()

    def combobox_changed(self, value):
        if value == "Не выбрано":
            self.ui.menuTable.setRowCount(0)
        else:
            row = 0
            self.ui.menuTable.setRowCount(len(self.menu.get(value)))
            for dish in self.menu.get(value).values():
                item = QtWidgets.QTableWidgetItem(dish.name)
                item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.ui.menuTable.setItem(row, 0, item)
                item = QtWidgets.QTableWidgetItem(str(dish.output))
                item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.ui.menuTable.setItem(row, 1, item)
                item = QtWidgets.QTableWidgetItem(str(dish.energy))
                item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.ui.menuTable.setItem(row, 2, item)
                item = QtWidgets.QTableWidgetItem(str(dish.price))
                item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.ui.menuTable.setItem(row, 3, item)
                row += 1
        self.ui.menuTable.resizeColumnsToContents()

    def menu_access_changed(self):
        if not self.ui.menuCheckBox.isChecked() and self.ui.menuReadOnlyCheckBox.isChecked():
            self.ui.menuReadOnlyCheckBox.setChecked(False)

    def menu_readonly_changed(self):
        if self.ui.menuReadOnlyCheckBox.isChecked() and not self.ui.menuCheckBox.isChecked():
            self.ui.menuCheckBox.setChecked(True)

    def staff_access_changed(self):
        if not self.ui.employeesCheckBox.isChecked() and self.ui.employeesReadOnlyCheckBox.isChecked():
            self.ui.employeesReadOnlyCheckBox.setChecked(False)

    def staff_readonly_changed(self):
        if self.ui.employeesReadOnlyCheckBox.isChecked() and not self.ui.employeesCheckBox.isChecked():
            self.ui.employeesCheckBox.setChecked(True)

    def orders_access_changed(self):
        if not self.ui.ordersCheckBox.isChecked() and self.ui.ordersReadOnlyCheckBox.isChecked():
            self.ui.ordersReadOnlyCheckBox.setChecked(False)

    def orders_readonly_changed(self):
        if self.ui.ordersReadOnlyCheckBox.isChecked() and not self.ui.ordersCheckBox.isChecked():
            self.ui.ordersCheckBox.setChecked(True)

    def show_dish(self):
        indexes = self.ui.menuTable.selectedIndexes()
        if len(indexes) < 1:
            return
        index = indexes[0]
        dish_name = self.ui.menuTable.item(index.row(), 0).text()
        dish = self.menu[self.ui.menuTypeComboBox.currentText()][dish_name]
        self.ui.dishNameEdit.setText(dish.name)
        self.ui.dishTypeComboBox.setCurrentText(dish.dish_type)
        self.ui.dishOutputEdit.setText(str(dish.output))
        self.ui.dishEnergyEdit.setText(str(dish.energy))
        self.ui.dishPriceEdit.setText(str(dish.price))

    def delete_dish(self):
        indexes = self.ui.menuTable.selectedIndexes()
        if len(indexes) < 1:
            return
        indexes = self.ui.menuTable.selectedIndexes()
        for index in indexes:
            dish_name = self.ui.menuTable.item(index.row(), 0).text()
            del self.menu[self.ui.menuTypeComboBox.currentText()][dish_name]
            DB.remove_dish(dish_name)
        self.combobox_changed(self.ui.menuTypeComboBox.currentText())

    def edit_dish(self):
        dish = Dish(self.ui.dishTypeComboBox.currentText(), self.ui.dishNameEdit.text(),
                    float(self.ui.dishPriceEdit.text()), int(self.ui.dishEnergyEdit.text()),
                    int(self.ui.dishOutputEdit.text()))
        self.delete_dish()
        DB.add_dish(dish)
        self.menu.setdefault(dish.dish_type, dish)
        self.combobox_changed(self.ui.menuTypeComboBox.currentText())

    def edit_employee(self):
        employee = Employee(self.ui.employeeSurnameEdit.text(), self.ui.employeeNameEdit.text(), self.ui.employeePatronymicEdit.text(),
                            self.ui.employeeBirthDateEdit.date(), self.ui.employeePositionEdit, self.ui.employeeSalaryEdit, self.ui.employeeLoginEdit,
                            self.ui.employeePasswordEdit, self.ui.menuCheckBox.isChecked(), self.ui.menuReadOnlyCheckBox.isChecked(),
                            self.ui.employeesReadOnlyCheckBox.isChecked(), self.ui.employeesReadOnlyCheckBox.isChecked(),
                            self.ui.ordersCheckBox.isChecked(), self.ui.ordersReadOnlyCheckBox.isChecked())
        self.delete_employee()
        DB.add_employee(employee)
        self.staff.recruit(employee)
        self.show_staff()

    def delete_employee(self):
        indexes = self.ui.employeesTable.selectedIndexes()
        if len(indexes) < 1:
            return
        indexes = self.ui.employeesTable.selectedIndexes()
        for index in indexes:
            login = self.ui.employeesTable.item(index.row(), 1).text()
            if login != self.account.login:
                del self.staff[login]
                DB.remove_employee(login)
        self.show_staff()

    def show_staff(self):
        row = 0
        self.ui.employeesTable.setRowCount(len(self.staff))
        for employee in self.staff.values():
            item = QtWidgets.QTableWidgetItem(employee.surname + " " + employee.name + " " + employee.patronymic)
            item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.ui.employeesTable.setItem(row, 0, item)
            item = QtWidgets.QTableWidgetItem(employee.login)
            item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.ui.employeesTable.setItem(row, 1, item)
            item = QtWidgets.QTableWidgetItem(employee.position)
            item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.ui.employeesTable.setItem(row, 2, item)
            row += 1
        self.ui.employeesTable.resizeColumnsToContents()

    def show_employee(self):
        indexes = self.ui.employeesTable.selectedIndexes()
        if len(indexes) < 1:
            return
        index = indexes[0]
        login = self.ui.employeesTable.item(index.row(), 1).text()
        employee = self.staff[login]
        self.ui.employeeSurnameEdit.setText(employee.surname)
        self.ui.employeeNameEdit.setText(employee.name)
        self.ui.employeePatronymicEdit.setText(employee.patronymic)
        self.ui.employeeBirthDateEdit.setDate(employee.birth_date)
        self.ui.employeePositionEdit.setText(str(employee.position))
        self.ui.employeeSalaryEdit.setText(str(employee.salary))
        self.ui.employeeLoginEdit.setText(str(employee.login))
        self.ui.employeePasswordEdit.setText(str(employee.password))
        self.ui.menuCheckBox.setChecked(employee.menu_access)
        self.ui.menuReadOnlyCheckBox.setChecked(employee.menu_readonly)
        self.ui.employeesCheckBox.setChecked(employee.staff_access)
        self.ui.employeesReadOnlyCheckBox.setChecked(employee.staff_readonly)
        self.ui.ordersCheckBox.setChecked(employee.orders_access)
        self.ui.ordersReadOnlyCheckBox.setChecked(employee.orders_readonly)

    def show_order(self):
        indexes = self.ui.ordersTable.selectedIndexes()
        if len(indexes) < 1:
            return
        index = indexes[0]
        order_id = self.ui.ordersTable.item(index.row(), 0).text()
        order = self.orders[order_id]
        row_counter = len(order)
        self.ui.orderTable.setRowCount(row_counter)
        row = 0
        for section in order.values():
            item = QtWidgets.QTableWidgetItem(section.name)
            item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.ui.orderTable.setItem(row, 0, item)
            item = QtWidgets.QTableWidgetItem(str(section.output))
            item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.ui.orderTable.setItem(row, 1, item)
            item = QtWidgets.QTableWidgetItem(str(section.number))
            item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.ui.orderTable.setItem(row, 2, item)
            item = QtWidgets.QTableWidgetItem(str(section.get_cost()))
            item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.ui.orderTable.setItem(row, 3, item)
            row += 1
        self.ui.orderTable.resizeColumnsToContents()

    def close_order(self):
        indexes = self.ui.ordersTable.selectedIndexes()
        if len(indexes) < 1:
            return
        index = indexes[0]
        order_id = self.ui.ordersTable.item(index.row(), 0).text()
        del self.orders[order_id]
        DB.close_order(order_id)
        self.show_orders()
        self.ui.orderTable.setRowCount(0)

    def show_orders(self):
        self.ui.ordersTable.setRowCount(len(self.orders))
        row = 0
        for order in self.orders.values():
            item = QtWidgets.QTableWidgetItem(order.id)
            item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.ui.ordersTable.setItem(row, 0, item)
            item = QtWidgets.QTableWidgetItem(order.time)
            item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.ui.ordersTable.setItem(row, 1, item)
            row += 1



