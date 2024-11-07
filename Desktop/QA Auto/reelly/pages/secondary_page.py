from pages.base_page import Page
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class SecondaryPage(Page):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout=15)
        # self.driver.implicitly_wait(10)
    def verify_page(self):
        assert 'secondary-listings' in self.driver.current_url

    FILTERS_BTN = (By.CSS_SELECTOR, ".filter-button")
    WANT_TO_SELL_BTN = (By.XPATH, "//div[contains(text(), 'Want to sell')]")
    APPLY_FILTER_BTN = (By.CSS_SELECTOR, "[wized='applyFilterButtonMLS']")
    FOR_SALE_TAGS = (By.CSS_SELECTOR, "[wized='saleTagMLS']")

    def click_filters(self):
        # self.wait_for_element_to_appear(self.FILTERS_BTN).click()
        self.wait.until(EC.element_to_be_clickable(self.FILTERS_BTN))
        self.find_element(*self.FILTERS_BTN).click()
        # sleep(5)

    def filter_products(self):
        # self.wait.until(EC.presence_of_element_located(self.WANT_TO_SELL_BTN))
        # self.wait.until(EC.visibility_of_element_located(self.WANT_TO_SELL_BTN))
        self.wait.until(EC.element_to_be_clickable(self.WANT_TO_SELL_BTN))
        self.find_element(*self.WANT_TO_SELL_BTN).click()
        # sleep(10)
    def click_apply_filter(self):
        self.wait.until(EC.element_to_be_clickable(self.APPLY_FILTER_BTN))
        self.find_element(*self.APPLY_FILTER_BTN).click()

    def verify_all_cards(self):
        assert self.find_element(*self.FOR_SALE_TAGS)

