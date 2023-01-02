from PySide6.QtWidgets import (
    QVBoxLayout,
    QHBoxLayout,
)

from . import the_hindus
from . import india_today

from .color import Color


def get_homepage_layout(gui_obj) -> QHBoxLayout:
    news_buttons_layout = QVBoxLayout()
    news_buttons_layout.addWidget(the_hindus.goto_button(gui_obj))
    news_buttons_layout.addWidget(india_today.goto_button(gui_obj))

    colors_layout = QVBoxLayout()
    colors_layout.addWidget(Color("orange", gui_obj.COLOR_CONTENT_SIZE))
    colors_layout.addWidget(Color("white", gui_obj.COLOR_CONTENT_SIZE))
    colors_layout.addWidget(Color("green", gui_obj.COLOR_CONTENT_SIZE))

    final_layout = QHBoxLayout()
    final_layout.addLayout(news_buttons_layout)
    final_layout.addLayout(colors_layout)

    return final_layout
