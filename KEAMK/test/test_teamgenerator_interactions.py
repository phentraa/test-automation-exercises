import pytest
from KEAMK.pom.teamgenerator import TeamGeneratorPage
from KEAMK.general.configuration import get_preconfigured_chrome_driver


class TestTeamGeneratorInteractions:
    """
    Contains test cases for simulate user interactions on the page.
    """

    # SETTINGS OF ENVIRONMENT ------------------------------------------------------------------------------------------

    def setup_method(self):
        self.page = TeamGeneratorPage(driver=get_preconfigured_chrome_driver())
        self.page.open()
        self.page.driver.maximize_window()

    def teardown_method(self):
        self.page.close()
        # pass

    @pytest.fixture
    def error_messages(self):
        return {
            'empty_title': 'The Title field should not be blank.',
            'empty_field': 'You must fill out at least the first Participant and the first Team.'
        }

    def get_section(self, field_group: str):
        """
        Get the Participants or Teams section of the page based on the field_group value.
        :param field_group: participant or team
        :return: Participants / Teams instance
        :raises ValueError
        """
        if field_group.lower() not in ['participant', 'team']:
            raise ValueError('The field_group parameter have to be "participant" or "team".')

        if field_group == 'participant':
            return self.page.participants
        else:
            return self.page.teams

    # BEGINNING OF TEST METHODS ----------------------------------------------------------------------------------------

    def test_submit_with_empty_title(self, error_messages):
        self.page.scroll_down()
        self.page.button_generate.click()

        assert self.page.error_field.text == error_messages['empty_title']

    @pytest.mark.parametrize('field_group', ['participant', 'team'])
    def test_submit_with_empty_section_inputs(self, field_group, error_messages):

        self.page.input_title.send_keys('Test Title')
        section = self.get_section(field_group)
        # The first input in this section will get a value.
        # I actually check that error message appears when the other section remains blank.
        section.input_nth(1).send_keys('Test Input 1')

        self.page.scroll_down()
        self.page.button_generate.click()

        assert self.page.error_field.text == error_messages['empty_field']

    @pytest.mark.parametrize('field_group', ['participant', 'team'])
    def test_total_follow_changes_on_select(self, field_group):
        test_number = '5'

        section = self.get_section(field_group)

        section.select_number.select_by_value(test_number)

        assert len(section.input_all) == int(test_number), 'Number of inputs should be equal with selected number'
        assert section.total.text == test_number, 'Number of inputs should be equal with the value of counter element'

    @pytest.mark.parametrize('field_group', ['participant', 'team'])
    def test_changes_are_followed_after_delete_an_input(self, field_group):

        section = self.get_section(field_group)
        self.page.button_delete_for(section.input_nth(1)).click()

        actual_input_number = len(section.input_all)
        assert int(section.total.text) == actual_input_number, 'Number of inputs should be equal with the total of inputs'

        selected_value = section.select_number.first_selected_option
        assert int(selected_value.text) == actual_input_number, 'The active option of select should be equal with the total of inputs'
