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

    def __input_field_phone(self, phone: str):
        super()._type(self.__PHONE_FIELD, phone)

    def __click_checkbox_uncheck(self):
        super()._click(self.__TERMS_CHECKBOX_UNCHECK)

    def __click_checkbox_checked(self):
        super()._click(self.__TERMS_CHECKBOX_CHECKED)

    def __click_button_next(self):
        super()._click(self.__NEXT_BUTTON)

    def reset_checked(self):
        super()._click(self.__TERMS_CHECKBOX_CHECKED)

    def reset_uncheck(self):
        super()._click(self.__TERMS_CHECKBOX_UNCHECK)

    def execute_phone_checked(self, phone: str):
        self.__input_field_phone(phone)
        self.__click_checkbox_uncheck()

    def execute_phone_checked_next(self, phone: str):
        self.execute_phone_checked(phone)
        self.__click_button_next()


    @property
    def button_next_is_enabled(self) -> bool:
        return super().is_enabled(self.__NEXT_BUTTON)

    @property
    def error_message_text(self) -> str:
        return super().get_text(self.__ERROR_MESSAGE,3)

