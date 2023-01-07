from bs4 import BeautifulSoup
import requests
from PySide6.QtWidgets import QPushButton, QVBoxLayout, QLabel, QSpacerItem
from PySide6.QtGui import QIcon, QImage
from .states import State
from loguru import logger
from .color import Color
from typing import Iterator

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


def scrape_all_text(url_soup: BeautifulSoup) -> Iterator:
    for para in url_soup.find_all("p"):
        yield para.getText()


def get_article_ui(url: str) -> QVBoxLayout:
    r = requests.get(url)
    logger.debug(url)
    url_soup = BeautifulSoup(r.content, "html.parser")
    layout = QVBoxLayout()
    layout.addSpacing(0)

    for story in url_soup.find_all("a"):
        if story.get("href") is None or not story.get("href").startswith(url):
            continue

        story_req = requests.get(story.get("href"))
        story_soup = BeautifulSoup(story_req.content, "html.parser")
        for text in scrape_all_text(story_soup):
            layout.addWidget(QLabel(text=text))

    layout.addWidget(Color("blue", (400, 32)))
    return layout


def get_homepage_layout(n_articles: int) -> QVBoxLayout:
    layout = QVBoxLayout()
    layout.addSpacing(0)
    links = scrape_links(n_articles)

    for link in links:
        ui = get_article_ui(link)
        layout.addLayout(ui)

    return layout
