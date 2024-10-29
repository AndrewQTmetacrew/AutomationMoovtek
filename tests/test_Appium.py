import time

import pytest
from appium.webdriver.common.appiumby import AppiumBy

def get_otp(driver):
    toast_opt_locator = (AppiumBy.CLASS_NAME, 'android.widget.TextView')
    toast_opt = driver.find_elements(*toast_opt_locator)[5]
    otp_code = [int(digit) for digit in str(toast_opt.text)]
    return otp_code


class TestRegisterScenario:
    @pytest.mark.parametrize("phone, status_btn",[("03922226", False)])
    def test_register_negative_phone_format(self, driver, phone, status_btn):
        phone_input_locator = (AppiumBy.XPATH, "//android.widget.EditText[@resource-id='text-input-outlined']")
        btn_next_locator = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("button")')
        checkbox_term_locator = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("check_box_unactive")')

        # Click checkbox term & policy
        checkbox_term = driver.find_element(*checkbox_term_locator)
        checkbox_term.click()

        # Input phone
        phone_input = driver.find_element(*phone_input_locator)
        phone_input.send_keys(phone)

        # Check button login not enable
        btn_next = driver.find_element(*btn_next_locator)
        assert btn_next.is_enabled() == status_btn


    @pytest.mark.parametrize("phone, status_btn , error_message",
                             [("0232222226", True, "Số điện thoại không đúng.")])
    def test_register_negative_phone_invalid(self, driver, phone, status_btn, error_message):
        phone_input_locator = (AppiumBy.XPATH, "//android.widget.EditText[@resource-id='text-input-outlined']")
        btn_next_locator = (AppiumBy.ACCESSIBILITY_ID, "Tiếp tục")
        error_message_locator = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Số điện thoại không đúng.")')


        # Input phone
        phone_input = driver.find_element(*phone_input_locator)
        phone_input.send_keys(phone)

        # Check button login not enable
        btn_next = driver.find_element(*btn_next_locator)
        assert btn_next.is_enabled() == status_btn

        #Click next
        btn_next.click()

        assert driver.find_element(*error_message_locator).text == error_message


    @pytest.mark.parametrize("phone, status_btn, error_message",
                             [("0392222283", True, "")])
    def test_registered_positive(self, driver, phone, status_btn, error_message):
        phone_input_locator = (AppiumBy.XPATH, "//android.widget.EditText[@resource-id='text-input-outlined']")
        btn_next_locator = (AppiumBy.ACCESSIBILITY_ID, "Tiếp tục")
        otp_title_locator = (AppiumBy.XPATH, '//android.widget.TextView[@text="Mã xác thực"]')


        #Input phone
        phone_input = driver.find_element(*phone_input_locator)
        phone_input.send_keys(phone)

        # Check button login not enable
        btn_next = driver.find_element(*btn_next_locator)
        assert btn_next.is_enabled()

        #Click next
        btn_next.click()
        # assert not driver.find_element(*error_message_locator).is_displayed()

        #Check re-direct to OTP screen
        otp_title = driver.find_element(*otp_title_locator)
        assert otp_title.text == "Mã xác thực"

    # def test_input_otp_negative():
    #     error_message = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Mã OTP bạn đã nhập sai vui lòng nhập lại")')
    #
    #     otp_code = get_otp()
    #     otp_code.reverse()
    #
    #     for i in range(len(otp_code)):
    #         otp_input_locator = (AppiumBy.XPATH, f'//android.widget.EditText[@resource-id="otp_input_{i}"]')
    #         driver.find_element(*otp_input_locator).send_keys(f"{otp_code[i]}")
    #     assert driver.find_element(*error_message).text == "Mã OTP bạn đã nhập sai vui lòng nhập lại"

    def test_input_otp(self, driver):
        create_password_title_locator = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Thiết lập mật khẩu")')
        otp_code = get_otp(driver)
        for i in range(len(otp_code)):
            otp_input_locator = (AppiumBy.XPATH, f'//android.widget.EditText[@resource-id="otp_input_{i}"]')
            driver.find_element(*otp_input_locator).send_keys(f"{otp_code[i]}")

        create_password_title = driver.find_element(*create_password_title_locator)
        assert create_password_title.text == "Thiết lập mật khẩu"


    def test_input_password(self, driver):
        register_title_locator = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Đăng ký trở thành đối tác")')
        password = "000000"
        password = [int(digit) for digit in password]
        for i in range(len(password)):
            password_locator = (AppiumBy.XPATH,f'//android.widget.EditText[@resource-id="otp_input_{i}"]')
            driver.find_element(*password_locator).send_keys(f"{password[i]}")

        el1 = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.Button")
        el1.click()

        register_title = driver.find_element(*register_title_locator)
        assert register_title.text == "Đăng ký trở thành đối tác"

    # def test_register_info(self, driver):
    #     el18 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().resourceId("text-input-outlined").instance(0)')
    #     el18.send_keys("Đào Văn Tuấn")
    #     el19 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
    #                                value='new UiSelector().resourceId("text-input-outlined").instance(1)')
    #     el19.send_keys("tuan@gmail.com")
    #     el20 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().resourceId("text-input-outlined").instance(2)')
    #     el20.click()
    #     el21 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().description("Hồ Chí Minh")')
    #     el21.click()
    #     el23 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().resourceId("text-input-outlined").instance(3)')
    #     el23.click()
    #     el22 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().description("MOOVTEK BIKE")')
    #     el22.click()
    #     el24 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().resourceId("text-input-outlined").instance(4)')
    #     el24.send_keys("ABC17823")
    #     el25 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().resourceId("button")')
    #     el25.click()
    #     el26 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().description("Xác nhận gửi")')
    #     el26.click()
    #     el27 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value= 'new UiSelector().text("Đăng ký trở thành đối tác")')
    #     assert el27.text == "Đăng ký trở thành đối tác"
