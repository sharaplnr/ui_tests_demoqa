import pytest
from playwright.sync_api import Page, Playwright, BrowserContext

def pytest_addoption(parser) -> None:
    parser.addoption("--browser", action="store", default="chrome", help="Выбор браузера")
    parser.addoption("--device", action="store", default="ios", help="Выбор девайса")
    parser.addoption("--headless", action="store", default="False", help="Отображение браузера")

@pytest.fixture
def page_init(playwright: Playwright, page: Page):

