from pages.base_page import Page
from time import sleep
from selenium.webdriver.common.by import By

class MainPage(Page):
    def open_main_page(self):
        self.open('https://soft.reelly.io/sign-in')

    INPUT_EMAIL = (By.ID, "email-2")
    INPUT_PASSWORD = (By.ID, "field")
    CONTINUE = (By.XPATH, "//a[contains(text(), 'Continue')]")
    SECONDARY_BTN = (By.XPATH, "//div[contains(text(), 'Secondary')]")


    def input_email(self, email):
        self.find_element(*self.INPUT_EMAIL).send_keys(email)

    def input_password(self, password):
        self.find_element(*self.INPUT_PASSWORD).send_keys(password)

    def click_continue(self):
        self.find_element(*self.CONTINUE).click()

    def click_secondary(self):
        self.find_element(*self.SECONDARY_BTN).click()



    def verify_cant_find_account(self):
        self.wait_for_element_to_appear(*self.CANT_FIND_ACCOUNT)
        sleep(3)