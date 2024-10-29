from appium import webdriver
from appium.webdriver import WebElement
from appium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class BasePage:
    def __init__(self, driver: webdriver):
        self._driver = driver

    def _wait_until_element_visible(self, locator, time):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.viu)

    def  _find(self, locator: tuple) -> WebElement:
        return self._driver.find_element(*locator)

    def _type(self, locator: tuple[str,str], text: str, time: int = 10):
        self._wait_until_element_visible(locator, time)
        self._find(locator).send_keys(text)


