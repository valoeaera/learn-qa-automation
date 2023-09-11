from selenium.webdriver.common.by import By
from pages.page import Page


class HomePage(Page):
    def open_category_search(self, category_name):
        CATEGORY_DROPDOWN = (By.ID, f"dropdown-{category_name}")
        SHOP_ALL_BUTTON = (By.ID, f"{category_name}-shop-all")

        self.click(*CATEGORY_DROPDOWN)
        self.click(*SHOP_ALL_BUTTON)
