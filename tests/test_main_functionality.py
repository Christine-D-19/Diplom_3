import allure
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from data.urls import BASE_URL


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
        assert page.is_displayed(MainPageLocators.FEED_HEADER)

    @allure.title("Если кликнуть на ингредиент — появляется модалка с деталями")
    def test_ingredient_click_opens_details_modal(self, driver):
        page = MainPage(driver)
        page.open_main(BASE_URL)

        page.open_first_ingredient()
        assert page.is_displayed(MainPageLocators.INGREDIENT_MODAL)

    @allure.title("Модалка закрывается кликом по крестику")
    def test_ingredient_modal_closes_by_close_button(self, driver):
        page = MainPage(driver)
        page.open_main(BASE_URL)

        page.open_first_ingredient()
        page.close_ingredient_modal()
        assert not page.is_displayed(MainPageLocators.INGREDIENT_MODAL)

    @allure.title("При добавлении ингредиента счетчик увеличивается")
    def test_ingredient_counter_increases_after_add(self, driver):
        page = MainPage(driver)
        page.open_main(BASE_URL)

        before = page.get_first_ingredient_counter()
        page.drag_first_ingredient_to_constructor()
        after = page.get_first_ingredient_counter()

        assert after == before + 1
