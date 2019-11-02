from PyQt5 import QtWidgets
from View.changePassword import Ui_MainWindow
import Control.administrationWindow as AdministrationWindow
import Control.authorizationWindow as AuthorizationWindow
from DB.dbHandler import dbHandler as DB


class ChangePasswordWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ChangePasswordWindow, self).__init__()
        self.administration_window = None
        self.authorization_window = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.cancelButton.clicked.connect(self.open_administration_page)
        self.ui.saveButton.clicked.connect(self.save_password)

    def open_administration_page(self):
        self.administration_window = AdministrationWindow.AdministrationWindow()
        self.administration_window.show()
        self.close()

    def open_authorization_page(self):
        self.authorization_window = AuthorizationWindow.AuthorizationWindow()
        self.authorization_window.show()
        self.close()

    def save_password(self):
        if self.ui.oldPasswordEdit.text() != DB.account.password:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage("Ошибка!", "Старый пароль введён неверно.")
            return
        elif self.ui.newPasswordEdit.text() != self.ui.passwordConfirmEdit.text():
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage("Ошибка!", "Пароли не совпадают.")
            return
        elif len(self.ui.newPasswordEdit.text()) < 4:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage("Ошибка!", "Пароль слишком короткий. Минимальная длинна: 4 символа.")
            return
        else:
            DB.change_password(DB.get_account().login, self.ui.newPasswordEdit.text())
            self.open_authorization_page()
