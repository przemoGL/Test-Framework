from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from src.providers.browsers.base_browser import BaseBrowser
from webdriver_manager.firefox import GeckoDriverManager


class FirefoxBrowser(BaseBrowser):
    OPTIONS = None

    @classmethod
    def get_driver(cls):
        return webdriver.Chrome(service=Service(GeckoDriverManager().install()),
                                options=cls.OPTIONS)
