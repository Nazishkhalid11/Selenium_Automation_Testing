from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1) Launch Chrome
driver = webdriver.Chrome()

try:
    # 2) Open the login page
    driver.get("https://the-internet.herokuapp.com/login")

    # 3) Wait until the username field is present
    wait = WebDriverWait(driver, 10)
    username = wait.until(EC.presence_of_element_located((By.ID, "username")))
    password = driver.find_element(By.ID, "password")

    # 4) Enter credentials
    username.send_keys("tomsmith")
    password.send_keys("SuperSecretPassword!")

    # 5) Click the Login button
    login_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_btn.click()

    # 6) Verify success message
    success = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".flash.success")))
    print("Login successful:", success.text.strip())

finally:
    input("▶️ Press Enter to close the browser…")
    driver.quit()