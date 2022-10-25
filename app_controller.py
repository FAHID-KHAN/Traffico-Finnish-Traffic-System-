import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication

from app_model import Model
from app_view import MainWindow


class Controller:
    def __init__(self):
        self._app = QtWidgets.QApplication(sys.argv)
        self._model = Model()
        self._view = MainWindow()

    def run(self):
        self._view.show()
        return self._app.exec_()


if __name__ == "__main__":
    controller = Controller()
    sys.exit(controller.run())