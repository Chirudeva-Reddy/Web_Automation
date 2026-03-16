from playwright.sync_api import sync_playwright

def basic_amazon_search():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # 1. Open Amazon India
        page.goto("https://www.amazon.in")

        # 2. Search for 'macbook pro'
        page.fill("input[name='field-keywords']", "macbook pro")
        page.keyboard.press("Enter")

        # 3. Wait for product links to load
        page.wait_for_selector("div.s-main-slot div[data-index] h2 a", timeout=15000)

        # 4. Click on the first product
        page.locator("div.s-main-slot div[data-index] h2 a").first.click()

        # 5. Pause so we can visually verify
        page.wait_for_timeout(5000)
        browser.close()

basic_amazon_search()