import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar


class Canvas(FigureCanvas):
    """
    Canvas class for plotting charts.

    This class sets up the canvas and plots bar chart using the data from the
    user.

    Attributes
    ----------
    fig: matplotlib.figure.Figure
        The figure object to hold the entire plot.
    ax: matplotlib.axes._subplots.AxesSubplot
        The axes object for the plot.

    Methods
    -------
    get_toolbar(parent=None)
        Returns the toolbar widget to the GUI.
    plot(data)
        Plots the bar chart from the data parameter.
    clear()
        Clears the current plot.
    """

    def __init__(self):
        # init figure and axes
        self.fig, self.ax = plt.subplots(figsize=(1, 1), dpi=100)
        super().__init__(self.fig)


    def get_toolbar(self, parent=None):
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
        # interactive mode on
        plt.ion()


    def clear(self):
        self.ax.clear()
