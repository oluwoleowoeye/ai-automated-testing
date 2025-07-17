from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import os
import datetime

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def take_screenshot(browser, test_name):
    """Helper function to take screenshots"""
    # Create screenshots directory if it doesn't exist
    if not os.path.exists('screenshots'):
        os.makedirs('screenshots')
    
    # Generate timestamp for unique filename
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Save screenshot
    screenshot_path = f"screenshots/{test_name}_{timestamp}.png"
    browser.save_screenshot(screenshot_path)
    return screenshot_path

def test_valid_login(browser):
  try:
      browser.get(f"file://{os.path.abspath('test_login.html')}")
      username = browser.find_element(By.ID, "username")
      password = browser.find_element(By.ID, "password")
      submit = browser.find_element(By.ID, "submit")
      username.send_keys("admin")
      password.send_keys("password123")
      submit.click()
      message = browser.find_element(By.ID, "message")
      assert "successful" in message.text

     # Take screenshot on success
      screenshot_path = take_screenshot(browser, "test_valid_login_success")
      print(f"Screenshot saved: {screenshot_path}")
        
  except Exception as e:
        # Take screenshot on failure
    take_screenshot(browser, "test_valid_login_failure")
    raise e
    
def test_invalid_login(browser):
  try:
      browser.get(f"file://{os.path.abspath('test_login.html')}")
      username = browser.find_element(By.ID, "username")
      password = browser.find_element(By.ID, "password")
      submit = browser.find_element(By.ID, "submit")
      username.send_keys("invalid_user")
      password.send_keys("wrong_password")
      submit.click()
      message = browser.find_element(By.ID, "message")
      assert "Invalid credentials" in message.text

  # Take screenshot on success
      screenshot_path = take_screenshot(browser, "test_invalid_login_success")
      print(f"Screenshot saved: {screenshot_path}")
        
  except Exception as e:
        # Take screenshot on failure
        take_screenshot(browser, "test_invalid_login_failure")
        raise e

