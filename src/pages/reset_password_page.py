from src.config.config import config
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ResetPasswordPage:

    URL = config.GITHUB_MAIN_URL + "/password_reset"

    email_field = (By.ID, "email_field")
    submit_button = (By.NAME, "commit")
    verify_captcha_button = (By.ID, "home_children_button")
    captcha_task = (By.CLASS_NAME, "Game__TextCenter-sc-t58kvs-0")
    refresh_captcha_button = (By.CLASS_NAME, "fc_meta_reload_btn")

    def __init__(self, github_ui_app):
        self.github_ui_app = github_ui_app

    def open_password_resetting_panel(self):
        self.github_ui_app.open_page(self.URL)

    def fill_email(self, email):
        self.github_ui_app.fill_field_by_text(*self.email_field, email)

    def run_captcha(self):
        WebDriverWait(self.github_ui_app.driver, 10).until(EC.visibility_of_element_located(self.verify_captcha_button))
        self.github_ui_app.click(*self.verify_captcha_button)   # Can not click... captcha security reason?

    def solve_captcha(self):
        # Some complicated script to hack captcha
        pass

    def get_captcha_task(self):
        WebDriverWait(self.github_ui_app.driver, 5).until(EC.visibility_of_element_located(self.captcha_task))
        return self.github_ui_app.get_element(*self.captcha_task).text

    def refresh_captcha(self):
        self.github_ui_app.click(*self.refresh_captcha_button)

    def confirm_password_resetting(self):
        self.github_ui_app.click(*self.submit_button)
