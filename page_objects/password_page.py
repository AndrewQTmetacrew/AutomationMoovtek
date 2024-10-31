from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver

from page_objects.base_page import BasePage

class PasswordPage(BasePage):
    __BACK_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.SvgView").instance(0)')
    __PASSWORD_TITLE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Mật khẩu")')


    def __init__(self, driver: webdriver):
        super().__init__(driver)

    def back(self):
        super()._click(self.__BACK_BUTTON)

    @property
    def header(self) -> str:
        return super().get_text(self.__PASSWORD_TITLE)
