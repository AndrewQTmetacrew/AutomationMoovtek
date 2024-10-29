from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver

from page_objects.base_page import BasePage


class OTPPage(BasePage):
    __OTP_TITLE = (AppiumBy.XPATH, '//android.widget.TextView[@text="Mã xác thực"]')


    def __init__(self, driver: webdriver):
        super().__init__(driver)

    @property
    def header(self) -> str:
        return super().get_text(self.__OTP_TITLE)
