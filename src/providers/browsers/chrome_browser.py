from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from src.providers.browsers.base_browser import BaseBrowser
from webdriver_manager.chrome import ChromeDriverManager


class ChromeBrowser(BaseBrowser):
    OPTIONS = None

    @classmethod
    def get_driver(cls):
        return webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                                options=cls.OPTIONS)
