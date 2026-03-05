import time
from selenium.common.exceptions import StaleElementReferenceException

from pages.base_page import BasePage
from locators.feed_page_locators import FeedPageLocators


class FeedPage(BasePage):
    def open_feed(self, base_url: str = "https://stellarburgers.education-services.ru/"):
        if base_url.endswith("/"):
            self.open(base_url + "feed")
        else:
            self.open(base_url + "/feed")

        self.wait_visible(FeedPageLocators.FEED_HEADER)

    def _safe_get_texts(self, locator, retries: int = 5, pause: float = 0.2):
        last_exc = None
        for _ in range(retries):
            try:
                elements = self.find_elements(locator)
                return [el.text.strip() for el in elements if el.text and el.text.strip()]
            except StaleElementReferenceException as e:
                last_exc = e
                time.sleep(pause)
        if last_exc:
            raise last_exc
        return []

    def is_order_in_progress(self, order_number: str) -> bool:
        self.wait_visible(FeedPageLocators.IN_PROGRESS_SECTION)

        end = time.time() + 15
        while time.time() < end:
            texts = self._safe_get_texts(FeedPageLocators.IN_PROGRESS_NUMBERS, retries=5, pause=0.2)
            if order_number in texts:
                return True
            time.sleep(0.5)

        return False

    def are_counters_increased(self) -> bool:
        total = int(self.wait_visible(FeedPageLocators.TOTAL_DONE).text.strip())
        today = int(self.wait_visible(FeedPageLocators.TODAY_DONE).text.strip())
        return total >= 1 and today >= 1
    