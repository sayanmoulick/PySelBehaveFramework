from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC

from pages.BasePage import BasePage

import time

class LeaveApplyPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    leave_menu_button               = (By.XPATH, "//li/a[@href='/web/index.php/leave/viewLeaveModule']")
    apply_leave_top_navbar          = (By.XPATH, "//nav/ul/li[1]/a")

    apply_leave_type_dropdown       = (By.XPATH, "//div[contains(@class, 'oxd-select-text-input')]")
    
    apply_leave_from_date_field     = (By.XPATH, "//div[contains(@class,'oxd-grid-4 orangehrm-full-width-grid')]//div[1]//div//div[2]//input[contains(@class,'oxd-input oxd-input--active')]")
    apply_leave_from_date_picker    = (By.XPATH, "//div[contains(@class,'oxd-grid-4 orangehrm-full-width-grid')]//div[1]//div//div[2]//i[contains(@class,'oxd-icon bi-calendar oxd-date-input-icon')]")
    apply_leave_to_date_field       = (By.XPATH, "//div[contains(@class,'oxd-grid-4 orangehrm-full-width-grid')]//div[2]//div//div[2]//input[contains(@class,'oxd-input oxd-input--active')]")
    apply_leave_to_date_picker      = (By.XPATH, "//div[contains(@class,'oxd-grid-4 orangehrm-full-width-grid')]//div[2]//div//div[2]//i[contains(@class,'oxd-icon bi-calendar oxd-date-input-icon')]")
    apply_button                    = (By.XPATH, "//button[text()[normalize-space() = 'Apply']]")
    leave_balance_left              = (By.XPATH, "//p[contains(@class,'orangehrm-leave-balance-text')]")

    calender_year_selector          = (By.XPATH, "//li[@class='oxd-calendar-selector-year']//p[1]")
    calender_month_selector         = (By.XPATH, "//div[@class='oxd-calendar-selector-month-selected']")
    calender_month_swipe_left       = (By.XPATH, "//button[@class='oxd-icon-button']//i[@class='oxd-icon bi-chevron-left']")
    calender_month_swipe_right      = (By.XPATH, "//button[@class='oxd-icon-button']//i[@class='oxd-icon bi-chevron-right']")

    partial_days_locator            = (By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//form[@class='oxd-form']/div[3]//div[@class='oxd-select-wrapper']/div[1]/div[@class='oxd-select-text-input']")
    start_day_selector              = (By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//form[@class='oxd-form']/div[3]/div/div[2]/div//div[@class='oxd-select-wrapper']/div[1]")
    end_day_selector                = (By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//form[@class='oxd-form']/div[3]/div/div[3]/div//div[@class='oxd-select-wrapper']/div[1]")

    comments_area_locator           = (By.XPATH, "//textarea[contains(@class, 'oxd-textarea oxd-textarea--active oxd-textarea--resize-vertical')]")
    toast_message_locator           = (By.XPATH, "//div[@class='oxd-toast oxd-toast--success oxd-toast-container--toast']//p[@class='oxd-text oxd-text--p oxd-text--toast-message oxd-toast-content-text']")
    
    # toast_message_locator           = (By.XPATH, "//div[@class='oxd-toast oxd-toast--success oxd-toast-container--toast']")

    # //li[normalize-space()='2027'] //p[normalize-space()='September']  //li[normalize-space()='June']  
    
    def goto_apply_leave_page(self):
        self.do_click(self.leave_menu_button)
        self.do_click(self.apply_leave_top_navbar)
        self.take_screen_shot_of_the_page(self.__class__.__name__)

    def select_leave_type_dropdown(self):
        self.do_click(self.apply_leave_type_dropdown)
        # time.sleep(5)
        # print(self.get_elements((By.XPATH, "//div[contains(@class,'oxd-select-dropdown --position-bottom')]")))
        self.action_Chains_Element((By.XPATH, "//div[@class='oxd-grid-4 orangehrm-full-width-grid']//div[1]//div[1]//div[2]//div[1]//div[1]//i[1]"))
        self.take_screen_shot_of_the_page(self.__class__.__name__)
   
    def select_from_date(self):
        # self.take_screen_shot_of_the_page(self.__class__.__name__)
        self.do_click(self.apply_leave_from_date_field)
        self.do_click(self.calender_year_selector)
        self.do_click((By.XPATH, "//li[normalize-space()='2025']"))
        self.do_click(self.calender_month_selector)
        self.do_click((By.XPATH, "//li[normalize-space()='May']"))
        self.do_click((By.XPATH, "//div[contains(text(),'2')]"))
        self.take_screen_shot_of_the_page(self.__class__.__name__)

    def select_to_date(self):
        self.do_click(self.apply_leave_to_date_field)
        self.do_click(self.calender_year_selector)
        self.do_click((By.XPATH, "//li[normalize-space()='2025']"))
        # self.do_click(self.calender_month_swipe_right)
        self.do_click(self.calender_month_selector)
        self.do_click((By.XPATH, "//li[normalize-space()='May']"))
        self.do_click((By.XPATH, "//div[contains(text(),'9')]"))
        self.take_screen_shot_of_the_page(self.__class__.__name__)

    def select_partial_days(self):
        self.do_click(self.partial_days_locator)
        # dropdown_elements = self.return_list((By.XPATH, "//div[contains(@class,'oxd-select-dropdown --position-bottom')]"))
        # for element in dropdown_elements:
        #     if element.text == "Start Day Only":
        #         self.do_click(element)
        self.do_click((By.XPATH, "//*[normalize-space()='Start Day Only']"))
        self.take_screen_shot_of_the_page(self.__class__.__name__)

    def select_start_days(self):
        self.do_click(self.start_day_selector)
        self.do_click((By.XPATH, "//*[normalize-space()='Half Day - Afternoon']"))
        self.take_screen_shot_of_the_page(self.__class__.__name__)

    def select_end_days(self):
        # self.do_click(self.end_day_selector)
        pass

    def add_comments(self):
        comment_element = self.get_element(self.comments_area_locator)
        self.enter_text(comment_element, "It's elementary!")
        self.take_screen_shot_of_the_page(self.__class__.__name__)

    def click_apply_button(self):
        self.do_click(self.apply_button)

    def verify_success(self):
        self.take_screen_shot_of_the_page(self.__class__.__name__)
        return self.get_element_text(self.toast_message_locator)

    # def getApplyLeaveTypeDropdown(self):
    #     return self.get_element(self.apply_leave_type_dropdown)

    # def getApplyLeaveFromDateField(self):
    #     return self.get_element(self.apply_leave_from_date_field)

    # def getApplyLeaveFromDatePicker(self):
    #     return self.get_element(self.apply_leave_from_date_picker)

    # def getApplyLeaveToDateField(self):
    #     return self.get_element(self.apply_leave_to_date_field)

    # def getApplyLeaveToDatePicker(self):
    #     return self.get_element(self.apply_leave_to_date_picker)

    

    def getLeaveBalanceLeftText(self):
        return self.get_element(self.leave_balance_left).text