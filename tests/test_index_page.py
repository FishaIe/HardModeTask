import pytest
import pages
import time


class TestFooter:

    def test_user_should_be_able_to_open_popup_select_subscription_plan(self, page):
        pages.index_page.open_index_page(page)
        pages.index_page.put_text_in_name_folder(page)
        pages.index_page.put_text_in_email_folder(page)
        pages.index_page.click_on_submit_button(page)
        time.sleep(5)
        actual_result = pages.index_page.get_text_after_submission(page)
        assert actual_result == 'Make sure you fill in all required fields.', '"Make sure you fill in all required fields" is not correct'