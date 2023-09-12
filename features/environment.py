# Selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait

# Allure Reporter
from allure import attach
from allure_commons.types import AttachmentType

# WebDriver
from webdriver_manager import chrome

# Internal
from app.application import Application


def before_scenario(context, scenario):
    # Configure Chrome service & options
    options = webdriver.ChromeOptions()
    driver_path = chrome.ChromeDriverManager().install()
    service = Service(driver_path)

    # Use headless mode if headless option is true (e.g. -D headless=true)
    if context.config.userdata.getbool("headless", default=False):
        options.headless = True
        options.add_argument("window-size=1280,1024")

    # Set Base URL dynamically if it is set in userdata
    baseurl = context.config.userdata.getbool(
        "baseurl", default="https://www.tcgplayer.com"
    )

    # Configure Application
    context.driver = webdriver.Chrome(service=service, options=options)
    context.driver.wait = WebDriverWait(context.driver, timeout=10)
    context.app = Application(
        driver=context.driver, wait=context.driver.wait, baseurl=baseurl
    )

    print(f"Started Scenario: {scenario.name}, Testing Against: {baseurl}.")


def before_step(context, step):
    print(f"Started Step: {step.name}")
    context.driver.get(context.app.baseurl)
    context.driver.maximize_window()


def after_step(context, step):
    if step.status == "Failed":
        print(f"{step} failed.")
        attach(
            context.driver.get_screenshot_as_png(),
            name=f"{step.name}.png",
            attachment_type=AttachmentType.PNG,
        )


def after_scenario(context):
    context.driver.delete_all_cookies()
    context.driver.quit()
