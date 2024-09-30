from configuration.config import TestData
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

# Before All -- It will opens once and After All -- It will close Once
# def before_all(context):
#     context.driver = webdriver.Chrome()
#
#
# def after_all(context):
#     context.driver.close()
#

# def before_feature(context, feature):
#     context.driver = webdriver.Chrome()
#
#
# def after_feature(context, feature):
#     context.driver.close()

def before_scenario(context, scenario):
    if TestData.BROWSER == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--start-maximized')
        # options.add_argument('--start-fullscreen')
        # options.add_argument('--single-process')
        options.add_argument('--disable-dev-shm-usage')
        # options.add_argument("--incognito")
        options.add_argument('--disable-blink-features=AutomationControlled')
        # options.add_experimental_option('useAutomationExtension', False)
        # options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_argument("disable-infobars")
        # options.add_experimental_option("prefs", {"profile.default_content_setting_values.cookies": 2})
        # options.headless = True
        context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        context.driver.implicitly_wait(30)

    elif TestData.BROWSER == 'firefox':

        context.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        context.driver.implicitly_wait(30)
    else:
        context.driver = None
        raise ValueError('Browser is not supported')


def after_scenario(context, scenario):
    context.driver.close()

# def before_tag(context, tag):
#     context.driver = webdriver.Chrome()
#
#
# def after_tag(context, tag):
#     context.driver.close()

# def before_step(context, step):
#     context.driver = webdriver.Chrome()
#
#
# def after_step(context, step):
#     context.driver.close()