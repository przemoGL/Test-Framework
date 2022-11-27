import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestsGitHubUI:

    def test_main_page_title(self, github_ui):
        github_ui.open_main_page()
        assert github_ui.get_title() == "GitHub: Let’s build from here · GitHub"

    def test_incorrect_loging_in(self, github_ui):
        github_ui.login_page.open_login_panel()
        WebDriverWait(github_ui.driver, 5).until(EC.presence_of_element_located((By.ID, "login_field")))
        github_ui.login_page.login("incorrect_user", "incorrect_pass")
        assert github_ui.get_element(By.CLASS_NAME, "js-flash-alert")

    @pytest.mark.skip(reason="Captcha blocking")
    def test_refresh_captcha(self, github_ui):
        github_ui.reset_password_page.open_forgot_password_panel()
        github_ui.reset_password_page.solve_captcha()
        task_before_refreshing = github_ui.reset_password_page.get_captcha_task()
        github_ui.reset_password_page.refresh_captcha()
        task_after_refreshing = github_ui.reset_password_page.get_captcha_task()
        assert task_before_refreshing != task_after_refreshing
