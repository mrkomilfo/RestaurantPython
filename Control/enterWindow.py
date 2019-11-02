from PyQt5 import QtWidgets
from View.enter import Ui_MainWindow
import Control.customerWindow as CustomerWindow
import Control.authorizationWindow as AuthorizationWindow


class EnterWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(EnterWindow, self).__init__()
        self.customer_window = None
        self.authorization_window = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.employeeButton.clicked.connect(self.open_authorization_page)
        self.ui.guestButton.clicked.connect(self.open_customer_page)

    def open_customer_page(self):
        self.customer_window = CustomerWindow.CustomerWindow()
        self.customer_window.show()
        self.close()

    def open_authorization_page(self):
        self.authorization_window = AuthorizationWindow.AuthorizationWindow()
        self.authorization_window.show()
        self.close()
