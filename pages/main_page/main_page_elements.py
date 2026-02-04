from playwright.sync_api import Page


class MainPageElements():
    def __init__(self, page: Page):
        self.page = page

    @property
    def elements_card(self):
        return self.page.locator('//h5[contains(text(), "Elements")]')

