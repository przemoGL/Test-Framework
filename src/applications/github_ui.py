from src.applications.base_ui import BaseUI
from src.config.config import config
from src.pages.sign_in_page import SignInPage
from src.pages.reset_password_page import ResetPasswordPage
from src.pages.sign_up_page import SignUpPage


class GitHubUI(BaseUI):

    def __init__(self, driver):
        super().__init__(driver=driver)
        self.login_page = SignInPage(self)
        self.reset_password_page = ResetPasswordPage(self)
        self.sing_up_page = SignUpPage(self)

    def open_main_page(self):
        self.open_page(config.GITHUB_MAIN_URL)
