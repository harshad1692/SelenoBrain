import chromedriver_autoinstaller
chromedriver_autoinstaller.install()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException

def test_login():
    try:
        # Setup the Chrome WebDriver
        driver = webdriver.Chrome()
        driver.get("https://staging-xyz.com/")

        # Wait for the login elements and login
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "Username")))
        username_element = driver.find_element(By.ID, "Username")
        password_element = driver.find_element(By.ID, "Password")
        login_button = driver.find_element(By.ID, "Login")

        username_element.send_keys("owner")
        password_element.send_keys("123@owner")
        login_button.click()

        # Wait for homepage to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "homepage-element")))
        print("✅ Test Passed")
    except TimeoutException:
        print("❌ Test Failed")
    except WebDriverException as e:
        print(f"❌ Test Failed: {e}")
    finally:
        driver.quit()

# Run the test
test_login()
