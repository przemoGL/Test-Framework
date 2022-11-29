import pytest
from src.models.data_time import DataTime
from src.models.user import User
from src.applications.github_api import GitHubApi
from src.applications.github_ui import GitHubUI
from src.providers.browsers.browser_provider import BrowserProvider


# Date-time
@pytest.fixture(scope="session")
def time():
    yield
    data_time = DataTime()
    print(f'\n\nDate: {data_time.get_date()} \t Time: {data_time.get_time()}')


# User
@pytest.fixture(scope="function")
def user(name, surname):
    user = User(name, surname)
    yield user
    del user


# GitHub API (with user logger)
@pytest.fixture()
def github_api(username):
    github_api = GitHubApi()
    github_api.login(username)
    yield github_api
    github_api.logout(username)


# GitHub UI
@pytest.fixture(scope="class")
def github_ui(request):
    browser = request.config.getoption("--browser")
    driver = BrowserProvider.get_driver(browser=browser)
    github_ui = GitHubUI(driver)
    yield github_ui
    github_ui.exit()


# Browser selector
def pytest_addoption(parser):
    parser.addoption("--browser",
                     action="store",
                     choices=["chrome", "edge", "firefox"],
                     default="chrome",
                     help="Choose a browser")
