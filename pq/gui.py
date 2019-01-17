import sys
from PySide2 import QtWidgets

from pq import __name__, __version__

from pq.widgets.providers import ProviderListWidget
from pq.widgets.results import ResultsWidget
from pq.widgets.save_search import SaveSearchWidget
from pq.widgets.load_search import LoadSearchWidget


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        save_search = SaveSearchWidget()
        load_search = LoadSearchWidget()
        save_search.load_search = load_search
        results = ResultsWidget()
        load_search.results = results

        save_search.show()
        load_search.show()
        results.show()

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(save_search)
        layout.addWidget(load_search)
        layout.addWidget(results)

        central_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(central_widget)
        central_widget.setLayout(layout)

        self.setWindowTitle(__name__)


def run():
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName(__name__)
    app.setDesktopFileName(__name__)
    app.setApplicationVersion(__version__)

    main_window = MainWindow()
    main_window.show()

    return app.exec_()
