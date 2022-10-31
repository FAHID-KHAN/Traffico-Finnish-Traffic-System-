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
    update_tasks_widget(data)
        Updates the road maintainance page using the data from the Model.
    update_conditions_widget(data)
        Updates the road conditions page using the data from the Model.
    update_messages_widget(data)
        Updates the traffic messages page using the data from the Model.
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

        # send signals to the controller
        self.ui.main_submit_btn.clicked.connect(self.controller.submit_tasks)
        self.ui.cond_submit_btn.clicked.connect(self.controller.submit_conditions)
        self.ui.msg_submit_btn.clicked.connect(self.controller.submit_messages)


    def setup_canvas(self):
        # init canvas
        self.canvas = Canvas(self.ui.results_page_1)
        self.toolbar = self.canvas.get_toolbar(self)

        # layouts and widgets for the canvas and the toolbar
        self.ui.canvas_layout = QVBoxLayout()
        self.ui.canvas_widget = QWidget()

        # add the canvas and the toolbar to the layout and then to the widget
        self.ui.canvas_layout.addWidget(self.toolbar)
        self.ui.canvas_layout.addWidget(self.canvas)
        self.ui.canvas_widget.setLayout(self.ui.canvas_layout)

        # container layout and widget
        self.ui.container_layout = QHBoxLayout()
        self.ui.container_widget = QWidget()

        # add the canvas widget to the container layout and then to the widget
        self.ui.container_layout.addWidget(self.ui.canvas_widget)
        self.ui.container_widget.setLayout(self.ui.container_layout)

        # add the container widget to the road maintenance page
        self.ui.container_widget.setParent(self.ui.results_page_1)


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
        return self.ui.msg_input.currentText()


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
