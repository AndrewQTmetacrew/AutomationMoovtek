from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver

from page_objects.base_page import BasePage


class LoginRegisterPage(BasePage):
    __PHONE_FIELD = (AppiumBy.XPATH, "//android.widget.EditText[@resource-id='text-input-outlined']")
    __ERROR_MESSAGE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Số điện thoại không đúng.")')
    __TERMS_CHECKBOX_UNCHECK = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("check_box_unactive")')
    __TERMS_CHECKBOX_CHECKED = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("check_box_active")')
    __NEXT_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("button")')

    def __init__(self, driver: webdriver):
        super().__init__(driver)

    def execute_phone_format(self, phone: str):
        super()._type(self.__PHONE_FIELD, phone)
        super()._click(self.__TERMS_CHECKBOX_UNCHECK)

    def execute_phone_invalid(self, phone: str):
        super()._type(self.__PHONE_FIELD, phone)
        super()._click(self.__TERMS_CHECKBOX_UNCHECK)
        super()._click(self.__NEXT_BUTTON)

    def execute_phone_valid(self, phone: str):
        super()._type(self.__PHONE_FIELD, phone)
        super()._click(self.__TERMS_CHECKBOX_UNCHECK)

    def execute_sign_in(self, phone: str):
        super()._type(self.__PHONE_FIELD, phone)
        super()._click(self.__TERMS_CHECKBOX_UNCHECK)
        super()._click(self.__NEXT_BUTTON)

    def uncheck_terms(self):
        super()._click(self.__TERMS_CHECKBOX_CHECKED)

    def reset_all(self):
        super()._clear(self.__PHONE_FIELD)
        super()._click(self.__TERMS_CHECKBOX_CHECKED)

    @property
    def button_next_is_enabled(self) -> bool:
        return super().is_enabled(self.__NEXT_BUTTON)

    @property
    def error_message_text(self) -> str:
        return super().get_text(self.__ERROR_MESSAGE,3)

