from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver

from page_objects.base_page import BasePage

class PasswordPage(BasePage):
    __BACK_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(0)')
    __PASSWORD_TITLE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Mật khẩu")')
    __PASSWORD_CONTENT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Nhập mật khẩu của bạn")')
    __PASSWORD_FIELD_1 = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("otp_input_0")')
    __PASSWORD_FIELD_2 = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("otp_input_1")')
    __PASSWORD_FIELD_3 = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("otp_input_2")')
    __PASSWORD_FIELD_4 = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("otp_input_3")')
    __PASSWORD_FIELD_5 = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("otp_input_4")')
    __PASSWORD_FIELD_6 = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("otp_input_5")')
    __PASSWORD_ERROR = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Incorrect Password")')
    __PASSWORD_SHOW = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Hiện mật khẩu")')
    __PASSWORD_HIDE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Ẩn mật khẩu")')
    __PASSWORD_FORGOT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Quên mật khẩu")')
    __BUTTON_NEXT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("button")')

    #Prepare
    def back(self):
        super()._click(self.__BACK_BUTTON)

    def __show_password(self):
        super()._click(self.__PASSWORD_SHOW)

    def __hide_password(self):
        super()._click(self.__PASSWORD_HIDE)

    def __forgot_password(self):
        super()._click(self.__PASSWORD_FORGOT)

    def __input_password(self, password: str):
        password_field = [
            self.__PASSWORD_FIELD_1,
            self.__PASSWORD_FIELD_2,
            self.__PASSWORD_FIELD_3,
            self.__PASSWORD_FIELD_4,
            self.__PASSWORD_FIELD_5,
            self.__PASSWORD_FIELD_6
        ]
        for i, char in enumerate(password):
            super()._type(password_field[i], char)

    def __clear_password(self):
        super()._click(self.__PASSWORD_FIELD_1)

    def __next(self):
        super()._click(self.__BUTTON_NEXT)

    @property
    def header_text(self) -> str:
        return super().get_text(self.__PASSWORD_TITLE)

    @property
    def content(self) -> str:
        return super().get_text(self.__PASSWORD_CONTENT)

    @property
    def error_password(self) -> str:
        return super().get_text(self.__PASSWORD_ERROR)

    @property
    def button_next_is_enabled(self) -> bool:
        return super().is_enabled(self.__BUTTON_NEXT)

    #Action methods
    def _input_wrong_password(self, password: str):
        self.__input_password(password)
        self.__next()

    def _input_correct_password(self, password: str):
        self.__input_password(password)
        self.__next()

    def _clear_password(self):
        self.__clear_password()
