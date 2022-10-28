from PyQt5.QtWidgets import QMainWindow
from interface import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, controller, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.controller = controller

        # init UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.handle_signals()

        # min window size
        # self.setMinimumSize(800, 700)

    def handle_signals(self):
        # change pages on clicked
        self.ui.main_button.clicked.connect(lambda: self.ui.stacked_widget.setCurrentWidget(self.ui.main_page))
        self.ui.cond_button.clicked.connect(lambda: self.ui.stacked_widget.setCurrentWidget(self.ui.cond_page))
        self.ui.msg_button.clicked.connect(lambda: self.ui.stacked_widget.setCurrentWidget(self.ui.msg_page))

        # send signals to the controller
        self.ui.main_submit_btn.clicked.connect(self.controller.submit_tasks)
        self.ui.cond_submit_btn.clicked.connect(self.controller.submit_conditions)
        self.ui.msg_submit_btn.clicked.connect(self.controller.submit_messages)

    def get_tasks_input(self):
        return

    def get_conditions_input(self):
        return

    def get_messages_input(self):
        return self.ui.msg_input.currentText()

    def update_tasks_widget(self, data):
        print(data)

        # reset input form
        self.ui.main_input_1.setCurrentIndex(0)

        # TODO: update results data

        # show results page
        self.ui.stacked_widget_1.setCurrentIndex(1)

    def update_conditions_widget(self, data):
        print(data)

        # reset input form
        self.ui.cond_input_1.setCurrentIndex(0)
        self.ui.cond_input_2.setCurrentIndex(0)

        # update results data
        self.ui.cond_data_1.setText(str(data["roadTemperature"]))
        self.ui.cond_data_2.setText(str(data["temperature"]))
        self.ui.cond_data_3.setText(str(data["windSpeed"]))
        self.ui.cond_data_4.setText(str(data["windDirection"]))
        self.ui.cond_data_5.setText(str(data["type"]))
        self.ui.cond_data_6.setText(str(data["reliability"]))

        # show results page
        self.ui.stacked_widget_2.setCurrentIndex(1)

    def update_messages_widget(self, data):
        print(data)

        # reset input form
        self.ui.msg_input.setCurrentIndex(0)

        # TODO: update results data

        # show results page
        self.ui.stacked_widget_3.setCurrentIndex(1)
