# pylint: disable=function-redefined, missing-function-docstring
# flake8: noqa
"""
Web Steps
Steps file for web interactions with Selenium
For information on Waiting until elements are present in the HTML see:
    https://selenium-python.readthedocs.io/waits.html
"""

from behave import given, when, then

@given('I am on the "Home Page"')
def step_impl(context):
    context.response = context.driver.get(f"{context.base_url}/pets")

# Still failing when run Behave 
@when('I set the "Category" to "dog"')
def step_impl(context):
    element = context.driver.find_element_by_id('pet_category')
    element.clear()
    element.send_keys('dog')


@when('I click the "Search" button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click the "Search" button')


@then('I should see the message "Success"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should see the message "Success"')


@then('I should see "Fido" in the results')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should see "Fido" in the results')


@then('I should not see "Kitty" in the results')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should not see "Kitty" in the results')


@then('I should not see "Leo" in the results')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should not see "Leo" in the results')
