from selenium.webdriver.common.by import By
from src.applications.base_ui import BaseUI
from src.config.config import configuration


class GitHubUI(BaseUI):
    def __init__(self, driver):
        super().__init__(driver=driver)

    def open_main_page(self):
        self.open_page(configuration.GITHUB_MAIN_URL)

    def open_login_panel(self):
        self.open_page(configuration.GITHUB_MAIN_URL + '/session')

    def login(self, username, password):
        self.fill_field_by_text(By.ID, 'login_field', username)
        self.click(By.NAME, 'commit')
        self.fill_field_by_text(By.ID, 'password', password)
        self.click(By.NAME, 'commit')
