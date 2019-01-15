import sys
from PySide2 import QtWidgets

from pq import __name__, __version__

from widgets.search import SearchWidget
from widgets.providers import ProviderListWidget
from widgets.results import ResultsWidget


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        results = ResultsWidget()
        providers = ProviderListWidget()
        search = SearchWidget()

        search.provider_list = providers.provider_list
        search.results = results

        providers.show()
        search.show()
        results.show()

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(search)
        layout.addWidget(providers)
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
