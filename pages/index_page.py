from playwright.sync_api import Page
import config


class IndexPage:
    _NAME_FOLDER = "//*[@id='et_pb_contact_name_0']"
    _EMAIL_FOLDER = "//*[@id='et_pb_contact_email_0']"
    _BUTTON_SUBMIT = "//*[@name='et_builder_submit_button']"
    _SUBMISSION_TEXT = "//*[@class='et-pb-contact-message']"


    def open_index_page(self, page: Page) -> None:
        page.goto(config.url.DOMAIN)

    def put_text_in_name_folder(self, page: Page) -> None:
        page.locator(self._NAME_FOLDER).click()
        return page.locator(self._NAME_FOLDER).fill("Temmi")

    def put_text_in_email_folder(self, page: Page) -> None:
        page.locator(self._EMAIL_FOLDER).click()
        return page.locator(self._EMAIL_FOLDER).fill("mail@gmail.com")

    def click_on_submit_button(self, page: Page) -> None:
        return page.locator(self._BUTTON_SUBMIT).click()

    def get_text_after_submission(self, page: Page):
        return page.locator(self. _SUBMISSION_TEXT).inner_text()