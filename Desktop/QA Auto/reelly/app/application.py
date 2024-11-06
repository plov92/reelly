from pages.main_page import MainPage
from pages.base_page import Page
from pages.secondary_page import SecondaryPage

class Application:
    def __init__(self, driver):
        self.base_page = Page(driver)
        self.main_page = MainPage(driver)
        self.secondary_page = SecondaryPage(driver)


