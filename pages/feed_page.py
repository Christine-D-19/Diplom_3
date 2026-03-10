from data.urls import FEED_URL
from locators.feed_page_locators import FeedPageLocators
from pages.base_page import BasePage


class FeedPage(BasePage):
    def open_feed(self):
        self.open(FEED_URL)
        self.wait_visible(FeedPageLocators.FEED_HEADER)

    def is_order_in_progress(self, order_number: str) -> bool:
        self.wait_visible(FeedPageLocators.IN_PROGRESS_SECTION)
        self.wait_text_in_element(FeedPageLocators.IN_PROGRESS_SECTION, order_number)
        return order_number in self.get_text(FeedPageLocators.IN_PROGRESS_SECTION)

    def get_total_done(self) -> int:
        return int(self.get_text(FeedPageLocators.TOTAL_DONE))

    def get_today_done(self) -> int:
        return int(self.get_text(FeedPageLocators.TODAY_DONE))
    