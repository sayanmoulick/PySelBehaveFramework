from behave import given, when, then
from selenium.webdriver.common.by import By

from pages.LoginPage import LoginPage

@given('I am on the login page')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.load_url("http://localhost:8200/web/index.php/auth/login")
    assert context.login_page.get_login_page_text() == "Login"

@given('I am logged in as an Employee')
def step_impl(context):
    username_element = context.login_page.get_username_field()
    context.login_page.enter_text(username_element, "sh_holmes")
    password_element = context.login_page.get_pass_field()
    context.login_page.enter_text(password_element, "Im!Admin123OK")
    context.login_page.click_login_button()

@given('I am logged in as HR')
def step_impl(context):
    username_element = context.login_page.get_username_field()
    context.login_page.enter_text(username_element, "Admin")
    password_element = context.login_page.get_pass_field()
    context.login_page.enter_text(password_element, "Im!Admin123OK")
    context.login_page.click_login_button()

@when('I enter valid credentials')
def step_impl(context):
    username_element = context.login_page.get_username_field()
    context.login_page.enter_text(username_element, "Admin")
    password_element = context.login_page.get_pass_field()
    context.login_page.enter_text(password_element, "Im!Admin123OK")
    context.login_page.click_login_button()

@when('I enter invalid credentials')
def step_impl(context):
    username_element = context.login_page.get_username_field()
    context.login_page.enter_text(username_element, "dmin")
    password_element = context.login_page.get_pass_field()
    context.login_page.enter_text(password_element, "admin1234")
    context.login_page.click_login_button()

@then('I should be redirected to the dashboard')
def step_impl(context):
    message = context.login_page.get_header_text()
    print(message)
    assert "Dashboard" == message

@then('I should see an error message')
def step_impl(context):
    error_message = context.login_page.get_login_error_text()
    print(error_message)
    assert error_message == "Invalid credentials"
