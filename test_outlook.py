from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://outlook.office.com/mail/")

    print("Title:", page.title())
    print("URL:", page.url)

    input("Check the page. Press Enter in the terminal to close...")
    browser.close()
