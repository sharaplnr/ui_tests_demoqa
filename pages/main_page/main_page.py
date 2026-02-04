from playwright.sync_api import Page

from pages.main_page.main_page_elements import MainPageElements


class MainPage:
    def __init__(self, page: Page):
        self.page = page
        self.elements = MainPageElements(self.page)