from src.config.config import config
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SignUpPage:

    URL = config.GITHUB_MAIN_URL + "/signup"

    email_field = (By.ID, "email")
    continue_button = (By.CLASS_NAME, "js-continue-button")

    def __init__(self, github_ui_app):
        self.github_ui_app = github_ui_app

    def open_sing_up_panel(self):
        self.github_ui_app.open_page(self.URL)

    def fill_email(self, email):
        WebDriverWait(self.github_ui_app.driver, 10).until(EC.visibility_of_element_located(self.email_field))
        self.github_ui_app.fill_field_by_text(*self.email_field, email)
        self.github_ui_app.click(*self.continue_button)
