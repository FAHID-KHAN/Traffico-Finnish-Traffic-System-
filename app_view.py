from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QTableWidgetItem
from interface import Ui_MainWindow
from canvas import Canvas


class MainWindow(QMainWindow):
    def __init__(self, controller, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.controller = controller

        # init UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_canvas()

        self.handle_signals()

        # min window size
        self.setMinimumSize(1080, 860)

    def handle_signals(self):
        # change pages on clicked
        self.ui.main_button.clicked.connect(lambda: self.ui.stacked_widget.setCurrentWidget(self.ui.main_page))
        self.ui.cond_button.clicked.connect(lambda: self.ui.stacked_widget.setCurrentWidget(self.ui.cond_page))
        self.ui.msg_button.clicked.connect(lambda: self.ui.stacked_widget.setCurrentWidget(self.ui.msg_page))

        # send signals to the controller
        self.ui.main_submit_btn.clicked.connect(self.controller.submit_tasks)
        self.ui.cond_submit_btn.clicked.connect(self.controller.submit_conditions)
        self.ui.msg_submit_btn.clicked.connect(self.controller.submit_messages)

    def setup_canvas(self):
        self.canvas = Canvas(self.ui.results_page_1)
        self.toolbar = self.canvas.get_toolbar(self)

        # add the canvas and toolbar to an widget
        self.ui.plots_layout = QHBoxLayout()
        self.ui.plots_widget = QWidget()

        self.ui.canvas_layout = QVBoxLayout()
        self.ui.canvas_widget = QWidget()

        self.ui.canvas_layout.addWidget(self.toolbar)
        self.ui.canvas_layout.addWidget(self.canvas)
        self.ui.canvas_widget.setLayout(self.ui.canvas_layout)

        self.ui.plots_layout.addWidget(self.ui.canvas_widget)
        self.ui.plots_widget.setLayout(self.ui.plots_layout)
        self.ui.plots_widget.setParent(self.ui.results_page_1)

    def get_tasks_input(self):
        inputs = {}
        utc = "yyyy-MM-ddThh:mm:ssZ"
        inputs["location"] = self.ui.main_input_1.currentText()
        inputs["start_time"] = self.ui.main_input_2.dateTime().toString(utc)
        inputs["end_time"] = self.ui.main_input_3.dateTime().toString(utc)
        return inputs

    def get_conditions_input(self):
        inputs = {}
        inputs["location"] = self.ui.cond_input_1.currentText()
        inputs["precipitation"] = self.ui.cond_input_2.currentText()
        inputs["condition"] = self.ui.cond_input_3.currentText()
        inputs["hour"] = self.ui.buttonGroup.checkedButton().text()
        return inputs

    def get_messages_input(self):
        return self.ui.msg_input.currentText()

    def update_tasks_widget(self, data):
        print(data)

        # reset input form
        self.ui.main_input_1.setCurrentIndex(0)

        # add tasks per day bar plot
        self.canvas.clear()
        self.canvas.plot(data)

        # show results page
        self.ui.stacked_widget_1.setCurrentIndex(1)

    def update_conditions_widget(self, data):
        print(data)

        # reset input form
        self.ui.cond_input_1.setCurrentIndex(0)
        self.ui.cond_input_2.setCurrentIndex(0)
        self.ui.radioButton_1.setChecked(True)

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

        # add table data
        self.ui.tableWidget.setRowCount(len(data))
        for row, item in enumerate(data):
            self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(str(item["countryCode"])))
            self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(str(item["municipality"])))
            self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(str(item["road"])))
            self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(str(item["description"])))

        # show results page
        self.ui.stacked_widget_3.setCurrentIndex(1)
