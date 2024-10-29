from appium import webdriver
from appium.webdriver import WebElement
from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

class BasePage:
    def __init__(self, driver: webdriver):
        self._driver = driver

    def _wait_until_element_visible(self, locator: tuple[str,str], time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.visibility_of_element_located(locator))

    def _wait_until_element_clickable(self, locator: tuple[str,str], time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.element_to_be_clickable(locator))

    def _find(self, locator: tuple) -> WebElement:
        return self._driver.find_element(*locator)

    def _type(self, locator: tuple[str,str], text: str, time: int = 10):
        self._wait_until_element_visible(locator, time)
        self._find(locator).send_keys(text)

    def _click(self, locator: tuple[str,str], time: int = 10):
        self._wait_until_element_clickable(locator, time)
        self._find(locator).click()

    def _clear(self, locator: tuple[str,str], time: int = 10):
        self._wait_until_element_visible(locator, time)
        self._find(locator).clear()

    def is_displayed(self, locator: tuple[str,str]) -> bool:
        try:
            return self._find(locator).is_displayed()
        except NoSuchElementException:
            return False

    def is_enabled(self, locator: tuple[str,str]) -> bool:
        try:
            return self._find(locator).is_enabled()
        except NoSuchElementException:
            return False

    def get_text(self, locator: tuple[str,str], time: int = 10) -> str:
        self._wait_until_element_visible(locator, time)
        return self._find(locator).text