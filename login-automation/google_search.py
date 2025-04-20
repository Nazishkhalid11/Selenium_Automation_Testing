from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Launch Chrome
driver = webdriver.Chrome()

# Open Google
driver.get("https://www.google.com")
time.sleep(2)

# Find the search box
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium WebDriver with Python")
search_box.send_keys(Keys.RETURN)

# Wait and print title
time.sleep(3)
print("Page title is:", driver.title)

# Close browser
driver.quit()
