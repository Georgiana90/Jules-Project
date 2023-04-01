from time import sleep

from behave import *


@Given('I am on people page')
def step_impl(context):
    context.people_page.go_to('people')


@When('I type "{name}" in search bar')
def step_impl(context, name):
    context.people_page.search_bar_input(name)


@Then('I see the "{results}" of the people I have on my account')
def step_impl(context, results):
    context.people_page.verify_user_from_list(results)


@When('I type a name in search bar')
def step_impl(context):
    context.people_page.search_bar_input('John Doe')


@When('I select the first option and click delete')
def step_impl(context):
    context.people_page.select_option()
    context.people_page.delete_option()
    context.people_page.accept_delete()


@Then('I see the successfully delete confirmation')
def step_impl(context):
    sleep(2)
    context.people_page.verify_delete_message()
    context.people_page.close_alert()
