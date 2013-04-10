from lettuce import *
from lettuce_webdriver.util import assert_false, assert_true
from lettuce_webdriver.util import AssertContextManager


@step(u'I should see class "(.*?)" of element "(.*?)" id "(.*?)"')
def check_element_by_chass(step, att_class, element, att_id):
	assert_true(step, world.browser.find_element_by_xpath('//%s[@id="%s"]/div[contains(@class, "%s")]' 
		% (element, att_id, att_class)))

@step('I should see the selector "([^"]*)" has css attribute "([^"]*)" value "([^"]*)"')
def check_css_value(step, att_selector, att_name, att_value):
	ppvalue = world.browser.find_element_by_css_selector("%s" % att_selector).value_of_css_property('%s' % att_name)
	assert ppvalue in att_value

@step('I have the following data for css selector "(.*?)"')
def check_search_box(step, css_selector):
	for searchbox_dict in step.hashes:
		world.browser.get(searchbox_dict['name'])
		check_css_value(step, css_selector, searchbox_dict['attribute_name'], searchbox_dict['attribute_value'])

def find_field_by_class(browser, attribute):
    xpath = "//input[@class='%s']" % attribute
    elems = browser.find_elements_by_xpath(xpath)
    return elems[0] if elems else False

@step('I fill in field with class "(.*?)" with "(.*?)"')
def fill_in_textfield_by_class(step, field_name, value):
    with AssertContextManager(step):
        text_field = find_field_by_class(world.browser, field_name)
        text_field.clear()
        text_field.send_keys(value)


@step('I have the number (\d+)')
def have_the_number(step, number):
    world.number = int(number)

@step('I compute its factorial')
def compute_its_factorial(step):
    world.number = factorial(world.number)

@step('I see the number (\d+)')
def check_number(step, expected):
    expected = int(expected)
    assert world.number == expected, \
        "Got %d" % world.number

def factorial(number):
    number = int(number)
    if (number == 0) or (number == 1):
        return 1
    else:
        return number