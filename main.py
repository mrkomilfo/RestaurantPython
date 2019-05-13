import sys
from PyQt5 import QtWidgets
import Control.enterWindow as EnterWindow
from Models.Menu import Menu


class DB:
    menu = Menu.get_start_menu()

    @staticmethod
    def getMenu():
        return DB.menu


def main():
    app = QtWidgets.QApplication([])
    application = EnterWindow.EnterWindow()
    application.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    sys.exit(main())
