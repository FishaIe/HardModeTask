
from playwright.sync_api import sync_playwright

def run(playwright):
    chromium = playwright.chromium # or "firefox" or "webkit".
    browser = chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://simonsmith.github.io/github-user-search/#/search")
    print(page.title())


    browser.close()

with sync_playwright() as playwright:
    run(playwright)