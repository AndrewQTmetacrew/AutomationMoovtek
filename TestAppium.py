import os
import time

# adb shell
# dumpsys window displays | grep -E “mCurrentFocus”

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {
    "platformName": "Android",
    "platformVersion": "9",
    "deviceName": "ce08171840f17808057e",
    "automationName": "UIautomator2",
    "autoGrantPermissions": "true"
}
options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote('http://localhost:4723', options=options)
driver.implicitly_wait(1)
e0 = driver.find_element(by=AppiumBy.ID, value="sdpd.login:id/editText")
e0.click()
e0.send_keys("Username")
e1 = driver.find_element(by=AppiumBy.ID, value="sdpd.login:id/editText2")
e1.click()
e1.send_keys("Password")
e3 = driver.find_element(by=AppiumBy.ID, value="sdpd.login:id/button")
e3.click()
time.sleep(2)
driver.quit()
