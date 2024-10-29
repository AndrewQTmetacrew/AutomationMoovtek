import json
import os
import time
from appium import webdriver
import pytest
from appium.options.android import UiAutomator2Options

# adb shell dumpsys window windows | find "mCurrentFocus"

@pytest.fixture(scope="session")
def driver():
    env = int(os.getenv("ENV"))
    if env == 1:
        file_path = "E:/ProjectPython/AutomationMoovtek/desired_caps/real_device.json"
    elif env == 2:
        file_path = "E:/ProjectPython/AutomationMoovtek/desired_caps/virtual_device.json"
    else:
        file_path = True
        pytest.fail("Unsupported device")

    with open(file_path,'r', encoding="utf-8") as file:
        desired_caps = json.load(file)

    options = UiAutomator2Options().load_capabilities(desired_caps)
    driver = webdriver.Remote('http://localhost:4723', options=options)
    driver.implicitly_wait(10)
    yield driver
    time.sleep(1)
    driver.quit()
