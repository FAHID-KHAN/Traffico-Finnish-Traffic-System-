import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication

from app_model import Model
from app_view import MainWindow


class Controller:
    def __init__(self):
        self._app = QtWidgets.QApplication(sys.argv)
        self._model = Model()
        self._view = MainWindow(self)

    def submit_tasks(self):
        self._model.get_tasks_data()
        self._view.ui.stacked_widget_1.setCurrentIndex(1)
        self._view.update_tasks_widget(self._model.tasks_data)

    def submit_conditions(self):
        self._model.get_conditions_data()
        self._view.ui.stacked_widget_2.setCurrentIndex(1)
        self._view.update_conditions_widget(self._model.conditions_data)

    def submit_messages(self):
        self._model.get_message_data(self._view.ui.msg_input.currentText())
        self._view.ui.msg_input.setCurrentIndex(0)
        self._view.ui.stacked_widget_3.setCurrentIndex(1)
        self._view.update_messages_widget(self._model.message_data)

    def run(self):
        self._view.show()
        return self._app.exec_()


if __name__ == "__main__":
    controller = Controller()
    sys.exit(controller.run())
