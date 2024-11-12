from appium.webdriver.common.appiumby import AppiumBy

from page_objects.base_page import BasePage


class OTPPage(BasePage):
    __OTP_TITLE = (AppiumBy.XPATH, '//android.widget.TextView[@text="Mã xác thực"]')
    __BACK_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.SvgView").instance(0)')
    __OTP_CODE_TOAST = (AppiumBy.XPATH,
                        '//android.view.ViewGroup[@resource-id="toastAnimatedContainer"]'
                        '/android.view.ViewGroup/android.widget.TextView')
    __OTP_CODE_ZALO= (AppiumBy.XPATH,
        '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.zing.zalo:id/recycler_view_msgList"]'
        '/android.widget.FrameLayout[contains(@text, "MOOVTEK")]')
    __OTP_FIELD_1 = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("otp_input_0")')
    __OTP_FIELD_2 = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("otp_input_1")')
    __OTP_FIELD_3 = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("otp_input_2")')
    __OTP_FIELD_4 = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("otp_input_3")')
    __OTP_FIELD_5 = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("otp_input_4")')
    __OTP_FIELD_6 = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("otp_input_5")')
    __ERROR_MESSAGE = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Mã OTP bạn đã nhập sai vui lòng nhập lại")')
    __RESEND_OTP = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Gửi lại mã")')

    # Prepare
    def __input_otp_code(self, otp_code):
        opt_field = [
            self.__OTP_FIELD_1,
            self.__OTP_FIELD_2,
            self.__OTP_FIELD_3,
            self.__OTP_FIELD_4,
            self.__OTP_FIELD_5,
            self.__OTP_FIELD_6
        ]
        for i, char in enumerate(otp_code):
            super()._type(opt_field[i], char)

    # Action methods
    def back(self):
        super()._click(self.__BACK_BUTTON)

    def _input_correct_otp(self, otp_code):
        self.__input_otp_code(otp_code)

    def _input_wrong_otp(self, otp_code):
        reverse_otp_code = otp_code[::-1]
        self.__input_otp_code(reverse_otp_code)

    def _input_expire_otp(self, otp_code):
        super()._click(self.__RESEND_OTP, 70)
        self.__input_otp_code(otp_code)

    @property
    def get_otp_code_from_toast(self) -> str:
        return super().get_text(self.__OTP_CODE_TOAST)

    @property
    def get_otp_code_form_zalo(self) -> str:
        super()._change_app("com.zing.zalo")
        content_zns = super().get_text(self.__OTP_CODE_ZALO)
        start_index = content_zns.find("Mã xác thực của bạn là") + len("Mã xác thực của bạn là")
        super()._change_app("com.moovtek.driver.dev")
        return content_zns[start_index:start_index + 7].strip()

    @property
    def header(self) -> str:
        return super().get_text(self.__OTP_TITLE)

    @property
    def error_message(self) -> str:
        return super().get_text(self.__ERROR_MESSAGE)
