from .base_page import BasePage
from locators import LoginPageLocators


class LoginPage(BasePage):
    def login(self, username: str, password: str):
        self.page.locator(LoginPageLocators.USERNAME_INPUT).fill(username)
        self.page.locator(LoginPageLocators.PASSWORD_INPUT).fill(password)
        self.page.locator(LoginPageLocators.LOGIN_BUTTON).click()

    def get_error_message(self):
        return self.page.locator(LoginPageLocators.ERROR_MESSAGE).inner_text()