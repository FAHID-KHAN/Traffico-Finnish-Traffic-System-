from PyQt5.QtWidgets import QMainWindow
from interface import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # TODO: instantiate controller

        # init UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # add items to combo boxes
        self.add_combo_items()

        # change pages on clicked
        self.click_pages()

        # min window size
        # self.setMinimumSize(800, 640)

    def add_combo_items(self):
        location_items = [
        "-Select-",
        "All",
        "Municipalities",
        "State-roads",
        "Autori-oulu",
        "Autori-kuopio",
        "Paikannin-kuopio",
        ]
        self.ui.loc_input.addItems(location_items)
        self.ui.msg_input.addItems(location_items)

    def click_pages(self):
        self.ui.main_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.main_page))

        self.ui.cond_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.cond_page))

        self.ui.msg_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.msg_page))
