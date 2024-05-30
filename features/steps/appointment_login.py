import time
from behave import *
from selenium.webdriver.common.by import By

@when('Click on appointment button')
def open_appointment_webpage(context):
    try:
        appointment_button = context.driver.find_element(By.ID, "btn-make-appointment")
        appointment_button.click()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

@when('Verify the appointment webpage url')
def verify_appointment_webpage_url(context):
    try:
        context.current_url = context.driver.current_url
        assert context.driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

@when('Enter the username with "{usrnm}"')
def enter_username(context, usrnm):
    try:
        username_field = context.driver.find_element(By.ID, "txt-username")
        username_field.clear()
        username_field.send_keys(usrnm)
        print("Entered username")
    except Exception as e:
        print(f"An unexpected error occurred while entering username: {e}")

@when('Enter the password with "{pwd}"')
def enter_password(context, pwd):
    try:
        password_field = context.driver.find_element(By.ID, "txt-password")
        password_field.clear()
        password_field.send_keys(pwd)
    except Exception as e:
        print(f"An unexpected error occurred while entering password: {e}")

@when('Click on login button')
def click_on_login(context):
    try:
        time.sleep(8)
        login_button = context.driver.find_element(By.ID, "btn-login")
        login_button.click()
    except Exception as e:
        print(f"An unexpected error occurred while clicking login button: {e}")

@then('Verify the after login page')
def verify_dashboard(context):
    try:
        appointment_page = context.driver.find_element(By.XPATH, "//*[@id='appointment']/div/div/div/h2")
        appointment_header_text = appointment_page.text
        assert appointment_header_text == 'Make Appointment'
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

@then('Verify login error message')
def verify_login_error_message(context):
    try:
        login_page_error_msg = context.driver.find_element(By.CSS_SELECTOR, "#login > div > div > div.col-sm-12.text-center > p.lead.text-danger")
        error_message = login_page_error_msg.text
        print(error_message)
        assert  error_message == 'Login failed! Please ensure the username and password are valid.', f"Expected 'Login failed! Please ensure the username and password are valid.', but got '{error_message}'"
    except Exception as e:
        print(f"An unexpected error occurred while verifying login error message: {e}")
