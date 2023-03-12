from time import sleep

from behave import *


@Given('I am on the login page')
def step_impl(context):
    context.login_page.go_to('sign-in')


@When('I input a valid email and a valid password')
def step_impl(contex):
    contex.login_page.input_email('georgianastefan1511@gmail.com')
    contex.login_page.input_password('Test123test!')


@When('I click the login button')
def step_impl(context):
    context.login_page.click_login_button()


@Then('I see my account')
def step_impl(context):
    assert context.login_page.is_message_displayed() == 'The Banciu Household'



@When('I click my account options')
def step_impl(context):
    context.login_page.pop_up()
    context.login_page.user_options()


@When('I select logout')
def step_impl(context):
    context.login_page.log_out()
    context.login_page.log_out_accept()


@Then('I see the login page')
def step_impl(context):
    assert context.login_page.get_current_url() == 'https://jules.app/sign-in'


@Given('I am on my account page')
def step_impl(context):
    context.login_page.get_current_url()


@When('I input invalid email and valid password')
def step_impl(context):
    context.login_page.input_email('georgianastefan@gmail.com')
    context.login_page.input_password('Test123test!')


@Then('I am still on the sign-in page')
def step_impl(context):
    assert context.login_page.get_current_url() == 'https://jules.app/sign-in'


@When('I input valid email with invalid password')
def step_impl(context):
    context.login_page.input_email('georgianastefan1511@gmail.com')
    context.login_page.input_password('TestTest')


@When('I input invalid credentials')
def step_impl(context):
    context.login_page.input_email('georgianastefan@gmail.com')
    context.login_page.input_password('TestTest')
