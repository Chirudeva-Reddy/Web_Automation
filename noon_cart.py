from playwright.sync_api import sync_playwright
import time

def add_to_cart_and_go_to_checkout():
    product_url = "https://www.noon.com/uae-en/iphone-16-pro-max-256gb-desert-titanium-5g-with-facetime-international-version/N70106183V/p/?o=ec0700d645f41c7d&shareId=95bf3248-928c-4e6a-8f85-33d27e22c1be"
    cart_url = "https://www.noon.com/uae-en/cart"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=200)
        context = browser.new_context()
        page = context.new_page()

        # Step 1: Go to Product Page
        print("Navigating to product...")
        page.goto(product_url)
        page.wait_for_timeout(4000)

        # Step 2: Click Add to Cart
        try:
            print("Clicking Add to Cart...")
            add_to_cart = page.locator("button:has-text('ADD TO CART')").first
            add_to_cart.wait_for(timeout=15000)
            add_to_cart.click()
            print("Item added to cart")
        except Exception as e:
            print("Add to cart failed:", e)
            browser.close()
            return

        # Step 3: Wait and go to Cart
        time.sleep(4)
        print("Navigating to cart...")
        page.goto(cart_url)
        page.wait_for_timeout(4000)

        # Optional: Click Checkout (if available)
        try:
            checkout_button = page.locator("button:has-text('Checkout')").first
            checkout_button.wait_for(timeout=10000)
            checkout_button.click()
            print("Clicked Checkout")
        except Exception as e:
            print("⚠️ Could not click checkout (login may be required):", e)

        time.sleep(10)
        browser.close()

if __name__ == "__main__":
    add_to_cart_and_go_to_checkout()
    