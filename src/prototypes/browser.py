from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class Browser:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def openBrowserWindow(self, url: str):
        """

        :type url: str
        """
        self.driver.get(url)

    def getElementByClassName(self, className: str) -> object:
        """

        :type className: str
        """
        return WebDriverWait(self.driver, timeout=3).until(lambda d: d.find_element(By.CLASS_NAME, className))

    def kill(self):
        self.driver.quit()

    def getScrollHeight(self):
        return self.driver.execute_script('return window.scrollY')

    def getContainerHeight(self):
        return self.driver.execute_script('return document.getElementById("streamItems").getBoundingClientRect()')

    def scrollDown(self):
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
