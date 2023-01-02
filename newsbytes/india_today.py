from PySide6.QtWidgets import QPushButton
from PySide6.QtGui import QIcon
from .states import State

LOGO = "assets/india-today.png"


def goto_button(gui_obj) -> QPushButton:
    icon = QIcon(LOGO)
    button = QPushButton(icon, "India Today")
    button.clicked.connect(lambda: gui_obj.switch_state(State.INDIA_TODAY))

    return button
