from behave import *


@Given('I am logged in my Jules account')
def step_impl(context):
    context.people_page.go_to('sign-in')
    context.login_page.input_email('georgianastefan1511@gmail.com')
    context.login_page.input_password('Test123test!')
    context.login_page.click_login_button()


@When('I select people option')
def step_impl(context):
    context.people_page.people_option()


@When('I type the firstname in search bar')
def step_impl(context):
    context.people_page.search_bar_input('Maria')


@Then('I see the results of the people I have on my account')
def step_impl(context):
    context.people_page.verify_user_from_list()


@Given('I am on people page')
def step_impl(context):
    context.people_page.go_to('people')


@When('I type the lastname in search bar')
def step_impl(context):
    context.people_page.search_bar_input('Stefan')


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
    context.people_page.verify_delete_message()
    context.people_page.close_alert()
