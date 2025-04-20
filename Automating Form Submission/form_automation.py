from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup ChromeDriver correctly
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get("https://www.w3schools.com/html/html_forms.asp")
    time.sleep(2)

    # Locate and fill the form
    first_name = driver.find_element(By.NAME, "fname")
    last_name = driver.find_element(By.NAME, "lname")
    first_name.send_keys("HELLO")
    last_name.send_keys("BYE")

    # Submit
    submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")
    submit_button.click()

except Exception as e:
    print("⚠️ An error occurred:", e)

finally:
    input("▶️ Press Enter to close the browser…")
    driver.quit()