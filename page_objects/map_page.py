from appium.webdriver.common.appiumby import AppiumBy

from page_objects.base_page import BasePage


class MapPage(BasePage):
    __NAVIGATION_BAR_MAP = (AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='Bản đồ']/android.widget.TextView")
    __NAVIGATION_BAR_REVENUE = (AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='Doanh thu']/android.widget.TextView")
    __NAVIGATION_BAR_HISTORY = (AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='Lịch sử']/android.widget.TextView")
    __NAVIGATION_BAR_MORE = (AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='Thêm']/android.widget.TextView")


    @property
    def navigation_bar_map_content(self) -> str:
        return super().get_text(self.__NAVIGATION_BAR_MAP)

    @property
    def navigation_bar_revenue_content(self) -> str:
        return super().get_text(self.__NAVIGATION_BAR_REVENUE)

    @property
    def navigation_bar_history_content(self) -> str:
        return super().get_text(self.__NAVIGATION_BAR_HISTORY)

    @property
    def navigation_bar_more_content(self) -> str:
        return super().get_text(self.__NAVIGATION_BAR_MORE)
