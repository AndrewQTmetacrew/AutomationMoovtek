import os
import time
from enum import global_str
from pickle import FALSE

import pytest

from page_objects.create_password_page import CreatePasswordPage
from page_objects.login_register_page import LoginRegisterPage
from page_objects.otp_page import OTPPage
from page_objects.password_page import PasswordPage

@pytest.mark.name("Register test")
@pytest.mark.category("Login/Register Tests")
@pytest.mark.description("This test verifies register")
@pytest.mark.run
@pytest.mark.order(2)
class TestRegisterScenario:
    def test_positive_register(self, driver):
        positive_register = LoginRegisterPage(driver)
        registered = OTPPage(driver)

        # Type phone, checked term & policy, click next button
        positive_register.execute_phone_checked_next("0861230005")

        # Verify header OTP page
        assert registered.header == "Mã xác thực"

    @pytest.mark.skipif(os.getenv("is_zalo") == "True", reason= "is_zalo is True")
    def test_get_otp_from_toast(self, driver):
        registered = OTPPage(driver)
        password = CreatePasswordPage(driver)

        # Get OPT code form toast
        otp_code = registered.get_otp_code_from_toast

        # Input OTP code
        registered._input_correct_otp(otp_code)

        # Verify success
        assert password.header_text == "Thiết lập mật khẩu"

    @pytest.mark.skipif(os.getenv("is_zalo") == "False", reason="is_zalo is false")
    def test_get_otp_from_zalo(self, driver):
        registered = OTPPage(driver)

        otp_code = registered.get_otp_code_form_zalo

    def negative_otp_code(self, driver):
        otp = OTPPage(driver)

        # Get OPT code
        self.otp = otp.get_otp_code_form_zalo

        # Input wrong OTP code
        otp._input_wrong_otp(self.otp)

        # Verify error message
        assert otp.error_message == "Mã OTP bạn đã nhập sai vui lòng nhập lại", "Error message is not displayed"

    def expire_otp_code(self, driver):
        otp = OTPPage(driver)

        # Input previous OTP code
        otp._input_expire_otp(self.otp)

        # Verify error message
        assert otp.error_message == "Mã OTP bạn đã nhập sai vui lòng nhập lại", "Error message is not displayed"

    def resend_otp_code(self, driver):
        otp = OTPPage(driver)

        # Get new OTP code
        new_otp = otp.get_otp_code_form_zalo

        # Verify OTP not matching
        assert new_otp != self.otp , "New otp is matching with old otp"

        # Update OTP
        self.otp = new_otp

    def positive_otp_code(self, driver):
        otp = OTPPage(driver)
        password = PasswordPage(driver)

        # Input wrong OTP code
        otp._input_correct_otp(self.otp)

        # Verify

