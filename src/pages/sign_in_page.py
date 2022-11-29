from src.config.config import config
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SignInPage:

    URL = config.GITHUB_MAIN_URL + "/login"

    username_field = (By.ID, "login_field")
    password_field = (By.ID, "password")
    login_button = (By.NAME, "commit")
    alert_incorrect_login = (By.CLASS_NAME, "js-flash-alert")

    def __init__(self, github_ui_app):
        self.github_ui_app = github_ui_app

    def open_login_panel(self):
        self.github_ui_app.open_page(self.URL)

    def login(self, username, password):
        WebDriverWait(self.github_ui_app.driver, 5).until(EC.presence_of_element_located(self.username_field))
        self.github_ui_app.fill_field_by_text(self.username_field, username)
        self.github_ui_app.click(self.login_button)
        self.github_ui_app.fill_field_by_text(self.password_field, password)
        self.github_ui_app.click(self.login_button)
