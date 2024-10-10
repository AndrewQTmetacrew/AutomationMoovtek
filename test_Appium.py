import os
import time
# adb shell dumpsys window windows | find "mCurrentFocus"

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {
  "platformName": "Android",
  "appium:platformVersion": "14",
  "appium:deviceName": "OBSWJNR88PZLLZCQ",
  "appium:appPackage": "com.moovtek.driver.dev",
  "appium:appActivity": "com.moovtek.driver.dev.MainActivity",
  "appium:automationName": "UIautomator2",
  "appium:autoGrantPermissions": "true"
}
options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote('http://localhost:4723', options=options)
driver.implicitly_wait(4)

def test_login():
    el1 = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.EditText")
    el1.send_keys("0999000006")
    el2 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"com.horcrux.svg.PathView\").instance(223)")
    el2.click()
    el3 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Tiếp tục")
    el3.click()


    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="otp_input_0"]').send_keys("0")
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="otp_input_1"]').send_keys("0")
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="otp_input_2"]').send_keys("0")
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="otp_input_3"]').send_keys("0")
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="otp_input_4"]').send_keys("0")
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="otp_input_5"]').send_keys("0")
    el1 = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.Button")
    el1.click()
    assert driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Bản đồ").is_displayed()
    time.sleep(2)
    driver.quit()