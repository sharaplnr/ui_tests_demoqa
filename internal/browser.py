from playwright.sync_api import Playwright, BrowserContext, Browser, BrowserType

class BrowserManager:
    @staticmethod
    def _get_device(playwright: Playwright, device_type: str) -> dict | None:
        match device_type:
            case "ios":
                return playwright.devices["iPhone 14 Pro Max"]
            case "android":
                return playwright.devices["Galaxy S8"]
            case _:
                return None

    def _get_browser_type(playwright: Playwright, browser_name: str) -> BrowserType:
        match browser_name:
            case "firefox":
                return playwright.firefox
            case "webkit":
                return playwright.webkit
            case _:
                return playwright.chromium

    @staticmethod
    def get_browser_context(playwright: Playwright, browser_name: str, device_type: str, headless: bool = False) -> BrowserContext:
        browser: Browser = BrowserManager._get_browser_type(playwright, browser_name).launch(headless=headless)
        device: dict = BrowserManager._get_device(playwright, device_type)

        params: dict = dict(
            ignore_https_errors=True,
            viewport={"width": 1510, "height": 960},
        )

        if device:
            params.update(**device)

        context: BrowserContext = browser.new_context(**params)

        return context