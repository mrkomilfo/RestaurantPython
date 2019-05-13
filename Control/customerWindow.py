from PyQt5 import QtWidgets
from View.customer import Ui_MainWindow
import Control.enterWindow as EnterWindow
from Models.Menu import Menu
from main import DB


class CustomerWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(CustomerWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.enter_window = None
        self.ui.mainMenuButton.clicked.connect(self.openEnterPage)
        loaded_menu = DB.getMenu()
        self.menu = dict()
        self.menu.setdefault("Холодные закуски", Menu())
        self.menu.setdefault("Первое блюдо", Menu())
        self.menu.setdefault("Гарниры", Menu())
        self.menu.setdefault("Горячие блюда", Menu())
        self.menu.setdefault("Напитки", Menu())
        self.menu.setdefault("Десерты", Menu())
        for dish in loaded_menu.values():
            self.menu[dish.dish_type].add(dish)
        pass


    def openEnterPage(self):
        self.enter_window = EnterWindow.EnterWindow()
        self.enter_window.show()
        self.close()
