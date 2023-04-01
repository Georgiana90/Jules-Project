from time import sleep

from behave import *


@Given('I am on the login page')
def step_impl(context):
    context.login_page.go_to('sign-in')


@When('I insert "{username}" and "{password}"')
def step_impl(context, username, password):
    context.login_page.input_email(username)
    context.login_page.input_password(password)


@When('I click the login button')
def step_impl(context):
    context.login_page.click_login_button()


@Then('I cannot login to my account and see the "{error_msg}"')
def step_impl(context, error_msg):
    sleep(1)
    context.login_page.check_error_message(error_msg)


@When('I input a valid email and a valid password')
def step_impl(contex):
    contex.login_page.input_email('georgianabanciu1511@gmail.com')
    contex.login_page.input_password('Test123test!')


@Then('I see my Jules account')
def step_impl(context):
    sleep(5)
    context.login_page.pop_up()
    context.login_page.is_message_displayed()

