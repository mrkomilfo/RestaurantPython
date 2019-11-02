from PyQt5 import QtWidgets
from View.authorization import Ui_MainWindow
import Control.enterWindow as EnterWindow
import Control.administrationWindow as AdministrationWindow
from DB.dbHandler import dbHandler as DB


class AuthorizationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(AuthorizationWindow, self).__init__()
        self.enter_window = None
        self.administration_window = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.enterButton.clicked.connect(self.openAdministrationPage)
        self.ui.backButton.clicked.connect(self.openEnterPage)

    def openEnterPage(self):
        self.enter_window = EnterWindow.EnterWindow()
        self.enter_window.show()
        self.close()

    def openAdministrationPage(self):
        if DB.login(self.ui.loginEdit.text(), self.ui.passwordEdit.text()):
            self.administration_window = AdministrationWindow.AdministrationWindow()
            self.administration_window.show()
            self.close()
