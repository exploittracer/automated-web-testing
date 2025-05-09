from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the Chrome driver
driver = webdriver.Chrome()

try:
    # 1. Open Google
    driver.get("https://www.google.com")

    # 2. Find the search box
    search_box = driver.find_element(By.NAME, "q")

    # 3. Type in the search term and press Enter
    search_box.send_keys("OpenAI")
    search_box.send_keys(Keys.RETURN)

    # 4. Wait for results to load
    time.sleep(2)

    # 5. Check if 'OpenAI' is in the page title
    assert "OpenAI" in driver.title
    print("Test passed: 'OpenAI' found in the page title.")

except AssertionError:
    print("Test failed: 'OpenAI' not found in the page title.")

finally:
    # 6. Close the browser
    driver.quit()
