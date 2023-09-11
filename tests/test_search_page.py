import allure
import pytest
import pages
import time
from playwright.sync_api import Page, expect





class TestFooter:

    @allure.feature('API link')
    @allure.story('Переход на документацию REST API GITHUB')
    def test_following_the_github_api_link(self, page):
        pages.search_page.open_search_page(page)
        pages.search_page.following_the_github_api_link(page)
        with allure.step('переход по ссылке'):
            actual_result = pages.search_page.rest_api_site_after_link(page)
        assert actual_result == 'REST API', '"REST API" message is not correct'

    @allure.feature('GitHub source')
    @allure.story('Переход на GitHub источник')
    def test_following_the_source_github_link(self, page):
        pages.search_page.open_search_page(page)
        pages.search_page.following_the_github_source_link(page)
        with allure.step('переход по ссылке'):
            actual_result = pages.search_page.source_github_after_lick(page)
        assert actual_result == 'Github User Search ', '"Github User Search " message is not correct'

    @allure.feature('GitHub profile')
    @allure.story('Ввод английского текста в поисковую строку переход на профиль')
    def test_entering_english_text_and_profile(self, page):
        pages.search_page.open_search_page(page)
        pages.search_page.put_text_in_search_fild(page)
        pages.search_page.click_on_the_first_profile(page)
        with allure.step('профиль'):
            actual_result = pages.search_page.profile_repositories(page)
        assert actual_result == 'Repositories', '"Repositories" message is not correct'

    @allure.feature('Site logo')
    @allure.story('Возврат на начальную страницу из профиля')
    def test_return_to_home_page_from_profile(self, page):
        pages.search_page.open_search_page(page)
        pages.search_page.put_text_in_search_fild(page)
        pages.search_page.click_on_the_first_profile(page)
        pages.search_page.click_on_the_site_logo(page)
        with allure.step('начальная страница'):
            expect(page).to_have_url("https://simonsmith.github.io/github-user-search/#/search")

    @allure.feature('Pagination element')
    @allure.story('Переход по элементу пагинации')
    def test_navigating_by_pagination_element(self, page):
        pages.search_page.open_search_page(page)
        pages.search_page.put_text_in_search_fild(page)
        pages.search_page.click_on_the_pagination_button(page)
        with allure.step('Вторая страница результатов поиска'):
            expect(page).to_have_url("https://simonsmith.github.io/github-user-search/#/search?per_page=42&page=2&q=Bob-1")

    @allure.feature('Multiply search')
    @allure.story('Ввод не английского текста в поисковую строку')
    def test_entering_not_english_text(self, page):
        pages.search_page.open_search_page(page)
        pages.search_page.put_invalid_text_in_search_fild(page)
        with allure.step('Результат поиска'):
            expect(page).to_have_url("https://simonsmith.github.io/github-user-search/#/search?per_page=42&page=1&q=%E6%8F%8F")