from src.config.config import config
from selenium import webdriver
from src.providers.browsers.base_browser import BaseBrowser


class RemoteChromeBrowser(BaseBrowser):
    OPTIONS = None

    @classmethod
    def get_driver(cls):
        return webdriver.Remote(command_executor=config.SELENIUM_GRID_URL,
                                desired_capabilities={"browserName": "chrome"})
