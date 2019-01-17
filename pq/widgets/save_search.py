from PySide2 import QtCore
from PySide2.QtWidgets import (
    QWidget,
    QFormLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QHBoxLayout,
)

from pq.db import Database


class SaveSearchWidget(QWidget):
    def __init__(self):
        super().__init__()

        self._db = Database()

        self.form = QFormLayout()
        row_1 = QHBoxLayout()
        row_2 = QHBoxLayout()
        row_3 = QHBoxLayout()
        row_4 = QHBoxLayout()

        self.name = QLineEdit()
        row_1.addWidget(QLabel("Name:"))
        row_1.addWidget(self.name)

        self.tag = QLineEdit()
        row_2.addWidget(QLabel("Tag:"))
        row_2.addWidget(self.tag)

        self.url = QLineEdit()
        row_3.addWidget(QLabel("URL:"))
        row_3.addWidget(self.url)

        enter_button = QPushButton()
        enter_button.setText("Save")
        enter_button.clicked.connect(self.save)
        row_4.addWidget(enter_button)

        self.form.addRow(row_1)
        self.form.addRow(row_2)
        self.form.addRow(row_3)
        self.form.addRow(row_4)
        self.setLayout(self.form)

    @QtCore.Slot()
    def save(self):
        search = {
            "name": self.name.text(),
            "tag": self.tag.text(),
            "url": self.url.text(),
        }
        self._db.save_search(search)
        self.load_search.clear_form()
        self.load_search.load_searches()

    def __exit__(self):
        self._db.close()
