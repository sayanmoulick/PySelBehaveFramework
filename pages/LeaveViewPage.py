from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.BasePage import BasePage

import time

class LeaveViewPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    leave_menu_button               = (By.XPATH, "//li/a[@href='/web/index.php/leave/viewLeaveModule']")
    leave_list_top_navbar           = (By.XPATH, "//nav/ul/li[6]/a")

    employee_name_field             = (By.XPATH, "//div[@class='oxd-autocomplete-wrapper']//input")
    
    search_button                   = (By.XPATH, "//button[normalize-space()='Search']")
    # search_button                   = (By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']")
    reset_button                    = (By.XPATH, "//button[normalize-space()='Reset']")
    
    toast_message_locator           = (By.XPATH, "//div[@class='oxd-toast-content oxd-toast-content--success']//p[@class='oxd-text oxd-text--p oxd-text--toast-message oxd-toast-content-text']")
    
    leave_requests_locator          = (By.XPATH, "//div[@class='oxd-table-card']")
    first_leave_request_locator     = (By.XPATH, "//div[@class='oxd-table-card'][1]//button[normalize-space()='Approve']")

    def goto_leave_listview_page(self):
        self.do_click(self.leave_menu_button)
        self.do_click(self.leave_list_top_navbar)
        self.take_screen_shot_of_the_page(self.__class__.__name__)

    def search_employee(self):
        employee_name_element = self.get_element(self.employee_name_field)
        self.enter_text(employee_name_element, "sher")
        self.take_screen_shot_of_the_page(self.__class__.__name__)

    def select_employee(self):
        self.action_Chains_Element((By.XPATH, "//div[@class='oxd-autocomplete-option']//*[normalize-space()='Sherlock Holmes']"))
        # self.presence_of_element_located_dev((By.XPATH, "//*[normalize-space()='Sherlock Holmes']"))
        # self.do_click((By.XPATH, "//*[normalize-space()='Sherlock Holmes']"))

        # elem = driver.find_element_by_id("quick-search-query")
        # elem.send_keys("remote")
        # elem.send_keys(Keys.ARROW_DOWN)

        # # wait for the first dropdown option to appear and open it
        # first_option = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".quick-search-dropdown li a")))
        # first_option.send_keys(Keys.RETURN)
        self.take_screen_shot_of_the_page(self.__class__.__name__)

    def approve_leave_request(self):
        self.take_screen_shot_of_the_page(self.__class__.__name__)
        self.presence_of_element_located_dev(self.first_leave_request_locator)
        leave_request_element = self.get_element(self.first_leave_request_locator)
        if leave_request_element.text == 'Approve':
            self.do_click(self.first_leave_request_locator)
        self.take_screen_shot_of_the_page(self.__class__.__name__)

    # def approve_all_leave_requests(self):
    #     leave_requests_elements = self.get_elements(self.leave_requests_locator)
    #     for element in leave_requests_elements:
    #         child_element = element.find_element(By.XPATH, "//button[normalize-space()='Approve']")
    #         if child_element.text == 'Approve':
    #             self.do_click(child_element)
    
    def verify_success(self):
        self.take_screen_shot_of_the_page(self.__class__.__name__)
        return self.get_element_text(self.toast_message_locator)
