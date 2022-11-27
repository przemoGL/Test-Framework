from src.applications.base_ui import BaseUI
from src.config.config import config
from src.pages.login_page import LoginPage
from src.pages.reset_password_page import ResetPasswordPage


class GitHubUI(BaseUI):

    def __init__(self, driver):
        super().__init__(driver=driver)
        self.login_page = LoginPage(self)
        self.reset_password_page = ResetPasswordPage(self)

    def open_main_page(self):
        self.open_page(config.GITHUB_MAIN_URL)
