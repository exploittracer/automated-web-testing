from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the Chrome driver
driver = webdriver.Chrome()

# Open the file and read all filenames into a list
with open('file-list.txt', 'r') as file:
    filenames = [line.strip() for line in file if line.strip()]

# Print the list of filenames
for file in filenames:
    # print(file)

    try:
        # 1. Open Google
        driver.get("https://github.com/ffisk/books/blob/master/" + file)

        # driver.get("https://github.com/ffisk/books/blob/master/are-your-networks-ready-for-the-iot.pdf")
        time.sleep(5)

        # 2. Find the download button
        download_button = driver.find_element(By.XPATH, '//*[@id=":rgr:"]/button')
        
        # 3. Click download button
        download_button.click()

        # 4. Wait for results to load
        time.sleep(10)

        # # 5. Check if 'OpenAI' is in the page title
        # assert "OpenAI" in driver.title
        # print("Test passed: 'OpenAI' found in the page title.")

    except AssertionError:
        print("Test failed: 'OpenAI' not found in the page title.")

    # finally:
# 6. Close the browser
driver.quit()
