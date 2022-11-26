class BaseUI:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url_address):
        self.driver.get(url_address)
        self.driver.maximize_window()

    def get_title(self):
        return self.driver.title

    def get_element(self, locator_type, locator_value):
        return self.driver.find_element(locator_type, locator_value)

    def click(self, locator_type, locator_value):
        element = self.get_element(locator_type, locator_value)
        element.click()

    def fill_field_by_text(self, locator_type, locator_value, text):
        field = self.get_element(locator_type, locator_value)
        field.send_keys(text)

    def exit(self):
        self.driver.quit()
