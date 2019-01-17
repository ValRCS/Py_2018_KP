from enum import Enum
from multiprocessing.pool import ThreadPool
from multiprocessing import cpu_count
from PySide2 import QtCore
from PySide2.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QFormLayout,
    QLabel,
    QCheckBox,
    QPushButton,
    QTableWidgetItem,
)


from pq.db import Database
from pq.providers import ss
from pq.widgets.results import TableHeader as result_header


class TableHeader(Enum):
    Selected = 0
    ID = 1
    Tag = 2
    Name = 3
    URL = 4


class LoadSearchWidget(QWidget):
    header_labels = [header.name for header in TableHeader]

    def __init__(self):
        super().__init__()

        self.db = Database()

        self.form = QFormLayout()

        # TODO: enable header row and correctly align it with the loaded result row
        # columns
        #         header_row = QHBoxLayout()
        #         for header in self.header_labels:
        #             header_row.addWidget(QLabel(header))
        #         self.form.addRow(header_row)

        self.search_button = QPushButton()
        self.search_button.setText("Search")
        self.search_button.clicked.connect(self.search)

        layout = QVBoxLayout()
        layout.addLayout(self.form)
        layout.addWidget(self.search_button)
        self.setLayout(layout)

        self.load_searches()

    def clear_form(self):
        print("[DEBUG] Clearing list of loaded searches")
        # Leave the header row
        while self.form.rowCount() > 0:
            self.form.removeRow(0)

    @QtCore.Slot()
    def load_searches(self):
        print("[DEBUG] Loading saved searches")
        searches = self.db.get_saved_searches()
        if searches is None:
            return

        for id, name, tag, url in searches:
            row = QHBoxLayout()
            row.enabled = QCheckBox()
            row.id = id
            row.url = url

            row.addWidget(row.enabled)
            row.addWidget(QLabel(f"{id}"))
            row.addWidget(QLabel(tag))
            row.addWidget(QLabel(name))
            row.addWidget(QLabel(url))

            self.form.addRow(row)

    @QtCore.Slot()
    def search(self):
        ss_provider = ss.Provider()
        urls = []

        rows = (self.form.itemAt(i) for i in range(self.form.count()))
        for row in rows:
            if row.enabled.isChecked():
                urls.append(row.url)

        with ThreadPool(cpu_count()) as pool:
            pool.map(lambda url: ss_provider.get_page(url), urls)

        row = 0
        for match in ss_provider.matches:
            self.results.table.setRowCount(row + 1)

            item = QTableWidgetItem(match.description)
            self.results.table.setItem(row, result_header.Description.value, item)

            item = QTableWidgetItem(f"{match.price}")
            self.results.table.setItem(row, result_header.Price.value, item)

            item = QTableWidgetItem(match.url)
            self.results.table.setItem(row, result_header.URL.value, item)

            item = QTableWidgetItem(match.image)
            self.results.table.setItem(row, result_header.Image.value, item)

            row = row + 1

        # Prepare provider for the next search
        ss_provider.matches = []

    def __exit__(self):
        self._db.close()
