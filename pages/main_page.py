from selenium.common.exceptions import NoSuchElementException

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    def open_main(self, base_url: str):
        self.open(base_url)

    def go_to_constructor(self):
        self.click(MainPageLocators.CONSTRUCTOR_LINK)
        self.wait_visible(MainPageLocators.CONSTRUCTOR_HEADER)

    def go_to_feed(self):
        self.click(MainPageLocators.FEED_LINK)
        self.wait_url_contains("/feed")

    def open_first_ingredient(self):
        self.scroll_into_view(MainPageLocators.FIRST_INGREDIENT)
        self.click(MainPageLocators.FIRST_INGREDIENT)
        self.wait_visible(MainPageLocators.INGREDIENT_MODAL)

    def close_ingredient_modal(self):
        self.click(MainPageLocators.MODAL_CLOSE_BUTTON)
        self.wait_invisible(MainPageLocators.INGREDIENT_MODAL)

    def get_first_ingredient_counter(self) -> int:
        card = self.wait_visible(MainPageLocators.FIRST_INGREDIENT)
        try:
            counter = card.find_element(*MainPageLocators.INGREDIENT_COUNTER_IN_CARD)
            text = counter.text.strip()
            return int(text) if text else 0
        except NoSuchElementException:
            return 0

    def drag_first_ingredient_to_constructor(self):
        try:
            self.drag_and_drop(
                MainPageLocators.FIRST_NOT_BUN,
                MainPageLocators.CONSTRUCTOR_DROPZONE,
            )
        except NoSuchElementException:
            self.drag_and_drop(
                MainPageLocators.FIRST_NOT_BUN_FALLBACK,
                MainPageLocators.CONSTRUCTOR_DROPZONE,
            )

    def add_bun_to_constructor_twice(self):
        self.drag_and_drop(
            MainPageLocators.FIRST_BUN,
            MainPageLocators.CONSTRUCTOR_DROPZONE,
        )
        self.drag_and_drop(
            MainPageLocators.FIRST_BUN,
            MainPageLocators.CONSTRUCTOR_DROPZONE,
        )

    def click_login_button(self):
        self.click(MainPageLocators.LOGIN_BUTTON)

    def click_place_order(self):
        self.click(MainPageLocators.PLACE_ORDER_BUTTON)

    def get_order_number(self) -> str:
        text = self.get_text(MainPageLocators.ORDER_NUMBER)
        return "".join(symbol for symbol in text if symbol.isdigit())

    def wait_order_modal(self):
        self.wait_visible(MainPageLocators.ORDER_MODAL)

    def wait_counter_change(self, value: int):
        self.wait.until(
            lambda driver: self.get_first_ingredient_counter() == value
        )
        