import os
import time
# adb shell dumpsys window windows | find "mCurrentFocus"

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {
    "platformName": "Android",
    "platformVersion": "9",
    "deviceName": "emulator-5554",
    # "app": "E:\ProjectPython\AutomationMoovtek\Login.apk",
    "appPackage": "com.moovtek.driver.dev",
    "appActivity":"com.moovtek.driver.dev.MainActivity",
    "automationName": "UIautomator2",
    "autoGrantPermissions": "true"
}
options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote('http://localhost:4723', options=options)
driver.implicitly_wait(10)

el1 = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.EditText")
el1.send_keys("0999000006")
el2 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"com.horcrux.svg.PathView\").instance(223)")
el2.click()
el3 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Tiếp tục")
el3.click()
el4 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().resourceId(\"otp_input_0\")")
el4.send_keys("0")
el4 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().resourceId(\"otp_input_1\")")
el4.send_keys("0")
el4 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().resourceId(\"otp_input_2\")")
el4.send_keys("0")
el4 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().resourceId(\"otp_input_3\")")
el4.send_keys("0")
el4 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().resourceId(\"otp_input_4\")")
el4.send_keys("0")
el4 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().resourceId(\"otp_input_5\")")
el4.send_keys("0")
el1 = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.Button")
el1.click()
assert driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Bản đồ").is_displayed()
