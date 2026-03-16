from playwright.sync_api import sync_playwright
import time

def myntra_add_to_wishlist():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        
        # 1. Go to Myntra
        page.goto("https://www.myntra.com")
        
        # 2. Search product
        page.fill("input.desktop-searchBar", "shoes")
        page.keyboard.press("Enter")

        # 3. Wait for search results
        page.wait_for_selector("ul.results-base > li", timeout=15000)

        # 4. Click first product and wait for new tab
        with context.expect_page() as new_page_info:
            page.locator("ul.results-base > li").first.click()
        product_page = new_page_info.value
        product_page.wait_for_load_state()

        # 5. Optional: Log in popup might interfere
        # Skip or dismiss it if it appears (you can add logic here)

        # 6. Try clicking wishlist
        try:
            product_page.wait_for_selector("div.pdp-add-to-wishlist", timeout=10000)
            product_page.click("div.pdp-add-to-wishlist")
            print("Clicked wishlist icon")
            # 7. Handle mobile login prompt
            try:
                login_input = product_page.wait_for_selector("input[type='tel']", timeout=8000)
                login_input.fill("9876543210")  # Replace with valid number for testing

                # Check the agreement checkbox
                product_page.wait_for_selector("input[type='checkbox']", timeout=5000)
                product_page.check("input[type='checkbox']")

                print("Looking for CONTINUE button...")
                # Wait for the active continue button to appear and click it
                continue_button = product_page.wait_for_selector("div.submitBottomOption", timeout=20000)
                print("CONTINUE button found, clicking...")
                continue_button.click()

                print("Submitted mobile number and clicked CONTINUE")
            except Exception as login_error:
                print("Login prompt did not appear or failed to submit:", login_error)
        except Exception as e:
            print("Could not click wishlist:", e)

        time.sleep(6)
        browser.close()

if __name__ == "__main__": 
    myntra_add_to_wishlist()