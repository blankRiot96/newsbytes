from bs4 import BeautifulSoup
import requests
from PySide6.QtWidgets import QPushButton, QVBoxLayout
from PySide6.QtGui import QIcon
from .states import State

URL = "https://www.thehindu.com/news/national/"
LOGO = "assets/thehindu-logo.svg"


def goto_button(gui_obj) -> QPushButton:
    icon = QIcon(LOGO)
    button = QPushButton(icon, "The Hindus")
    button.clicked.connect(lambda: gui_obj.switch_state(State.THE_HINDUS))

    return button


def get_homepage_soup() -> BeautifulSoup:
    r = requests.get(URL)
    return BeautifulSoup(r.content, "html.parser")


def scrape_homepage_links() -> list[str]:
    homepage_soup = get_homepage_soup()
    for link in homepage_soup.find_all("a"):
        print(link.get("href"))


def get_homepage_layout() -> QVBoxLayout:
    return QVBoxLayout()
