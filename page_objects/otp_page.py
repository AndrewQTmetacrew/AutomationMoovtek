from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver

from page_objects.base_page import BasePage


class OTPPage(BasePage):
    __OTP_TITLE = (AppiumBy.XPATH, '//android.widget.TextView[@text="Mã xác thực"]')
    __BACK_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.SvgView").instance(0)')


    def __init__(self, driver: webdriver):
        super().__init__(driver)

    def back(self):
        super()._click(self.__BACK_BUTTON)
        super()._click(self.__BACK_BUTTON)

    @property
    def header(self) -> str:
        return super().get_text(self.__OTP_TITLE)

