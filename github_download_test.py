from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
from pathlib import Path


# Set up the Chrome driver
driver = webdriver.Chrome()

# Open the Github text file and read all filenames into a list
with open('github-file-list.txt', 'r') as file:
    filenames = [line.strip() for line in file if line.strip()]

# Define the Downloads folder (default directory to store downloaded files)
downloads = Path("D:/Downloads")

# Iterate through list of filenames
for file in filenames:

    # Attempt downloading the file and verify if downloaded successfully
    try:
        # Open the Github page of downloadable PDF file and wait for 5 seconds
        driver.get("https://github.com/ffisk/books/blob/master/" + file)
        time.sleep(5)

        # Find the download button
        download_button = driver.find_element(By.XPATH, '//*[@id=":rgr:"]/button')

        # Check if the download button is found and displayed on the page
        if download_button and download_button.is_displayed():
            print("https://github.com/ffisk/books/blob/master/" + file + " exist.")

            # Click download button and wait then for 10 seconds in downloading the file
            download_button.click()
            time.sleep(10)

            # Get the full directory of the target file from Downloads folder
            pdf_file = downloads / file

            # Check if the file was successfully downloaded
            if pdf_file.exists():
                print(f"✅ '{pdf_file.name}' downloaded successfully in Downloads folder.")
                print()
            else:
                print(f"❌ '{pdf_file.name}' not found in Downloads.")
                print()

    # If the file does not exist in the Github page
    except NoSuchElementException:
        print("https://github.com/ffisk/books/blob/master/" + file + " does not exist.")
        print()

# Close the browser
driver.quit()
