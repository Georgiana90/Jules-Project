from Pages.login_page import Login
from Pages.add_page import AddItem
from Pages.people_page import PeoplePage

from browser import Browser


def before_all(context):
    context.browser = Browser()
    context.login_page = Login(context.browser)
    context.people_page = PeoplePage(context.browser)
    context.add_page = AddItem(context.browser)


def after_all(context):
    context.browser.close()
