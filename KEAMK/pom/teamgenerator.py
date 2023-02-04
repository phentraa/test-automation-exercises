from KEAMK.general.basepage import BasePage

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.relative_locator import locate_with


class Participants:
    """
    Container class for all participant related web elements
    Used by TeamGeneratorPage class.
    """

    def __init__(self, driver):
        self.__driver = driver

    # SELECT elements --------------------------------------------------------------------------------------------------

    @property
    def select_count(self) -> Select:
        return Select(self.__driver.find_element(By.ID, 'nb-participants'))

    # INPUT elements ---------------------------------------------------------------------------------------------------

    def input_by(self, _id: int) -> WebElement:
        return self.__driver.find_element(By.XPATH, f'//input[contains(@placeholder, "Participant {_id}")]')

    @property
    def input_all(self) -> list[WebElement]:
        return self.__driver.find_elements(By.XPATH, '//input[contains(@placeholder, "Participant")]')

    # BUTTON elements --------------------------------------------------------------------------------------------------

    @property
    def button_add(self) -> WebElement:
        return self.__driver.find_element(By.ID, 'more-player')

# ----------------------------------------------------------------------------------------------------------------------


class Teams:
    """
    Container class for all teams related web elements.
    Used by TeamGeneratorPage class.
    """

    def __init__(self, driver):
        self.__driver = driver

    # SELECT elements --------------------------------------------------------------------------------------------------

    @property
    def select_count(self) -> Select:
        return Select(self.__driver.find_element(By.ID, 'nb-teams'))

    # INPUT elements ---------------------------------------------------------------------------------------------------

    def input_by(self, _id: int) -> WebElement:
        return self.__driver.find_element(By.XPATH, f'//input[contains(@placeholder, "Team {_id}")]')

    @property
    def input_all(self) -> list[WebElement]:
        return self.__driver.find_elements(By.XPATH, '//input[contains(@placeholder, "Team")]')

    # BUTTON elements --------------------------------------------------------------------------------------------------

    @property
    def button_add(self) -> WebElement:
        return self.__driver.find_element(By.ID, 'more-team')

# ----------------------------------------------------------------------------------------------------------------------


class TeamGeneratorPage(BasePage):
    """Handles the web elements of the whole page."""

    def __init__(self, driver):
        super().__init__(driver=driver, url=r'https://www.keamk.com/random-team-generator')
        self.__participants = Participants(driver=driver)
        self.__teams = Teams(driver=driver)

    @property
    def participants(self) -> Participants:
        return self.__participants

    @property
    def teams(self) -> Teams:
        return self.__teams

    # INPUT elements ---------------------------------------------------------------------------------------------------
    @property
    def input_title(self) -> WebElement:
        return self.driver.find_element(By.ID, 'mix_title')

    # BUTTON elements --------------------------------------------------------------------------------------------------
    @property
    def button_generate(self) -> WebElement:
        return self.driver.find_element(By.ID, 'mix_save')

    def button_delete_of(self, input_element: WebElement) -> WebElement:
        return self.driver.find_element(locate_with(
            By.TAG_NAME, 'span'
        ).to_right_of(input_element))

# ----------------------------------------------------------------------------------------------------------------------
