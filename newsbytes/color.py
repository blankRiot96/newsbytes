from PySide6.QtCore import QSize
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPalette, QColor


class Color(QWidget):
    def __init__(self, color, size):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        if size is not None:
            self.setFixedSize(QSize(*size))

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)
