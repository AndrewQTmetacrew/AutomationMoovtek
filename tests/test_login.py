import time

import pytest

from conftest import driver
from page_objects.login_register_page import LoginRegisterPage
from page_objects.otp_page import OTPPage
from page_objects.password_page import PasswordPage


@pytest.mark.run
class TestLoginRegisterScenario:
    @pytest.mark.name("Login and register with an incorrect phone number format")
    @pytest.mark.category("Login/Register Tests")
    @pytest.mark.description("This test verifies the behavior when an incorrect phone number format is entered.")
    def test_negative_phone_format(self, driver):
        negative_phone_format = LoginRegisterPage(driver)

        #Type phone, checked term & policy, click next button
        negative_phone_format.execute_phone_checked("03922226")

        #Verify button Next not enable
        assert negative_phone_format.button_next_is_enabled == False, "Button Next is enabled with invalid phone"

        # Reset
        negative_phone_format.reset_checked()

    @pytest.mark.name("Login and register with an invalid phone number")
    @pytest.mark.category("Login/Register Tests")
    @pytest.mark.description("This test verifies the behavior when an invalid phone number is entered.")
    @pytest.mark.parametrize("phone, error_message",
                             [("0232222283", "Số điện thoại không đúng."),
                              ("02342222283", "Số điện thoại không đúng.")])

    def test_negative_phone_invalid(self, driver, phone, error_message):
        negative_phone_invalid = LoginRegisterPage(driver)

        #Type phone, checked term & policy
        negative_phone_invalid.execute_phone_checked_next(phone)

        #Verify button Next was enabled
        assert negative_phone_invalid.error_message_text == error_message, "Error message is not correct"

        #Reset
        negative_phone_invalid.reset_checked()

    @pytest.mark.name("Login and register without agreeing to the terms & services")
    @pytest.mark.category("Login/Register Tests")
    @pytest.mark.description("This test verifies the behavior when without agreeing to the terms & services.")
    def test_negative_uncheck_terms(self, driver):
        negative_uncheck_term = LoginRegisterPage(driver)

        #Type phone, checked term & policy
        negative_uncheck_term.execute_phone_checked("0856461679")

        #Verify button Next enable
        assert negative_uncheck_term.button_next_is_enabled == True, "Button Next is not enabled"

        #Uncheck agree terms & services
        negative_uncheck_term.reset_checked()

        #Verify button Next not enable
        assert negative_uncheck_term.button_next_is_enabled == False, "Button Next is enabled"

    @pytest.mark.name("Register test")
    @pytest.mark.category("Login/Register Tests")
    @pytest.mark.description("This test verifies register")
    def test_positive_register(self, driver):
        positive_register = LoginRegisterPage(driver)
        registered = OTPPage(driver)

        # Type phone, checked term & policy, click next button
        positive_register.execute_phone_checked_next("0396565656")

        #Verify header OTP page
        assert registered.header == "Mã xác thực"

        #Click back button
        registered.back()

        # Uncheck agree terms & services
        positive_register.reset_checked()


    @pytest.mark.name("Register test")
    @pytest.mark.category("Login/Register Tests")
    @pytest.mark.description("This test verifies login")
    def test_positive_login(self, driver):
        positive_login = LoginRegisterPage(driver)
        password = PasswordPage(driver)

        # Type phone, checked term & policy, click next button
        positive_login.execute_phone_checked_next("0856461679")

        # Verify header OTP page
        assert password.header == "Mật khẩu"

        # Click back button
        password.back()