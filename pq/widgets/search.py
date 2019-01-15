from PySide2 import QtWidgets, QtCore
from multiprocessing.pool import ThreadPool
from multiprocessing import cpu_count

from pq.widgets.results import TableHeader


class SearchWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__()

        self.provider_list = None

        self.enter_button = QtWidgets.QPushButton()
        self.enter_button.setText("Search")
        self.enter_button.clicked.connect(self.search)

        self.search_field = QtWidgets.QLineEdit()
        self.search_field.returnPressed.connect(self.enter_button.click)

        self.layout = QtWidgets.QHBoxLayout()
        self.layout.addWidget(self.search_field)
        self.layout.addWidget(self.enter_button)

        self.setLayout(self.layout)

    @property
    def provider_list(self):
        return self.__provider_list

    @provider_list.setter
    def provider_list(self, providers):
        self.__provider_list = providers

    @QtCore.Slot()
    def search(self):
        # search_text = self.search_field.text()
        with ThreadPool(cpu_count()) as pool:
            pool.map(lambda p: p.get_page(), self.provider_list)

        row = 0
        for provider in self.provider_list:
            for match in provider.matches:
                self.results.table.setRowCount(row + 1)

                item = QtWidgets.QTableWidgetItem(match.description)
                self.results.table.setItem(
                    row, TableHeader.Description.value, item
                )

                item = QtWidgets.QTableWidgetItem(f"{match.price}")
                self.results.table.setItem(row, TableHeader.Price.value, item)

                item = QtWidgets.QTableWidgetItem(match.url)
                self.results.table.setItem(row, TableHeader.URL.value, item)

                item = QtWidgets.QTableWidgetItem(match.image)
                self.results.table.setItem(row, TableHeader.Image.value, item)

                row = row + 1
