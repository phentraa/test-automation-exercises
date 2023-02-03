from selenium.webdriver import Chrome


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