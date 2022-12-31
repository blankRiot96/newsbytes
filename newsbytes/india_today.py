from PySide6.QtWidgets import QPushButton
from PySide6.QtGui import QIcon

LOGO = "assets/india-today.png"


def goto_button() -> QPushButton:
    icon = QIcon(LOGO)
    return QPushButton(icon, "India Today")
