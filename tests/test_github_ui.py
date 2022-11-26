import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestsGitHubUI:
    def test_main_page_title(self, github_ui):
        github_ui.open_main_page()
        assert github_ui.get_title() == "GitHub: Let’s build from here · GitHub"

    @pytest.mark.xfail(reason="Incorrect input login credentials")
    def test_loging_in(self, github_ui):
        github_ui.open_login_panel()
        WebDriverWait(github_ui.driver, 5).until(EC.presence_of_element_located((By.ID, "login_field")))
        github_ui.login("incorrect_user", "incorrect_pass")
        assert not github_ui.driver.find_element(By.CLASS_NAME, "js-flash-alert")
