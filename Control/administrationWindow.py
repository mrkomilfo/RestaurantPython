from PyQt5 import QtWidgets
from View.administration import Ui_MainWindow
import Control.authorizationWindow as AuthorizationWindow
import Control.newDishWindow as NewDishWindow
import Control.newEmployeeWindow as NewEmployeeWindow
import Control.changePasswordWindow as ChangePasswordWindow


class AdministrationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(AdministrationWindow, self).__init__()
        self.authorization_window = None
        self.new_dish_window = None
        self.new_employee_window = None
        self.change_password_window = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.backButton.clicked.connect(self.openAuthorizationPage)
        self.ui.addDishButton.clicked.connect(self.openNewDishPage)
        self.ui.addEmployeeButton.clicked.connect(self.openNewEmployeePage)
        self.ui.changePasswordButton.clicked.connect(self.openChangePasswordPage)
        self.ui.tabWidget.setCurrentIndex(0)

    def openAuthorizationPage(self):
        self.authorization_window = AuthorizationWindow.AuthorizationWindow()
        self.authorization_window.show()
        self.close()

    def openNewDishPage(self):
        self.new_dish_window = NewDishWindow.NewDishWindow()
        self.new_dish_window.show()
        self.close()

    def openNewEmployeePage(self):
        self.new_employee_window = NewEmployeeWindow.NewEmployeeWindow()
        self.new_employee_window.show()
        self.close()

    def openChangePasswordPage(self):
        self.change_password_window = ChangePasswordWindow.ChangePasswordWindow()
        self.change_password_window.show()
        self.close()
