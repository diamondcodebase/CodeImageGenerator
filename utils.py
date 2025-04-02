from playwright.sync_api import sync_playwright

def take_screenshot(url):
    with sync_playwright() as playwright:
        webkit = playwright.webkit
        browser = webkit.launch()
        browser_context = browser.new_context()
        page = browser_context.new_page()
        page.goto(url)

        # To locate the html element
        element = page.locator("h1")
        print(element.text_content())
        browser.close()

