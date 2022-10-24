import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from interface import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # init UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Add items to combo boxes
        self.ui.locCombo.addItems([
                                "-Select-",
                                "All",
                                "Municipalities",
                                "State-roads",
                                "Autori-oulu",
                                "Autori-kuopio",
                                "Paikannin-kuopio",
        ])
        self.ui.msgCombo.addItems([
                                "-Select-",
                                "All",
                                "Municipalities",
                                "State-roads",
                                "Autori-oulu",
                                "Autori-kuopio",
                                "Paikannin-kuopio",
        ])

        # Pages
        self.click_pages()

        # min window size
        # self.setMinimumSize(800, 640)

        # show window
        self.show()

    def click_pages(self):
        self.ui.mainButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.mainPage))

        self.ui.condButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.condPage))

        self.ui.msgButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.msgPage))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
