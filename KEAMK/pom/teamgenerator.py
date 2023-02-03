from KEAMK.general.configuration import get_preconfigured_chrome_driver
from KEAMK.general.basepage import BasePage


class TeamGeneratorPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver=driver, url='https://www.keamk.com/random-team-generator')


