import pytest

from page_objects.map_page import MapPage
from page_objects.login_register_page import LoginRegisterPage
from page_objects.password_page import PasswordPage

@pytest.mark.name("Login test")
@pytest.mark.category("Login/Register Tests")
@pytest.mark.description("This test verifies login")
@pytest.mark.run
@pytest.mark.order(2)
class TestLoginScenario:
    def test_positive_login(self, driver):
        positive_login = LoginRegisterPage(driver)
        password = PasswordPage(driver)

        # Type phone, checked term & policy, click next button
        positive_login.execute_phone_checked_next("0997894231")

        # Verify header password page
        assert password.header_text == "Mật khẩu"

    def test_negative_empty_password(self, driver):
        empty_password = PasswordPage(driver)

        # Verify button next status
        assert empty_password.button_next_is_enabled == False , "Button next is enabled when password is empty"

    def test_negative_wrong_password(self, driver):
        wrong_password = PasswordPage(driver)

        # Input wrong password
        wrong_password._input_wrong_password("123456")

        # Verify error message
        assert wrong_password.error_password == "Incorrect Password", "Message error not displayed"

        # Clear password field
        wrong_password._clear_password()

    def test_positive_password(self, driver):
        correct_password = PasswordPage(driver)
        home_bar = MapPage(driver)

        # Input correct password
        correct_password._input_correct_password("000000")

        # Verify header OTP page
        assert home_bar.navigation_bar_map_content == "Bản đồ"
        assert home_bar.navigation_bar_revenue_content == "Doanh thu"
        assert home_bar.navigation_bar_history_content == "Lịch sử"
        assert home_bar.navigation_bar_more_content == "Thêm"