import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    def open_main(self, base_url: str):
        self.open(base_url)

    def go_to_feed(self):
        self.scroll_into_view(MainPageLocators.FEED_LINK)
        self.js_click(MainPageLocators.FEED_LINK)

        self.wait_visible(MainPageLocators.FEED_HEADER)

    def go_to_constructor(self):
        try:
            self.click(MainPageLocators.CONSTRUCTOR_LINK_HREF)
        except Exception:
            self.click(MainPageLocators.CONSTRUCTOR_LINK)
        self.wait_for_page_ready()

    def _get_constructor_dropzone(self):
        return self.find_first_present(MainPageLocators.CONSTRUCTOR_DROPZONE_VARIANTS)

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
            txt = counter.text.strip()
            return int(txt) if txt else 0
        except Exception:
            return 0

    def _drag_element_to_constructor(self, ingredient_locator):
        src = self.wait_visible(ingredient_locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", src)

        target = self._get_constructor_dropzone()
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", target)

        browser = (self.driver.capabilities.get("browserName") or "").lower()
        if "firefox" in browser:
            self.html5_drag_and_drop(src, target)
            time.sleep(0.3)
            return

        try:
            ActionChains(self.driver).drag_and_drop(src, target).perform()
        except Exception:
            self.html5_drag_and_drop(src, target)

        time.sleep(0.2)

    def drag_first_ingredient_to_constructor(self):
        try:
            self._drag_element_to_constructor(MainPageLocators.FIRST_NOT_BUN)
        except Exception:
            self._drag_element_to_constructor(MainPageLocators.FIRST_NOT_BUN_FALLBACK)

    def add_bun_to_constructor_twice(self):
        self._drag_element_to_constructor(MainPageLocators.FIRST_BUN)
        self._drag_element_to_constructor(MainPageLocators.FIRST_BUN)

    def place_order_with_login_if_needed(self, user) -> str:
        if self.is_displayed(MainPageLocators.LOGIN_BUTTON):
            self.click(MainPageLocators.LOGIN_BUTTON)

            from pages.login_page import LoginPage
            login = LoginPage(self.driver)

            login.login(user.email, user.password)
            self.wait_for_page_ready()

        self.click(MainPageLocators.PLACE_ORDER_BUTTON)

        self.wait_visible(MainPageLocators.ORDER_MODAL)
        number_el = self.wait_visible(MainPageLocators.ORDER_NUMBER)

        order_number = number_el.text.strip()
        if not order_number or not any(ch.isdigit() for ch in order_number):
            time.sleep(1)
            order_number = self.wait_visible(MainPageLocators.ORDER_NUMBER).text.strip()

        digits = "".join([c for c in order_number if c.isdigit()])
        return digits
    