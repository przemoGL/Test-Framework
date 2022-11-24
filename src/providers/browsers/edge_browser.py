from selenium import webdriver
from selenium.webdriver.edge.service import Service
from src.providers.browsers.base_browser import BaseBrowser
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class EdgeBrowser(BaseBrowser):
    OPTIONS = None

    @classmethod
    def get_driver(cls):
        return webdriver.Chrome(service=Service(EdgeChromiumDriverManager().install()),
                                options=cls.OPTIONS)
