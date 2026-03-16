from playwright.sync_api import sync_playwright
import time

def amazon_add_to_cart_direct():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=200)
        context = browser.new_context()
        page = context.new_page()

        # Visit a specific product page (not search result)
        product_url = "https://www.amazon.in/s?k=macbook+pro&crid=QCQ3MF4SRG7F&sprefix=macbook+p%2Caps%2C222&ref=nb_sb_noss_2"  # Example product page
        page.goto(product_url)

        print("Waiting for Add to Cart button...")
        page.wait_for_selector("button[name='submit.addToCart']")

        print("Clicking Add to Cart...")
        page.click("button[name='submit.addToCart']")

        print("✅ Item added to cart!")

        # Navigate to Cart Page
        page.goto("https://www.amazon.in/gp/cart/view.html")
        page.wait_for_timeout(3000)

        # Click Proceed to Buy
        try:
            page.click("input[name='proceedToRetailCheckout']")
            print("✅ Proceeded to checkout")
        except Exception as e:
            print("❌ Failed to proceed to checkout:", e)

        time.sleep(5)
        browser.close()

amazon_add_to_cart_direct()