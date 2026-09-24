from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time
import random

def test_register():
    driver = webdriver.Chrome()

    try:
        # Navigate to the registration page 
        # (Assuming the route is /register based on the Link in LoginPage)
        print("Navigating to local register page...")
        driver.get("http://localhost:5173/register")

        # Wait up to 10 seconds for the first input to appear
        wait = WebDriverWait(driver, 10)
        
        print("Locating form fields...")
        # Full Name uses type="text"
        full_name_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='text']")))
        
        # Email uses type="email"
        email_input = driver.find_element(By.XPATH, "//input[@type='email']")
        
        # There are two password fields, so we use XPATH indexing (XPATH is 1-indexed)
        password_input = driver.find_element(By.XPATH, "(//input[@type='password'])[1]")
        confirm_password_input = driver.find_element(By.XPATH, "(//input[@type='password'])[2]")
        
        # Role uses a <select> dropdown
        role_select_element = driver.find_element(By.XPATH, "//select")
        role_select = Select(role_select_element)
        
        # The submit button
        submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")

        print("Entering account details...")
        
        # Generate a random number to make the email unique every time you run the test,
        # otherwise your backend might complain about "Email already exists"
        rand_num = random.randint(1000, 9999)
        test_email = f"newuser{rand_num}@university.edu"
        
        full_name_input.send_keys("Test Researcher")
        email_input.send_keys(test_email)
        
        # Select "researcher" from the dropdown using its HTML value attribute
        role_select.select_by_value("researcher")
        
        password_input.send_keys("SecurePass123!")
        confirm_password_input.send_keys("SecurePass123!")

        print(f"Submitting registration for {test_email}...")
        submit_button.click()

        # Wait a few seconds to visually see the result
        time.sleep(4)

        # Check if redirected to profile (RegisterPage.tsx redirects to /profile on success)
        if "/profile" in driver.current_url:
            print("✅ Registration test passed! Successfully redirected to profile.")
        else:
            print("⚠️ Registration test finished, but did not redirect to /profile.")
            print("Current URL is:", driver.current_url)
            
            # Print error if one appears on screen
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
    test_register()
