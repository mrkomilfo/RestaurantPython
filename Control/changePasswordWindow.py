from PyQt5 import QtWidgets
from View.changePassword import Ui_MainWindow
import Control.administrationWindow as AdministrationWindow


class ChangePasswordWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ChangePasswordWindow, self).__init__()
        self.administration_window = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.cancelButton.clicked.connect(self.openAdministrationPage)

    def openAdministrationPage(self):
        self.administration_window = AdministrationWindow.AdministrationWindow()
        self.administration_window.show()
        self.close()
