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

    def close(self, only_close=False):
        """
        Calls the driver's quit() method.
        :param only_close: When True then calls the close() method
        :return: None
        """
        if only_close:
            self.driver.close()
        self.driver.quit()
