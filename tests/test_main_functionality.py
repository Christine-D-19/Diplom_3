import allure

from data.urls import BASE_URL
from locators.main_page_locators import MainPageLocators
from pages.feed_page import FeedPage
from pages.main_page import MainPage


@allure.suite("Основная функциональность")
class TestMainFunctionality:
    @allure.title("Переход по клику на «Конструктор»")
    def test_click_constructor_opens_constructor(self, driver):
        page = MainPage(driver)
        page.open_main(BASE_URL)

        page.go_to_constructor()

        assert page.is_displayed(MainPageLocators.CONSTRUCTOR_HEADER)

    @allure.title("Переход по клику на «Лента заказов»")
    def test_click_feed_opens_feed(self, driver):
        page = MainPage(driver)
        page.open_main(BASE_URL)

        page.go_to_feed()
        feed_page = FeedPage(driver)

        assert feed_page.is_displayed(feed_page.__class__.__mro__[0] and feed_page.__class__ and __import__("locators.feed_page_locators").feed_page_locators.FeedPageLocators.FEED_HEADER)
        