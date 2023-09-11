import allure
import pytest
import pages
import time



class TestFooter:

    @allure.feature('Forma')
    @allure.story('Заполнение рандомной формы')
    def test_user_should_be_able_to_open_popup_select_subscription_plan(self, page):
        pages.index_page.open_index_page(page)
        pages.index_page.put_text_in_name_folder(page)
        pages.index_page.put_text_in_email_folder(page)
        pages.index_page.click_on_submit_button(page)
        with allure.step('конец заполнения формы'):
            time.sleep(2)
        actual_result = pages.index_page.get_text_after_submission(page)
        assert actual_result == 'Make sure you fill in all required fields.', '"Make sure you fill in all required fields" is not correct'

    @allure.feature('True')
    @allure.story('Просто проходящий тест')
    def test_success(self):
        """this test succeeds"""
        assert True

    @allure.feature('False')
    @allure.story('Просто падающий тест')
    def test_failure(self):
        """this test fails"""
        assert False