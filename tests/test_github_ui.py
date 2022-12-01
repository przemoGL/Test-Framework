import pytest


class TestsGitHubUI:

    def test_main_page_title(self, github_ui):
        github_ui.open_main_page()
        assert github_ui.get_title() == github_ui.MAIN_PAGE_TITLE

    def test_incorrect_loging_in(self, github_ui):
        github_ui.sign_in_page.open_login_panel()
        github_ui.sign_in_page.login("incorrect_user", "incorrect_pass")
        assert github_ui.get_element(github_ui.sign_in_page.alert_incorrect_login)

    @pytest.mark.skip(reason="Captcha blocking")
    def test_refresh_captcha(self, github_ui):
        github_ui.reset_password_page.open_password_resetting_panel()
        github_ui.reset_password_page.run_captcha()
        task_before_refreshing = github_ui.reset_password_page.get_captcha_task()
        github_ui.reset_password_page.refresh_captcha()
        task_after_refreshing = github_ui.reset_password_page.get_captcha_task()
        assert task_before_refreshing != task_after_refreshing

    def test_password_requirement(self, github_ui):
        github_ui.sign_up_page.open_sing_up_panel()
        github_ui.sign_up_page.fill_email('test_email@email.com')
        continue_button = github_ui.get_element(github_ui.sign_up_page.continue_button)
        assert continue_button.is_displayed()
        assert not continue_button.is_enabled()
