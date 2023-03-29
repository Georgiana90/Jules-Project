from time import sleep

from behave import *


@Given('I am on Jules Add page')
def step_impl(context):
    context.add_page.go_to('sign-in')
    context.add_page.select_add()


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
    sleep(3)
    context.add_page.check_add_message()


@When('I input numbers in firstname and lastname')
def step_impl(context):
    context.add_page.input_first_name('1234')
    context.add_page.input_last_name('56789')


@Then('I see the error message')
def step_impl(context):
    context.add_page.check_invalid_field()
