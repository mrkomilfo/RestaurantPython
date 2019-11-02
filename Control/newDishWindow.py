from PyQt5 import QtWidgets
from View.newDish import Ui_MainWindow
import Control.administrationWindow as AdministrationWindow
from Models.Dish import Dish
from DB.dbHandler import dbHandler as DB
from MLM.PredictionMachine import PredictionMachine as PM


class NewDishWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(NewDishWindow, self).__init__()
        self.administration_window = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.typeComboBox.addItem("Не выбрано")
        self.ui.typeComboBox.addItem("Холодные закуски")
        self.ui.typeComboBox.addItem("Первое блюдо")
        self.ui.typeComboBox.addItem("Гарниры")
        self.ui.typeComboBox.addItem("Горячие блюда")
        self.ui.typeComboBox.addItem("Напитки")
        self.ui.typeComboBox.addItem("Десерты")

        self.ui.cancelButton.clicked.connect(self.open_administration_page)
        self.ui.addButton.clicked.connect(self.add_dish)
        self.ui.predictPriceButton.clicked.connect(self.predict_price)

    def open_administration_page(self):
        self.administration_window = AdministrationWindow.AdministrationWindow()
        self.administration_window.show()
        self.close()

    def add_dish(self):
        dish = Dish(self.ui.typeComboBox.currentText(), self.ui.nameEdit.text(), float(self.ui.priceEdit.text()),
                    int(self.ui.energyEdit.text()), int(self.ui.outputEdit.text()))
        DB.add_dish(dish)
        self.open_administration_page()

    def predict_price(self):
        dish_type = PM.get_code(self.ui.typeComboBox.currentText())
        energy = int(self.ui.energyEdit.text())
        output = int(self.ui.outputEdit.text())
        predicted_price = PM.predict([[dish_type, energy, output]])
        self.ui.priceEdit.setText(str(predicted_price))
