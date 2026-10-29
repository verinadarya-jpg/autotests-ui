from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
   brouser = playwright.chromium.launch(headless=False)
   page = brouser.new_page()
   page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
   page.get_by_test_id("login-form-email-input").locator("input")
   for character in 'user@gmail.com':
       page.keyboard.type(cl)