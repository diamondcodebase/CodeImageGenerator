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


def take_screenshot_img(url):
    with sync_playwright() as playwright:
        webkit = playwright.webkit
        browser = webkit.launch()
        browser_context = browser.new_context()
        page = browser_context.new_page()
        page.goto(url)

        # To locate the html element
        element = page.locator("h1")
        screenshot_bytes = element.screenshot()
        browser.close()

        # save the screenshot as an image file
        with open("screenshot.png", mode = "wb") as img:
            img.write(screenshot_bytes)

if __name__ == "__main__":
    take_screenshot_img("http://127.0.0.1:5000")