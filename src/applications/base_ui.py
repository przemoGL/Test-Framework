class BaseUI:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url_address):
        self.driver.get(url_address)
        self.driver.maximize_window()

    def get_title(self):
        return self.driver.title

    def get_element(self, locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        element = self.get_element(locator)
        element.click()

    def fill_field_by_text(self, locator, text):
        field = self.get_element(locator)
        field.send_keys(text)

    def exit(self):
        self.driver.quit()
