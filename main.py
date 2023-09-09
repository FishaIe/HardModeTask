from playwright.sync_api import sync_playwright

def run(playwright):
    chromium = playwright.chromium # or "firefox" or "webkit".
    browser = chromium.launch()
    page = browser.new_page()
    page.goto("https://courses.ultimateqa.com/users/sign_in")
    print(page.title())


    browser.close()

with sync_playwright() as playwright:
    run(playwright)