from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from app.application import Application
from support.logger import logger


def browser_init(context):
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)

    context.app = Application(context.driver)
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)


def before_scenario(context, scenario):
    print("\nStarted Scenario : ", scenario)
    logger.info(f"\nStarted Scenario :  {scenario.name}")
    browser_init(context)


def before_step(context, step):
    print("\nStarted step", step)
    logger.info(f"\nStarted step  {step}")


def after_step(context, step):
    if step.status == 'failed':
        context.driver.save_screenshot(f'./test_results/{step}.png')
        print('\nStep failed: ', step)
        logger.warning(f'\nStep failed:  {step}')


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()



