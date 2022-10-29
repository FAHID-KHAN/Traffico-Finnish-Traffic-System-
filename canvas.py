import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar


class Canvas(FigureCanvas):
    def __init__(self, parent):
        self.fig, self.ax = plt.subplots(figsize=(1, 1), dpi=100)
        super().__init__(self.fig)
        self.setParent(parent)
        plt.ion()

    def get_toolbar(self, parent):
        return NavigationToolbar(self, parent)

    def plot(self, data):
        self.ax.bar(range(len(data)),
                    list(data.values()),
                    align="center",
                    alpha=0.5)
        self.ax.set_xticks(range(len(data)), list(data.keys()))
        self.ax.set_xlabel("Tasks")
        self.ax.set_ylabel("Frequency")
        self.ax.set_title("Tasks per day")

    def clear(self):
        self.ax.clear()
