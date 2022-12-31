from bs4 import BeautifulSoup
import requests
from PySide6.QtWidgets import QPushButton
from PySide6.QtGui import QIcon

URL = "https://www.thehindu.com/news/national/"
LOGO = "assets/thehindu-logo.svg"


def goto_button() -> QPushButton:
    icon = QIcon(LOGO)
    return QPushButton(icon, "The Hindus")


def get_homepage_soup() -> BeautifulSoup:
    r = requests.get(URL)
    return BeautifulSoup(r.content, "html.parser")


def scrape_homepage_links() -> list[str]:
    homepage_soup = get_homepage_soup()
