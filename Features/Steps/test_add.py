from time import sleep

from behave import *


@Given('I am on Jules Add page')
def step_impl(context):
    context.add_page.go_to('add')


@When('I select the option to add person')
def step_impl(context):
    context.add_page.click_add_person()


@When('I input firstname and lastname')
def step_impl(context):
    context.add_page.input_first_name('John')
    context.add_page.input_last_name('Doe')


@When('I click save button')
def step_impl(context):
    context.add_page.click_save_button()


@Then('I see the confirmation message')
def step_impl(context):
    sleep(2)
    context.add_page.check_add_message()
    context.add_page.click_finish_button()


@When('I type "{firstname}" and "{lastname}"')
def step_impl(context, firstname, lastname):
    context.add_page.input_first_name(firstname)
    context.add_page.input_last_name(lastname)


@Then('I see the "{error_message}"')
def step_impl(context, error_message):
    context.add_page.check_invalid_field(error_message)
