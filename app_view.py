import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from interface import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # init UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # add items to combo boxes
        self.add_items()

        # change pages on clicked
        self.click_pages()

        # min window size
        # self.setMinimumSize(800, 640)

    def add_items(self):
        location_items = [
        "-Select-",
        "All",
        "Municipalities",
        "State-roads",
        "Autori-oulu",
        "Autori-kuopio",
        "Paikannin-kuopio",
        ]
        self.ui.locCombo.addItems(location_items)
        self.ui.msgCombo.addItems(location_items)

    def click_pages(self):
        self.ui.mainButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.mainPage))

        self.ui.condButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.condPage))

        self.ui.msgButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.msgPage))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
