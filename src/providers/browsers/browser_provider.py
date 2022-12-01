from src.providers.browsers.chrome_browser import ChromeBrowser
from src.providers.browsers.firefox_browser import FirefoxBrowser
from src.providers.browsers.edge_browser import EdgeBrowser
from src.providers.browsers.remote_chrome_browser import RemoteChromeBrowser


class BrowserProvider:
    MAPPER = {
        "chrome": ChromeBrowser,
        "firefox": FirefoxBrowser,
        "edge": EdgeBrowser,
        "remote_chrome": RemoteChromeBrowser
    }

    @classmethod
    def get_driver(cls, browser):
        browser_class = cls.MAPPER.get(browser)
        if browser_class is None:
            print("Browser not registered")
        return browser_class.get_driver()
