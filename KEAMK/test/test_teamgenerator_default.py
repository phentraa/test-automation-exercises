import pytest

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

    @pytest.mark.parametrize('field_group', ['participant', 'team'])
    def test_inputs_are_present(self, field_group: str, input_expected_data):
        if field_group == 'participant':
            input_fields = self.page.input_all_participants
        else:
            input_fields = self.page.input_all_teams

        assert len(input_fields) == input_expected_data[field_group]['number_of_fields']

    @pytest.mark.parametrize('field_group', ['participant', 'team'])
    def test_p_and_t_inputs_has_delete_button(self, field_group):
        if field_group == 'participant':
            input_fields = self.page.input_all_participants
        else:
            input_fields = self.page.input_all_teams

        for input_field in input_fields:
            assert self.page.button_delete_of(input_field).is_displayed()

    def test_title_input_is_present(self):
        assert self.page.input_title.is_displayed()

    def test_button_generator_is_present(self):
        assert self.page.button_generate.is_displayed()

    def test_button_add_participant_is_present(self):
        assert self.page.button_add_participant.is_displayed()

    def test_button_add_team_is_present(self):
        assert self.page.button_add_team.is_displayed()

    def test_select_participant_is_present(self):
        assert self.page.select_participants is not None

    def test_select_teams_is_present(self):
        assert self.page.select_teams is not None

