from enum import Enum
from PySide2 import QtWidgets, QtCore
import webbrowser


class TableHeader(Enum):
    Image = 0
    Description = 1
    Price = 2
    URL = 3


class ResultsWidget(QtWidgets.QWidget):
    header_labels = [header.name for header in TableHeader]

    def __init__(self):
        super().__init__()

        self.table = QtWidgets.QTableWidget()
        self.table.setRowCount(0)
        self.table.setColumnCount(len(TableHeader))
        self.table.setHorizontalHeaderLabels(self.header_labels)
        self.table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.table.cellClicked.connect(self.open_url)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.table)
        self.setLayout(self.layout)

    @QtCore.Slot()
    def open_url(self, row, column):
        if column == TableHeader.URL.value:
            item = self.table.item(row, TableHeader.URL.value)
            webbrowser.open_new_tab(item.text())
