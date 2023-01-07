from bs4 import BeautifulSoup
import requests
from PySide6.QtWidgets import QPushButton, QVBoxLayout, QLabel
from PySide6.QtGui import QIcon, QImage
from .states import State
from loguru import logger
from .color import Color

URL = "https://www.thehindu.com/news/national/"
LOGO = "assets/thehindu-logo.svg"
MAX_IMAGES_PER_ARTICLE = 3


def goto_button(gui_obj) -> QPushButton:
    icon = QIcon(LOGO)
    button = QPushButton(icon, "The Hindus")
    button.clicked.connect(lambda: gui_obj.switch_state(State.THE_HINDUS))

    return button


def get_homepage_soup() -> BeautifulSoup:
    r = requests.get(URL)
    return BeautifulSoup(r.content, "html.parser")


def scrape_links(n_articles: int) -> list[str]:
    links = []
    homepage_soup = get_homepage_soup()
    for link in homepage_soup.find_all("a", limit=n_articles):
        href: str | None = link.get("href")
        if href is None:
            continue

        if href.startswith(URL):
            links.append(href)

    return links


def get_article_ui(url: str) -> QVBoxLayout:
    r = requests.get(url)
    url_soup = BeautifulSoup(r.content, "html.parser")
    layout = QVBoxLayout()

    img_soups = url_soup.find_all("img")
    img_soups = img_soups[:MAX_IMAGES_PER_ARTICLE]
    for i, img_soup in enumerate(img_soups):
        if i == 1:
            continue
        try:
            img_bytes = requests.get(img_soup.get("src"))
        except:
            continue
        logger.info(img_bytes.content)
        img_label = QLabel()
        q_img = QImage(img_bytes.content)
        if q_img.isNull:
            continue
        img_label.setPixmap(QImage(img_bytes.content))
        layout.addWidget(img_label)

    layout.addWidget(Color("blue", (400, 32)))
    return layout


def get_homepage_layout(n_articles: int) -> QVBoxLayout:
    layout = QVBoxLayout()
    links = scrape_links(n_articles)

    for link in links:
        ui = get_article_ui(link)
        layout.addLayout(ui)

    return layout
