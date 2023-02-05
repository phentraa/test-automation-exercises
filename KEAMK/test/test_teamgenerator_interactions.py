import pytest, allure
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

    @allure.id('T201')
    @allure.title('Submit form with empty title')
    @allure.description("""
        Submit the empty form with clicking on the Generate Teams button
        Expected result: an error message appears because the Title field can not be empty.
        """)
    @allure.severity(allure.severity_level.MINOR)
    def test_submit_with_empty_title(self, error_messages):
        self.page.scroll_down()
        self.page.button_generate.click()

        assert self.page.error_field.text == error_messages['empty_title']

    # ------------------------------------------------------------------------------------------------------------------

    @allure.id('T202')
    @allure.title('Submit form with Participants / Teams fields')
    @allure.description("""
            1. Fill out the Title input with valid data
            2. Fill the first input of Participants or Teams section with valid data.
            Leave the other section empty.
            3. Submit the form with clicking on the Generate Teams button
            Expected result: an error message appears in both cases when an input field had been left empty.
            """)
    @allure.severity(allure.severity_level.MINOR)
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

    # ------------------------------------------------------------------------------------------------------------------

    @allure.id('T203')
    @allure.title('Check effects when select changes')
    @allure.description("""
                1. Change the select value of Participant section
                2. Change the select value of Teams section

                Expected result (in both cases):
                - The number of input fields changes as the selected value indicates
                - The indicator on the left of the Add new button shows the same value
                as the selected value. 
                """)
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize('field_group', ['participant', 'team'])
    def test_total_follows_changes_of_select(self, field_group):
        test_number = '5'

        section = self.get_section(field_group)
        section.select_number.select_by_value(test_number)

        assert len(section.input_all) == int(test_number), 'Number of inputs should be equal with selected number'
        assert section.total.text == test_number, 'Number of inputs should be equal with the value of counter element'

    # ------------------------------------------------------------------------------------------------------------------

    @allure.id('T204')
    @allure.title('Check effects when delete an input field')
    @allure.description("""
                   1. Delete the first input from the Participants section list
                   2. Delete the first input from the Teams section list
                   
                   Expected result (in both cases):
                   - The value of the number selector - related to the correct section - changes to the
                   actual input field number
                   - The value of the total number indicator left to the Add new button - related to the correct section - 
                   changes to the actual input field number
                   """)
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize('field_group', ['participant', 'team'])
    def test_changes_are_followed_after_delete_an_input(self, field_group):

        section = self.get_section(field_group)
        self.page.button_delete_for(section.input_nth(1)).click()

        actual_input_number = len(section.input_all)
        assert int(section.total.text) == actual_input_number, 'Number of inputs should be equal with the total of inputs'

        selected_value = section.select_number.first_selected_option
        assert int(selected_value.text) == actual_input_number, 'The active option of select should be equal with the total of inputs'

    # ------------------------------------------------------------------------------------------------------------------

    @allure.id('T205')
    @allure.title('Check effects when add a new input field')
    @allure.description("""
                       1. Click on the Add Participant button
                       2. Click on the Add Team button

                       Expected result (in both cases):
                       - The value of the number selector - related to the correct section - changes to the
                       actual input field number
                       - The value of the total number indicator left to the Add new button - related to the correct section - 
                       changes to the actual input field number.
                       """)
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize('field_group', ['participant', 'team'])
    def test_changes_are_followed_after_add_new_input(self, field_group):
        section = self.get_section(field_group)
        input_total = len(section.input_all)

        self.page.scroll_down()
        section.button_add.click()
        new_input_total = len(section.input_all)
        assert new_input_total == input_total + 1
        assert int(section.total.text) == new_input_total
        assert int(section.select_number.first_selected_option.text) == new_input_total

