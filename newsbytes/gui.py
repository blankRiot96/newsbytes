from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
)
from .states import State
from . import homepage
from . import the_hindus
from loguru import logger

logger.add("newsbytes.log", rotation="5 KB")


def clear_layout(layout):
    while layout.count():
        child = layout.takeAt(0)
        if child.widget():
            child.widget().deleteLater()


class GUI(QMainWindow):
    DEFAULT_WIN_SIZE = 1100, 600
    COLOR_CONTENT_SIZE = 500, 100

    def __init__(self):
        super().__init__()
        self.setWindowTitle("News Bytes")
        self.setFixedSize(QSize(*GUI.DEFAULT_WIN_SIZE))

        self.state = None
        self.widget = QWidget()
        self.switch_state(State.HOMEPAGE)

        self.setCentralWidget(self.widget)
        logger.info("Initialized window")

    def switch_state(self, state: State) -> None:
        self.state = state

        if self.widget.layout() is not None:
            clear_layout(self.widget.layout())

        if self.state == State.HOMEPAGE:
            self.widget.setLayout(homepage.get_homepage_layout(self))
        elif self.state == State.THE_HINDUS:
            self.widget.setLayout(the_hindus.get_homepage_layout())
        logger.info(f"Switched state to: {state}")


def main():
    app = QApplication()
    window = GUI()
    window.show()
    app.exec()
