from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):
    def login(self, email: str, password: str):
        email_input = self.wait_visible(LoginPageLocators.EMAIL_INPUT)
        email_input.clear()
        email_input.send_keys(email)

        password_input = self.wait_visible(LoginPageLocators.PASSWORD_INPUT)
        password_input.clear()
        password_input.send_keys(password)

        self.click(LoginPageLocators.SUBMIT_BUTTON)
        self.wait_for_page_ready()
        