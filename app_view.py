from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QTableWidgetItem
from interface import Ui_MainWindow
from canvas import Canvas


class MainWindow(QMainWindow):
    """
    MainWindow class which is the View of the MVC design pattern.

    This class sets up the GUI. The user interacts only with this class.
    It sends all signals (button presses, inputs, etc.) to the Controller class.

    Attributes
    ----------
    controller: app_controller.Controller
        The Controller object for sending the user input to it.
    ui: interface.Ui_MainWindow
        The main GUI object that has what the user see.
    canvas: canvas.Canvas
        The Canvas object for making plots.
    toolbar: matplotlib.backends.backend_qt.NavigationToolbar2QT
        The toolbat object on top of the plots.

    Methods
    -------
    handle_signals()
        Handles all the button clicked signals from the GUI using slots from
        the GUI itself or from the Controller in case of input submit buttons.
    setup_canvas()
        Sets up the canvas for plotting bar chart on road maintainance page.
    get_tasks_input()
        Gets the user inputs from the road maintainance input form.
    get_conditions_input()
        Gets the user inputs from the road conditions input form.
    get_messages_input()
        Gets the user input from the traffic messages input form.
    get_combined_input()
        Gets the user input from the combined reports input form.
    update_tasks_widget(data)
        Updates the road maintainance page using the data from the Model.
    update_conditions_widget(data)
        Updates the road conditions page using the data from the Model.
    update_messages_widget(data)
        Updates the traffic messages page using the data from the Model.
    update_combined_widget(tasks_data, conditions_data, messages_data, weather_data)
        Updates the combined reports page using the data from the Model.
    """

    def __init__(self, controller, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.controller = controller

        # init UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # set up the canvas
        self.setup_canvas()

        # handle all the button press signals
        self.handle_signals()

        # set min window size
        self.setMinimumSize(1080, 860)


    def handle_signals(self):
        # change pages on clicked
        self.ui.main_button.clicked.connect(lambda: self.ui.stacked_widget.setCurrentWidget(self.ui.main_page))
        self.ui.cond_button.clicked.connect(lambda: self.ui.stacked_widget.setCurrentWidget(self.ui.cond_page))
        self.ui.msg_button.clicked.connect(lambda: self.ui.stacked_widget.setCurrentWidget(self.ui.msg_page))
        self.ui.comb_button.clicked.connect(lambda: self.ui.stacked_widget.setCurrentWidget(self.ui.comb_page))

        # send signals to the controller
        self.ui.main_submit_btn.clicked.connect(self.controller.submit_tasks)
        self.ui.cond_submit_btn.clicked.connect(self.controller.submit_conditions)
        self.ui.msg_submit_btn.clicked.connect(self.controller.submit_messages)
        self.ui.comb_submit_btn.clicked.connect(self.controller.submit_combined)


    def setup_canvas(self):
        # init canvas
        self.canvas = Canvas()
        self.toolbar = self.canvas.get_toolbar()
        # 2nd canvas for combined report
        self.canvas_2 = Canvas()
        self.toolbar_2 = self.canvas_2.get_toolbar()

        # layouts for the canvas and the toolbar
        self.ui.canvas_layout = QVBoxLayout()
        self.ui.canvas_layout_2 = QVBoxLayout()

        # add the canvas and the toolbar to the layout and then to the widget
        self.ui.canvas_layout.addWidget(self.toolbar)
        self.ui.canvas_layout.addWidget(self.canvas)
        self.ui.canvas_widget.setLayout(self.ui.canvas_layout)
        self.ui.canvas_layout_2.addWidget(self.toolbar_2)
        self.ui.canvas_layout_2.addWidget(self.canvas_2)
        self.ui.canvas_widget_2.setLayout(self.ui.canvas_layout_2)


    def get_tasks_input(self):
        inputs = {}
        # UTC datetime format string (the API requires this format)
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
        # radio button input is taken from their button group
        inputs["hour"] = self.ui.buttonGroup.checkedButton().text()
        return inputs


    def get_messages_input(self):
        inputs = {}
        inputs["type"] = self.ui.msg_input.currentText()
        return inputs


    def get_combined_input(self):
        inputs = {}

        utc = "yyyy-MM-ddThh:mm:ssZ"
        inputs["location"] = self.ui.comb_input_1.currentText()
        inputs["type"] = self.ui.comb_input_2.currentText()
        inputs["start_time"] = self.ui.comb_input_3.dateTime().toString(utc)
        inputs["end_time"] = self.ui.comb_input_4.dateTime().toString(utc)

        # default inputs for unspecified items (taken from road conditions page)
        inputs["precipitation"] = self.ui.cond_input_2.currentText()
        inputs["condition"] = self.ui.cond_input_3.currentText()
        inputs["hour"] = self.ui.buttonGroup.checkedButton().text()

        return inputs


    def update_tasks_widget(self, data):
        # DEBUG: prints the data to the shell
        print(data)

        # reset input form
        # self.ui.main_input_1.setCurrentIndex(0)

        # clear the canvas and add tasks per day bar plot
        self.canvas.clear()
        self.canvas.plot(data)

        # switch to the results page
        self.ui.stacked_widget_1.setCurrentIndex(1)


    def update_conditions_widget(self, data):
        # DEBUG: prints the data to the shell
        print(data)

        # reset input form
        # self.ui.cond_input_1.setCurrentIndex(0)
        # self.ui.cond_input_2.setCurrentIndex(0)
        # self.ui.radioButton_1.setChecked(True)

        # add results data to the square widgets
        self.ui.cond_data_1.setText(str(data["roadTemperature"]))
        self.ui.cond_data_2.setText(str(data["temperature"]))
        self.ui.cond_data_3.setText(str(data["windSpeed"]))
        self.ui.cond_data_4.setText(str(data["windDirection"]))
        self.ui.cond_data_5.setText(str(data["type"]))
        self.ui.cond_data_6.setText(str(data["reliability"]))

        # switch to the results page
        self.ui.stacked_widget_2.setCurrentIndex(1)


    def update_messages_widget(self, data):
        # DEBUG: prints the data to the shell
        print(data)

        # reset input form
        # self.ui.msg_input.setCurrentIndex(0)

        # add table data row by row to the tableWidget
        self.ui.tableWidget.setRowCount(len(data))
        for row, item in enumerate(data):
            self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(str(item["countryCode"])))
            self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(str(item["municipality"])))
            self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(str(item["road"])))
            self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(str(item["description"])))

        # switch to the results page
        self.ui.stacked_widget_3.setCurrentIndex(1)


    def update_combined_widget(self, tasks_data, conditions_data, messages_data, weather_data):
        # DEBUG: prints the data to the shell
        print(weather_data)

        # reset input form
        # self.ui.msg_input.setCurrentIndex(0)


        # add weather data
        self.ui.weather_data_1.setText(str(weather_data["t2m"]))
        self.ui.weather_data_2.setText(str(weather_data["ws_10min"]))
        self.ui.weather_data_3.setText(str(weather_data["n_man"]))

        # add road maintainance plots
        self.canvas_2.clear()
        self.canvas_2.plot(tasks_data)

        # add road conditions data
        self.ui.cond_data_7.setText(str(conditions_data["roadTemperature"]))
        self.ui.cond_data_8.setText(str(conditions_data["temperature"]))
        self.ui.cond_data_9.setText(str(conditions_data["windSpeed"]))
        self.ui.cond_data_10.setText(str(conditions_data["windDirection"]))
        self.ui.cond_data_11.setText(str(conditions_data["type"]))
        self.ui.cond_data_12.setText(str(conditions_data["reliability"]))

        # add traffic mesages table data
        self.ui.tableWidget_2.setRowCount(len(messages_data))
        for row, item in enumerate(messages_data):
            self.ui.tableWidget_2.setItem(row, 0, QTableWidgetItem(str(item["countryCode"])))
            self.ui.tableWidget_2.setItem(row, 1, QTableWidgetItem(str(item["municipality"])))
            self.ui.tableWidget_2.setItem(row, 2, QTableWidgetItem(str(item["road"])))
            self.ui.tableWidget_2.setItem(row, 3, QTableWidgetItem(str(item["description"])))

        # switch to the results page
        self.ui.stacked_widget_4.setCurrentIndex(1)
