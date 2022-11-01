import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication

from app_model import Model
from app_view import MainWindow


class Controller:
    """
    Controller class of the MVC design pattern.

    This class is responsible for performing logic and maintain and control
    the communication between the View and Model classes.

    Attributes
    ----------
    _app: PyQt5.QtWidgets.QApplication
        The PyQt5 application object for creating the app instance.
    _model: app_model.Model
        The Model object that contains the data.
    _view: app_view.MainWindow
        The MainWindow object that contains the GUI.

    Methods
    -------
    submit_tasks()
        On road maintainance submit-button-press the user input is taken,
        the data is parsed from the API, and the result is shown as bar plot.
    submit_conditions()
        On road conditions submit-button-press the user input is taken,
        the data is parsed from the API, and the result is shown as widgets.
    submit_messages()
        On traffic messages submit-button-press the user input is taken,
        the data is parsed from the API, and the result is shown as table.
    """

    def __init__(self):
        self._app = QtWidgets.QApplication(sys.argv)

        # external style sheet
        with open("assets/style.css","r") as f:
            self._app.setStyleSheet(f.read())

        self._model = Model()
        self._view = MainWindow(self)


    def submit_tasks(self):
        self._model.get_tasks_data(self._view.get_tasks_input())
        self._view.update_tasks_widget(self._model.tasks_per_day)


    def submit_conditions(self):
        self._model.get_conditions_data(self._view.get_conditions_input())
        self._view.update_conditions_widget(self._model.conditions_data)


    def submit_messages(self):
        self._model.get_messages_data(self._view.get_messages_input())
        self._view.update_messages_widget(self._model.messages_data)


    def run(self):
        self._view.show()
        return self._app.exec_()


if __name__ == "__main__":
    controller = Controller()
    sys.exit(controller.run())
