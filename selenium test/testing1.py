from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def run_test():
    # 1. Initialize the Chrome driver 
    # (Selenium 4.6+ will auto-download ChromeDriver for you)
    print("Starting browser...")
    driver = webdriver.Chrome()

    try:
        # 2. Navigate to Google
        print("Navigating to Google...")
        driver.get("https://www.google.com")

        # 3. Find the search box using its name attribute
        search_box = driver.find_element(By.NAME, "q")

        # 4. Type text and hit enter
        print("Searching for 'ResCollab'...")
        search_box.send_keys("ResCollab")
        search_box.send_keys(Keys.RETURN)

        # 5. Wait a few seconds to see the results
        time.sleep(3) # Note: For real tests, use WebDriverWait instead of time.sleep!

        # Print the title to the console
        print("Test passed! Page title is:", driver.title)

    finally:
        # 6. Close the browser
        print("Closing browser...")
        driver.quit()

if __name__ == "__main__":
    run_test()
