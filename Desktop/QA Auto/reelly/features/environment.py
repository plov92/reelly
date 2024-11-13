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
    options = Options()
    options.add_argument("--start-maximized")
    # Uncomment the line below for headless mode
    # options.add_argument("--headless")

    try:
        # Use WebDriverManager to download and set up ChromeDriver
        service = Service(ChromeDriverManager().install())
        context.driver = webdriver.Chrome(service=service, options=options)
    except Exception as e:
        logger.error(f"Error initializing WebDriver: {e}")
        raise

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
