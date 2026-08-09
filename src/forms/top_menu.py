from playwright.sync_api import Page, TimeoutError


class TopMenu:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.__products_button = page.locator("a[href='/products']")
        self.__cookie_accept_button = page.locator(".fc-cta-consent")

    def click_products_button(self) -> None:
        self.accept_cookies()
        self.__products_button.click()

    def accept_cookies(self) -> None:
        try:
            self.__cookie_accept_button.wait_for(state="visible", timeout=6000)
            self.__cookie_accept_button.click()
        except TimeoutError:
            pass
