import pkgutil
import importlib
from PySide2 import QtWidgets

import pq.providers as providers


class ProviderListWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.provider_list = providers.get_all()

        self.widget = QtWidgets.QListWidget()
        self.widget.addItems([provider.name for provider in self.provider_list])

        self.widget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.widget)
        self.setLayout(layout)
