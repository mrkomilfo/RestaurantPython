import sys
from PyQt5 import QtWidgets
import Control.enterWindow as EnterWindow
from MLM.PredictionMachine import PredictionMachine


def main():
    app = QtWidgets.QApplication([])
    application = EnterWindow.EnterWindow()
    application.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    sys.exit(main())
