import pytest, allure

from KEAMK.pom.teamgenerator import TeamGeneratorPage
from KEAMK.general.configuration import get_preconfigured_chrome_driver


class TestTeamGeneratorDefault:
    """
    Contains test cases for check the presence of necessary elements.
    """

    # SETTINGS OF ENVIRONMENT ------------------------------------------------------------------------------------------

    def setup_method(self):
        self.page = TeamGeneratorPage(driver=get_preconfigured_chrome_driver())
        self.page.open()
        self.page.driver.maximize_window()

    def teardown_method(self):
        self.page.close()

    @pytest.fixture
    def input_expected_data(self):
        return {
            'participant': {'number_of_fields': 10},
            'team': {'number_of_fields': 5}
        }

    # BEGINNING OF TEST METHODS ----------------------------------------------------------------------------------------

    @allure.id('T101')
    @allure.title('All section inputs are present')
    @allure.description("""
            Check the page for all section inputs are present.
            
            Expected results:
            - 10 Participant input fields are present on the page by default
            - 5 Team input fields are present on the page by default
            """)
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.parametrize('field_group', ['participant', 'team'])
    def test_inputs_are_present(self, field_group: str, input_expected_data):
        if field_group == 'participant':
            input_fields = self.page.participants.input_all
        else:
            input_fields = self.page.teams.input_all

        assert len(input_fields) == input_expected_data[field_group]['number_of_fields']

    # ------------------------------------------------------------------------------------------------------------------

    @allure.id('T102')
    @allure.title('Section input fields has delete button')
    @allure.description("""
            Check that all input fields on the Participants and Teams section has a delete button.
            
            Expected results:
            The delete buttons are displayed on the left side of the input fields.
            """)
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.parametrize('field_group', ['participant', 'team'])
    def test_p_and_t_inputs_has_delete_button(self, field_group):
        if field_group == 'participant':
            input_fields = self.page.participants.input_all
        else:
            input_fields = self.page.teams.input_all

        for input_field in input_fields:
            assert self.page.button_delete_for(input_field).is_displayed()

    # ------------------------------------------------------------------------------------------------------------------

    @allure.id('T103')
    @allure.title('Title input is present')
    @allure.description("""
            Check the presence of Title input field.
            Expected result: The Title input field is displayed on the page
            """)
    @allure.severity(allure.severity_level.MINOR)
    def test_title_input_is_present(self):
        assert self.page.input_title.is_displayed()

    # ------------------------------------------------------------------------------------------------------------------

    @allure.id('T104')
    @allure.title('Generate team button is present')
    @allure.description("""
                Check the presence of Generate Team button.
                Expected result: The Generate Team button is displayed on the page
                """)
    @allure.severity(allure.severity_level.MINOR)
    def test_button_generator_is_present(self):
        assert self.page.button_generate.is_displayed()

    # ------------------------------------------------------------------------------------------------------------------

    @allure.id('T105')
    @allure.title('Add Participant button is present')
    @allure.description("""
                    Check the presence of the Add Participant button.
                    Expected result: The Add Participant button is displayed on the page
                    """)
    @allure.severity(allure.severity_level.MINOR)
    def test_button_add_participant_is_present(self):
        assert self.page.participants.button_add.is_displayed()

    # ------------------------------------------------------------------------------------------------------------------

    @allure.id('T106')
    @allure.title('Add Team button is present')
    @allure.description("""
                        Check the presence of the Add Team button.
                        Expected result: The Add Team button is displayed on the page
                        """)
    @allure.severity(allure.severity_level.MINOR)
    def test_button_add_team_is_present(self):
        assert self.page.teams.button_add.is_displayed()

    # ------------------------------------------------------------------------------------------------------------------

    @allure.id('T107')
    @allure.title('Participant number selector is present')
    @allure.description("""
                        Check the presence of the Participant number selector.
                        Expected result: The Participant number selector is available on the page
                        """)
    @allure.severity(allure.severity_level.MINOR)
    def test_select_participant_is_present(self):
        assert self.page.participants.select_number is not None

    # ------------------------------------------------------------------------------------------------------------------

    @allure.id('T108')
    @allure.title('Team number selector is present')
    @allure.description("""
                           Check the presence of the Team number selector.
                           Expected result: The Team number selector is available on the page
                           """)
    @allure.severity(allure.severity_level.MINOR)
    def test_select_teams_is_present(self):
        assert self.page.teams.select_number is not None

