from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
@given('Open the main page https://soft.reelly.io/sign-in')
def open_main_page(context):
    context.app.main_page.open_main_page()

@when('Input {email} as email')
def input_email(context, email):
    context.app.main_page.input_email(email)

@when('Input {password} as password')
def input_pwd(context, password):
    context.app.main_page.input_password(password)

@when('Click "Continue"')
def click_continue(context):
    context.app.main_page.click_continue()

@then('Click on “Secondary” option at the left side menu')
def click_secondary(context):
    context.app.main_page.click_secondary()


@then('Verify the right page opens')
def verify_page(context):
    context.app.secondary_page.verify_page()


@then('Click on Filters')
def click_filters(context):
    context.app.secondary_page.click_filters()

@then('Filter the products by “want to sell”')
def filter_products(context):
    context.app.secondary_page.filter_products()

@then('Click on Apply Filter')
def click_apply_filter(context):
    context.app.secondary_page.click_apply_filter()

@then('Verify all cards have “for sale” tag')
def verify_all_cards(context):
    context.app.secondary_page.verify_all_cards()
