import allure

from pages.main_page import MainPage
from pages.feed_page import FeedPage
from helpers.api_user import create_user_via_api
from data.urls import BASE_URL


@allure.suite("Лента заказов")
class TestFeedFlow:
    @allure.title("После создания заказа увеличиваются счетчики и номер появляется в 'В работе'")
    def test_order_appears_in_feed_and_counters_increase(self, driver):
        user = create_user_via_api()

        main = MainPage(driver)
        main.open_main(BASE_URL)

        main.add_bun_to_constructor_twice()
        main.drag_first_ingredient_to_constructor()

        order_number = main.place_order_with_login_if_needed(user)

        feed = FeedPage(driver)
        feed.open_feed(BASE_URL)

        assert feed.is_order_in_progress(order_number)
        assert feed.are_counters_increased()
