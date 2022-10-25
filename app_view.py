from PyQt5.QtWidgets import QMainWindow
from interface import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, controller, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.controller = controller

        # init UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # add items to combo boxes
        self.add_combo_items()

        # change pages on clicked
        self.click_pages()

        # Send signals to the controller
        self.ui.msg_submit_btn.clicked.connect(self.controller.submit_message)

        # min window size
        # self.setMinimumSize(800, 640)

    def add_combo_items(self):
        locations = [
            "",
            "All",
            "Municipalities",
            "State-roads",
            "Autori-oulu",
            "Autori-kuopio",
            "Paikannin-kuopio",
            ]
        msg_types = [
            "",
            "TRAFFIC_ANNOUNCEMENT",
            "EXEMPTED_TRANSPORT",
            "WEIGHT_RESTRICTION",
            "ROAD_WORK",
            ]
        self.ui.loc_input.addItems(locations)
        self.ui.msg_input.addItems(msg_types)

    def click_pages(self):
        self.ui.main_button.clicked.connect(lambda: self.ui.stacked_widget.setCurrentWidget(self.ui.main_page))

        self.ui.cond_button.clicked.connect(lambda: self.ui.stacked_widget.setCurrentWidget(self.ui.cond_page))

        self.ui.msg_button.clicked.connect(lambda: self.ui.stacked_widget.setCurrentWidget(self.ui.msg_page))
