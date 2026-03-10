import allure

from data.urls import BASE_URL
from pages.feed_page import FeedPage
from pages.login_page import LoginPage
from pages.main_page import MainPage


@allure.suite("Лента заказов")
class TestFeedFlow:
    @allure.title("После создания заказа номер появляется в блоке «В работе»")
    def test_order_number_appears_in_progress(self, driver, registered_user):
        user = registered_user["user"]
        assert registered_user["response"].status_code == 200

        main = MainPage(driver)
        main.open_main(BASE_URL)

        main.add_bun_to_constructor_twice()
        main.drag_first_ingredient_to_constructor()
        main.click_login_button()

        login = LoginPage(driver)
        login.login(user.email, user.password)

        main.click_place_order()
        main.wait_order_modal()
        order_number = main.get_order_number()

        feed = FeedPage(driver)
        feed.open_feed()

        assert feed.is_order_in_progress(order_number)

    @allure.title("После создания заказа увеличивается счетчик «Выполнено за всё время»")
    def test_total_counter_increases_after_order(self, driver, registered_user):
        user = registered_user["user"]
        assert registered_user["response"].status_code == 200

        feed = FeedPage(driver)
        feed.open_feed()
        total_before = feed.get_total_done()

        main = MainPage(driver)
        main.open_main(BASE_URL)

        main.add_bun_to_constructor_twice()
        main.drag_first_ingredient_to_constructor()
        main.click_login_button()

        login = LoginPage(driver)
        login.login(user.email, user.password)

        main.click_place_order()
        main.wait_order_modal()

        feed.open_feed()
        total_after = feed.get_total_done()

        assert total_after >= total_before

    @allure.title("После создания заказа увеличивается счетчик «Выполнено за сегодня»")
    def test_today_counter_increases_after_order(self, driver, registered_user):
        user = registered_user["user"]
        assert registered_user["response"].status_code == 200

        feed = FeedPage(driver)
        feed.open_feed()
        today_before = feed.get_today_done()

        main = MainPage(driver)
        main.open_main(BASE_URL)

        main.add_bun_to_constructor_twice()
        main.drag_first_ingredient_to_constructor()
        main.click_login_button()

        login = LoginPage(driver)
        login.login(user.email, user.password)

        main.click_place_order()
        main.wait_order_modal()

        feed.open_feed()
        today_after = feed.get_today_done()

        assert today_after >= today_before
        