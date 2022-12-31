from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
)
from PySide6.QtWidgets import QLayout

from .color import Color
from . import the_hindus
from . import india_today
from . import times_of_india
from loguru import logger

logger.add("newsbytes.log", retention="3 days")


class GUI(QMainWindow):
    DEFAULT_WIN_SIZE = 1100, 600
    COLOR_CONTENT_SIZE = 500, 100

    def __init__(self):
        super().__init__()
        self.setWindowTitle("News Bytes")
        self.setFixedSize(QSize(*GUI.DEFAULT_WIN_SIZE))

        news_buttons_layout = QVBoxLayout()
        news_buttons_layout.addWidget(the_hindus.goto_button())
        news_buttons_layout.addWidget(india_today.goto_button())

        colors_layout = QVBoxLayout()
        colors_layout.addWidget(Color("orange", GUI.COLOR_CONTENT_SIZE))
        colors_layout.addWidget(Color("white", GUI.COLOR_CONTENT_SIZE))
        colors_layout.addWidget(Color("green", GUI.COLOR_CONTENT_SIZE))

        final_layout = QHBoxLayout()
        final_layout.addLayout(news_buttons_layout)
        final_layout.addLayout(colors_layout)

        widget = QWidget()
        widget.setLayout(final_layout)

        self.setCentralWidget(widget)
        logger.info("Initialized window")


def main():
    app = QApplication()
    window = GUI()
    window.show()
    app.exec()
