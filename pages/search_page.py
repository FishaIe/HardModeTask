from playwright.sync_api import Page
import config


class SearchPage:
    _GITHUB_API_LINK = "//*[@href='https://developer.github.com/v3/']"
    _GITHUB_SOURCE_LINK = "//*[@href='https://github.com/simonsmith/github-user-search']"
    _REST_API_GITHUB = "//*[@data-testid='sidebar-product-xl']"
    _SOURCE_GITHUB = "(//*[contains(text(),'Github User Search ')])[last()]"
    _SEARCH_FIELD = "//*[@id='searchInput']"
    _FIRST_PROFILE = "(//*[@class='User_username_rnfkwd'])[1]"
    _PROFILE_REPOSITORIES = "(//*[@class='Profile_contentTitle_123lc5a'])[1]"
    _LOGO_LINK = "//*[@class='Logo_link_18deiwy u-flex']"
    _PAGINATION_BUTTON = "//*[contains(text(),'Next')]"


    def open_search_page(self, page: Page) -> None:
        page.goto(config.url.DOMAIN)

    def following_the_github_api_link(self, page: Page) -> None:
        return page.locator(self._GITHUB_API_LINK).click()

    def following_the_github_source_link(self, page: Page) -> None:
        return page.locator(self._GITHUB_SOURCE_LINK).click()

    def rest_api_site_after_link(self, page: Page):
        return page.locator(self._REST_API_GITHUB).inner_text()

    def source_github_after_lick(self, page: Page):
        return page.locator(self._SOURCE_GITHUB).inner_text()

    def put_text_in_search_fild(self, page: Page) -> None:
        page.locator(self._SEARCH_FIELD).click()
        page.locator(self._SEARCH_FIELD).fill("Bob-1")
        return page.keyboard.press("Enter")

    def put_invalid_text_in_search_fild(self, page: Page) -> None:
        page.locator(self._SEARCH_FIELD).click()
        page.locator(self._SEARCH_FIELD).fill("Где Что")
        page.keyboard.press("Enter")
        page.locator(self._SEARCH_FIELD).fill("سيدنا")
        page.keyboard.press("Enter")
        page.locator(self._SEARCH_FIELD).fill("描")
        return page.keyboard.press("Enter")

    def click_on_the_first_profile(self, page: Page) -> None:
        return page.locator(self._FIRST_PROFILE).click()

    def profile_repositories(self, page: Page):
        return page.locator(self._PROFILE_REPOSITORIES).inner_text()

    def click_on_the_site_logo(self, page: Page) -> None:
        return page.locator(self._LOGO_LINK).click()

    def click_on_the_pagination_button(self, page: Page) -> None:
        return page.locator(self._PAGINATION_BUTTON).click()

