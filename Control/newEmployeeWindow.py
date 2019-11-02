from PyQt5 import QtWidgets
from View.newEmployee import Ui_MainWindow
import Control.administrationWindow as AdministrationWindow
from Models.Employee import Employee
from DB.dbHandler import dbHandler as DB


class NewEmployeeWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(NewEmployeeWindow, self).__init__()
        self.administration_window = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.cancelButton.clicked.connect(self.open_administration_page)
        self.ui.addButton.clicked.connect(self.add_employee)
        self.ui.menuAccess.stateChanged.connect(self.menu_access_changed)
        self.ui.menuReadonly.stateChanged.connect(self.menu_readonly_changed)
        self.ui.staffAccess.stateChanged.connect(self.staff_access_changed)
        self.ui.staffReadonly.stateChanged.connect(self.staff_readonly_changed)
        self.ui.ordersAccess.stateChanged.connect(self.orders_access_changed)
        self.ui.ordersReadonly.stateChanged.connect(self.orders_readonly_changed)

    def open_administration_page(self):
        self.administration_window = AdministrationWindow.AdministrationWindow()
        self.administration_window.show()
        self.close()

    def add_employee(self):
        employee = Employee(self.ui.surnameEdit.currentText(), self.ui.nameEdit.text(), self.ui.patronymicEdit.text(),
                            self.ui.birthDateEdit.date(), self.ui.positionEdit, self.ui.salaryEdit, self.ui.loginEdit,
                            self.ui.passwordEdit, self.ui.menuAccess.isChecked(), self.ui.menuReadonly.isChecked(),
                            self.ui.staffAccess.isChecked(), self.ui.staffReadonly.isChecked(),
                            self.ui.ordersAccess.isChecked(), self.ui.ordersReadonly.isChecked())
        DB.add_employee(employee)
        self.open_administration_page()

    def menu_access_changed(self):
        if not self.ui.menuAccess.isChecked() and self.ui.menuReadonly.isChecked():
            self.ui.menuReadonly.setChecked(False)

    def menu_readonly_changed(self):
        if self.ui.menuReadonly.isChecked() and not self.ui.menuAccess.isChecked():
            self.ui.menuAccess.setChecked(True)

    def staff_access_changed(self):
        if not self.ui.staffAccess.isChecked() and self.ui.staffReadonly.isChecked():
            self.ui.staffReadonly.setChecked(False)

    def staff_readonly_changed(self):
        if self.ui.staffReadonly.isChecked() and not self.ui.staffAccess.isChecked():
            self.ui.staffAccess.setChecked(True)

    def orders_access_changed(self):
        if not self.ui.ordersAccess.isChecked() and self.ui.ordersReadonly.isChecked():
            self.ui.ordersReadonly.setChecked(False)

    def orders_readonly_changed(self):
        if self.ui.ordersReadonly.isChecked() and not self.ui.ordersAccess.isChecked():
            self.ui.ordersAccess.setChecked(True)
