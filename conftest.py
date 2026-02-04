import os

import pytest
from playwright.sync_api import Page, Playwright, BrowserContext
from dotenv import load_dotenv

from internal.browser import BrowserManager


@pytest.fixture(scope="session", autouse=True)
def envs():
    load_dotenv()



def pytest_addoption(parser) -> None:
    parser.addoption("--browser", action="store", default="chrome", help="Выбор браузера")
    parser.addoption("--device", action="store", default="ios", help="Выбор девайса")
    parser.addoption("--headless", action="store", default="False", help="Отображение браузера")

@pytest.fixture()
def browser_test(request):
    browser = os.environ.get("BROWSER") or request.config.getoption("--browser")
    return browser

@pytest.fixture
def page_init(playwright: Playwright, browser_test):
    params: dict = dict(playwright=playwright, browser_name=browser_test)
    browser: BrowserContext = BrowserManager.get_browser_context(**params)

    page: Page = browser.new_page()
    yield page
    page.close()
    browser.close()

@pytest.fixture()
def main_page(page_init):
    page_init.goto("https://demoqa.com/")