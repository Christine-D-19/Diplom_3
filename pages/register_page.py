import allure
from pages.base_page import BasePage
from locators.register_page_locators import RegisterPageLocators


class RegisterPage(BasePage):
    @allure.step("Заполнить имя")
    def set_name(self, name: str):
        el = self.wait_visible(RegisterPageLocators.NAME_INPUT)
        el.clear()
        el.send_keys(name)

    @allure.step("Заполнить email")
    def set_email(self, email: str):
        el = self.wait_visible(RegisterPageLocators.EMAIL_INPUT)
        el.clear()
        el.send_keys(email)

    @allure.step("Заполнить пароль")
    def set_password(self, password: str):
        el = self.wait_visible(RegisterPageLocators.PASSWORD_INPUT)
        el.clear()
        el.send_keys(password)

    @allure.step("Нажать 'Зарегистрироваться'")
    def submit(self):
        self.click(RegisterPageLocators.REGISTER_BUTTON)
        