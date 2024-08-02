from playwright.sync_api import Page


class LoginPageLocators:
    USERNAME_INPUT = '#username'
    PASSWORD_INPUT = '#password'
    LOGIN_BUTTON = '#login'
    ERROR_MESSAGE = '#errorAlert'
