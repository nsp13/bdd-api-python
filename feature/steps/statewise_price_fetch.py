# Python Behave testing example for Selenium test automation
import time
import requests
import config_file_reader
import header_initialisation
from behave import given, when, then
headers = header_initialisation.price_fetch_headers
url = config_file_reader.price_fetch_url
r = requests.get('https://www.google.com')


@given('Create the header & url based on appointment id')
def step(context):
    global headers
    global url
    print("In the fn Create the header & url based on appointment id")
    #url = 'https://listing-service-au.c24.tech/v1/vehicle/pricing/6111223748'


@when('Perform the get call on price fetch api')
def enter_item_name(context):
    global r
    global headers
    global url
    print("In the fn Perform the get call on price fetch api")
    r = requests.get(url, data=None, headers=headers)


@then('Validate the status code & price')
def see_login_message(context):
    global r
    print("In the fn Validate the status code & price")
    print("API response time is: ", r.elapsed.total_seconds())
    print(r.json())
    assert r.status_code == 200, "Response code is not 200"
    assert r.json()[0]['egc'] == r.json()[1]['egc'] == r.json()[2]['egc'], "EGC value is different in all the states"


