import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication

from app_model import Model
from app_view import MainWindow


class Controller:
    def __init__(self):
        self._app = QtWidgets.QApplication(sys.argv)

        # TODO: add external style sheet
        # with open("assets/style.css","r") as f:
        #     self._app.setStyleSheet(f.read())
        
        self._model = Model()
        self._view = MainWindow(self)

    def submit_tasks(self):
        input = self._view.get_tasks_input()
        data = self._model.get_tasks_data(input)
        self._view.update_tasks_widget(data)

    def submit_conditions(self):
        input = self._view.get_conditions_input()
        data = self._model.get_conditions_data(input)
        self._view.update_conditions_widget(data)

    def submit_messages(self):
        input = self._view.get_messages_input()
        data = self._model.get_messages_data(input)
        self._view.update_messages_widget(data)

    def run(self):
        self._view.show()
        return self._app.exec_()


if __name__ == "__main__":
    controller = Controller()
    sys.exit(controller.run())
