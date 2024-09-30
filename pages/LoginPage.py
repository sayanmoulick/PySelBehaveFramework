from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.BasePage import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    login_text = (By.XPATH, "//h5[contains(@class, 'orangehrm-login-title')]")
    username_field = (By.XPATH, "//input[@placeholder='Username']")
    password_field = (By.XPATH, "//input[@placeholder='Password']")
    login_button   = (By.XPATH, "//button[normalize-space()='Login']")
    header_text    = (By.XPATH, "//h6[contains(@class,'oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module')]")
    login_error    = (By.XPATH, "//div[contains(@class, 'oxd-alert-content oxd-alert-content--error')]/p")

    def get_login_page_text(self):
        return self.get_element_text(self.login_text)
    
    def get_username_field(self):
        return self.get_element(self.username_field)

    def get_pass_field(self):
        return self.get_element(self.password_field)

    def get_login_button(self):
        return self.get_element(self.login_button)

    def click_login_button(self):
        self.do_click(self.login_button)

    def get_header_text(self):
        return self.get_element_text(self.header_text)

    def get_login_error_text(self):
        return self.get_element_text(self.login_error)