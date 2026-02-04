import os

import pytest
from playwright.sync_api import Page, Playwright, BrowserContext
from dotenv import load_dotenv

from internal.browser import BrowserManager


@pytest.fixture(scope="session", autouse=True)
def envs():
    load_dotenv()

def pytest_addoption(parser) -> None:
    parser.addoption("--browser_name", action="store", default="chrome", help="Выбор браузера")
    parser.addoption("--device_type", action="store", default="ios", help="Выбор девайса")
    parser.addoption("--headless", action="store", default="False", help="Отображение браузера")

@pytest.fixture()
def browser_test(request):
    browser = os.environ.get("BROWSER") or request.config.getoption("--browser_name")
    return browser

@pytest.fixture()
def page(playwright: Playwright, platform_test, browser_test):
    params: dict = dict(playwright=playwright, browser_name=browser_test, device_type=platform_test)
    context: BrowserContext = BrowserManager.get_browser_context(**params)

    page: Page = context.new_page()
    yield page
    page.close()
    context.browser.close()

@pytest.fixture()
def platform_test(request):
    if "/mobile/" in request.node.nodeid:
        device_from_user = os.environ.get("DEVICE") or request.config.getoption("device_test")
        device = device_from_user if device_from_user in ["ios", "android"] else "ios"
    else:
        device = "desktop"
    os.environ["platform_type"] = device
    yield device
