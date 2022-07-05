from selenium import webdriver


class WebDriver:
    class __WebDriver:
        def __init__(self):
            self.driver = webdriver.Firefox()

    driver = None

    def __init__(self):
        if not self.driver:
            WebDriver.driver = WebDriver.__WebDriver().driver

    def getDriver(self):
        driver = WebDriver().driver
        driver.get(self)
        return driver
