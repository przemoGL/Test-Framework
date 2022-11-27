from src.config.config import config
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ResetPasswordPage:

    RESET_PASSWORD_URL = config.GITHUB_MAIN_URL + "/password_reset"

    email_field = (By.ID, "email_field")
    submit_button = (By.NAME, "commit")
    start_captcha_button = (By.ID, "home_children_button")
    captcha_task = (By.CLASS_NAME, "Game__TextCenter-sc-t58kvs-0 gxZImH")
    refresh_captcha_button = (By.CLASS_NAME, "fc_meta_reload_btn")

    def __init__(self, github_ui_app):
        self.github_ui_app = github_ui_app

    def open_forgot_password_panel(self):
        self.github_ui_app.open_page(self.RESET_PASSWORD_URL)

    def fill_email(self, email):
        self.github_ui_app.fill_field_by_text(*self.email_field, email)

    def solve_captcha(self):
        WebDriverWait(self.github_ui_app.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, self.start_captcha_button)))
        self.github_ui_app.click(*self.start_captcha_button)   # Can not click... captcha security reason?
        WebDriverWait(self.github_ui_app.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, self.captcha_task)))
        # Some complicated script to hack captcha

    def get_captcha_task(self):
        return self.github_ui_app.get_element(*self.captcha_task).text

    def refresh_captcha(self):
        self.github_ui_app.click(*self.refresh_captcha_button)

    def confirm_password_resetting(self):
        self.github_ui_app.click(*self.submit_button)
