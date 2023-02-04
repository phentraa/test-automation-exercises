from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import time


class BasePage:
    """
    General page. Excepts Chrome driver.
    """

    def __init__(self, driver: Chrome, url: str):
        self.__driver = driver
        self.__url = url

    @property
    def driver(self):
        return self.__driver

    def open(self):
        self.driver.get(self.__url)

    def close(self, only_close=False):
        """
        Calls the driver's quit() method.
        :param only_close: When True then calls the close() method
        :return: None
        """
        if only_close:
            self.driver.close()
        self.driver.quit()

    @property
    def html(self) -> WebElement:
        return self.driver.find_element(By.TAG_NAME, 'html')

    def scroll_down(self):
        self.html.send_keys(Keys.END)
        time.sleep(1)  # Simulated scrolling is slower than code execution. We need to stop a little bit.
