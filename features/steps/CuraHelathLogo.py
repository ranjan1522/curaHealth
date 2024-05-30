from behave import *
from selenium.webdriver.common.by import By

@given('Open the cura health application in browser tab')
def step_impl(context):
    context.driver.get("https://katalon-demo-cura.herokuapp.com/#appointment")

@when('Verify the website logo')
def step_impl(context):
    heading_present = context.driver.find_element(By.XPATH, "//*[@id='top']/div/h1")
    heading_text = heading_present.text
    assert heading_text == "CURA Healthcare Service"
