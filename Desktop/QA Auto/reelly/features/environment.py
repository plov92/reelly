from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from app.application import Application
from support.logger import logger

# Command to run tests with Allure & Behave:
# behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/target_search.feature
def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """
    # Define Chrome options
    # mobile_emulation = {"deviceName": "Galaxy S8"}
    # options = Options()
    # options.add_argument("--start-maximized")
    # options.add_experimental_option("mobileEmulation", mobile_emulation)
    #
    # # Uncomment the line below for headless mode
    # # options.add_argument("--headless")
    #
    #
    # try:
    #     # Use WebDriverManager to download and set up ChromeDriver
    #     service = Service(ChromeDriverManager().install())
    #     context.driver = webdriver.Chrome(service=service, options=options)
    #     # chrome_options = webdriver.ChromeOptions()
    #
    # except Exception as e:
    #     logger.error(f"Error initializing WebDriver: {e}")
    #     raise

    ### BROWSERSTACK ###
    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    bs_user = 'rustamuktamov_zgtZ8P'
    bs_key = 'VBPqASqmQjrHwKpMawaV'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

    options = Options()
    bstack_options = {
        "deviceName" : "iPhone 13",
        "osVersion" : "18",
        'browserName': 'chromium',
        "deviceOrientation" : "portrait",
        'sessionName': scenario_name,
    }
    options.set_capability('bstack:options', bstack_options)
    context.driver = webdriver.Remote(command_executor=url, options=options)


    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, timeout=10)
    context.app = Application(context.driver)

def before_scenario(context, scenario):
    logger.info(f'Started scenario: {scenario.name}')
    browser_init(context, scenario.name)

def before_step(context, step):
    logger.info(f'Started step: {step}')

def after_step(context, step):
    if step.status == 'failed':
        logger.error(f'Step failed: {step}')

def after_scenario(context, scenario):
    if hasattr(context, 'driver'):
        context.driver.quit()
