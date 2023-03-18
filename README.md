# Jules-Project- 

Testing 3 main functionalities of the Jules web page: Login, People Search, Add Page using:

## Behaviour Driven Development
## Page Object Model
## Gerkin

### Prerequisites

We need a python library that implements the syntax Gherkin: [behave]

We also need selenium, webdriver-manager and a library for formatting reports [behave-html-formatter]

## In terminal(venv):
- pip install behave
- pip install selenium
- pip install webdriver-manager
- pip install behave-html-formatter

## The structure of Jules project:
...
/Features
login.feature
people.feature
test_add.feature
browser.py
environment.py
/Features/Pages
add_page.py
login_page.py
people_page.py
/Features/Steps
login.py
people.py
test_add.py
/behave.ini
...
# How to start the test with HTML report
## In terminal(venv):
behave -f html -o name_report.html
