from KEAMK.general.basepage import BasePage

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.relative_locator import locate_with


class TeamGeneratorPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver=driver, url=r'https://www.keamk.com/random-team-generator')

    # SELECT elements --------------------------------------------------------------------------------------------------
    @property
    def select_participants(self) -> Select:
        return Select(self.driver.find_element(By.ID, 'nb-participants'))

    @property
    def select_teams(self) -> Select:
        return Select(self.driver.find_element(By.ID, 'nb-teams'))

    # INPUT elements ---------------------------------------------------------------------------------------------------
    @property
    def input_title(self) -> WebElement:
        return self.driver.find_element(By.ID, 'mix_title')

    def input_participant_by(self, id: int):
        return self.driver.find_element(By.XPATH, f'//input[contains(@placeholder, "Participant {id}")]')

    @property
    def input_all_participants(self) -> list[WebElement]:
        return self.driver.find_elements(By.XPATH, '//input[contains(@placeholder, "Participant")]')

    def input_team_by(self, id: int):
        return self.driver.find_element(By.XPATH, f'//input[contains(@placeholder, "Team {id}")]')

    @property
    def input_all_teams(self) -> list[WebElement]:
        return self.driver.find_elements(By.XPATH, '//input[contains(@placeholder, "Team")]')

    # BUTTON elements --------------------------------------------------------------------------------------------------
    @property
    def button_generate(self) -> WebElement:
        return self.driver.find_element(By.ID, 'mix_save')

    @property
    def button_add_participant(self) -> WebElement:
        return self.driver.find_element(By.ID, 'more-player')

    @property
    def button_add_team(self) -> WebElement:
        return self.driver.find_element(By.ID, 'more-team')

    def button_delete_of(self, input_element: WebElement) -> WebElement:
        return self.driver.find_element(locate_with(
            By.TAG_NAME, 'span'
        ).to_right_of(input_element))



