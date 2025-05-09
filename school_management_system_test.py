from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# Configuration
LOGIN_URL = "http://localhost:3000/"  # Replace with actual login URL
USERNAME = "student1"                   # Replace with actual test username
PASSWORD = "student123"                   # Replace with actual test password
EXPECTED_URL = "http://localhost:3000/student"  # URL after successful login

# # Headless Chrome options (optional)
# options = Options()
# options.add_argument("--headless")
# options.add_argument("--disable-gpu")
# options.add_argument("--window-size=1920,1080")

# Start the driver
# driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome()

try:
    # 1. Open login page
    driver.get(LOGIN_URL)
    time.sleep(1)

    # 2. Locate and fill in the username and password fields
    driver.find_element(By.NAME, "username").send_keys(USERNAME)
    time.sleep(1)
    driver.find_element(By.NAME, "password").send_keys(PASSWORD)
    time.sleep(1)


    # 3. Submit the form (either by clicking or hitting Enter)
    driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)

    # 4. Wait for redirect
    time.sleep(3)

    # 5. Check if redirected to the expected URL
    current_url = driver.current_url
    assert current_url == EXPECTED_URL, f"Redirect failed! Expected: {EXPECTED_URL}, Got: {current_url}"
    print("✅ Login redirect test passed.")

except Exception as e:
    print(f"❌ Test failed: {e}")

finally:
    driver.quit()
