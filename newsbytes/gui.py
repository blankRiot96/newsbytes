from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QStackedWidget,
    QScrollArea,
    QHBoxLayout,
)
from .states import State
from . import homepage
from . import the_hindus
from loguru import logger
from .color import Color

logger.add("newsbytes.log", rotation="5 KB")


class GUI(QMainWindow):
    DEFAULT_WIN_SIZE = 1100, 600
    COLOR_CONTENT_SIZE = 500, 100

    def __init__(self):
        super().__init__()
        self.setWindowTitle("News Bytes")
        self.setFixedSize(QSize(*GUI.DEFAULT_WIN_SIZE))

        self.state = None
        self.widget = QStackedWidget()

        self.create_content_widgets()
        self.state_tree = {
            State.HOMEPAGE: self.homepage_widget,
            State.THE_HINDUS: self.the_hindus_widget,
        }
        self.prev_widget = None
        self.switch_state(State.HOMEPAGE)

        self.setCentralWidget(self.widget)
        logger.info("Initialized window")

    def create_content_widgets(self) -> None:
        self.homepage_widget = QScrollArea()
        self.the_hindus_widget = QScrollArea()
        self.homepage_widget.setLayout(homepage.get_homepage_layout(self))
        self.the_hindus_widget.setLayout(the_hindus.get_homepage_layout(3))

    def switch_state(self, state: State) -> None:
        self.state = state
        self.widget.removeWidget(self.prev_widget)

        self.widget.addWidget(self.state_tree[state])
        self.prev_widget = self.state_tree[state]
        logger.info(f"Switched state to: {state}")


def main():
    app = QApplication()
    window = GUI()
    window.show()
    app.exec()
