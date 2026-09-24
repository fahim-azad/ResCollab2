from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_login():
    driver = webdriver.Chrome()

    try:
        # Navigate to the local Vite frontend. 
        # (Assuming your app routes '/' or '/login' to the LoginPage)
        print("Navigating to local login page...")
        driver.get("http://localhost:5173/") 

        # Wait up to 10 seconds for the email input to appear
        wait = WebDriverWait(driver, 10)
        print("Looking for email input...")
        email_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='email']")))
        
        print("Looking for password input...")
        password_input = driver.find_element(By.XPATH, "//input[@type='password']")
        
        print("Looking for submit button...")
        submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")

        # Enter dummy credentials 
        # (Change these to a real user in your database to test a successful login)
        print("Entering credentials...")
        email_input.send_keys("azadi4@gmail.com")
        password_input.send_keys("azadi4")

        # Click the Sign In button
        print("Clicking 'Sign In'...")
        submit_button.click()

        # Wait a few seconds to visually see the result (e.g., error message or redirect)
        time.sleep(4)

        # Check if the URL changed to '/profile' which LoginPage.tsx redirects to on success
        if "/profile" in driver.current_url:
            print("✅ Login test passed! Successfully redirected to profile.")
        else:
            print("⚠️ Login test finished, but did not redirect to /profile.")
            print("Current URL is:", driver.current_url)
            
            # If there's an error message on screen, let's try to print it
            try:
                error_div = driver.find_element(By.XPATH, "//div[contains(@style, 'color: #d32f2f')]")
                print("Error shown on screen:", error_div.text)
            except:
                pass

    except Exception as e:
        print("❌ Test failed with exception:", e)

    finally:
        print("Closing browser...")
        driver.quit()

if __name__ == "__main__":
    test_login()
