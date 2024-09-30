from behave import given, when, then
from selenium.webdriver.common.by import By

from pages.LeaveApplyPage import LeaveApplyPage
from pages.LeaveViewPage import LeaveViewPage

@when('I navigate to "Leave Application"')
def step_impl(context):
    context.leave_apply_page = LeaveApplyPage(context.driver)
    context.leave_apply_page.goto_apply_leave_page()

@when('I fill out the leave application form')
def step_impl(context):
    context.leave_apply_page.select_leave_type_dropdown()
    
    context.leave_apply_page.select_from_date()
    context.leave_apply_page.select_to_date()

    context.leave_apply_page.select_partial_days()
    context.leave_apply_page.select_start_days()
    context.leave_apply_page.select_end_days()

    context.leave_apply_page.add_comments()

@when('I submit the application')
def step_impl(context):
    context.leave_apply_page.click_apply_button()

@then('I should see a confirmation message')
def step_impl(context):
    
    toaster_message = context.leave_apply_page.verify_success()
    assert toaster_message == "Successfully Saved"

@when('I navigate to "Leave Requests"')
def step_impl(context):
    context.leave_view_page = LeaveViewPage(context.driver)
    context.leave_view_page.goto_leave_listview_page()

@when('I search for leave request by employee name')
def step_impl(context):
    context.leave_view_page.search_employee()
    context.leave_view_page.select_employee()

@then('I approve the leave request')
def step_impl(context):
    context.leave_view_page.approve_leave_request()

@then('I should see a confirmation message of leave status "Approved"')
def step_impl(context):
    status = context.leave_view_page.verify_success()
    print(status)
    assert "Successfully Updated" == status
