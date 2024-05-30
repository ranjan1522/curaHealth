from behave import *
from features.commonUtility import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import allure


@when('Click on faclity which you want to choose "{healthcarefacility}"')
def choose_facility(context, healthcarefacility):
    try:
        explicit_wait_by_id(context, "combo_facility")
        facility_drop_down = Select(context.driver.find_element(By.ID, "combo_facility"))
        print("healthcarefacility: ", healthcarefacility)
        take_screenshot_and_attach(context, 'healthcarefacility')

        allure.attach.file('/path/to/image.png', name="my-image", attachment_type=allure.attachment_type.PNG)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

@when('Check on yes for hospital re-addmission')
def choose_readdmission(context):
        explicit_wait_by_id(context, "chk_hospotal_readmission")
        checkbox = context.driver.find_element(By.ID, "chk_hospotal_readmission")
        if not checkbox.is_selected():
            checkbox.click()

@when('Click on any health program "{HealthCareProgram}"')
def click_health_program(context, HealthCareProgram):
    try:
        id = "radio_program_{}".format(HealthCareProgram)
        print("Helath program: ", id)
        explicit_wait_by_id(context, id)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

@when('Choose the date to book and appointment "{Date}"')
def choose_date(context, Date):
    try:
        xpath = "//div[@class='datepicker-days']//td[contains(@class, 'day') and text()='{}']".format(Date)
        explicit_wait_by_css(context, "#appointment > div > div > form > div:nth-child(4) > div > div > div > span")
        select_date = context.driver.find_element(By.XPATH , xpath)
        select_date.click()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

@when('Wirte a comment as why need an appointment "{Comment}"')
def write_comment(context, Comment):
    explicit_wait_by_id(context, "txt_comment")
    comment_box = context.driver.find_element(By.ID, "txt_comment")
    comment_box.send_keys(Comment)

@when('Click on book appointment button')
def click_bookAppointment_button(context):
    explicit_wait_by_id(context, "btn-book-appointment")

@when('Verify the booked appointment url')
def confirmed_appointment_url(context):
    try:
        current_url = context.driver.current_url()
        assert current_url == "https://katalon-demo-cura.herokuapp.com/appointment.php#summary"

    except Exception as e:
        print(f"Url is not matched: {e} ")


@when('Verify booked appointment header')
def booked_appointment_header(context):
    try:
     verify_element_byXpath(context, "//*[@id='summary']/div/div/div[1]/h2", "Appointment Confirmation")
    except Exception as e:
        print(f"Booked appointment header error: {e}")


@when('Verify booked appointment sub header')
def booked_appointment_sub_header(context):
    try:
        verify_element_byXpath(context, "//*[@id='summary']/div/div/div[1]/p", "Please be informed that your appointment has been booked as following:")

    except Exception as e:
        print(f"Booked appointment sub header error: {e}")


@when('Verify Facility Name with input "{facility}"')
def facility_name(context, facility):
    try:
        verify_element_byID(context, "facility", facility)
    except Exception as e:
        print(f"Facility Name error: {e}")


@when('Verify - Apply for hospital readmission')
def hospital_readmission(context):
    try:
        verify_element_byID(context, "hospital_readmission", "YES")

    except Exception as e:
        print(f"Apply for hospital readmission error: {e}")


@when('Verify - Healthcare Program with input "{program}"')
def healthcare_program(context, program):
    try:
        modified_program = program.capitalize() # it will capitilize only first letter of the string
        verify_element_byID(context, "program", modified_program)

    except Exception as e:
        print(f"Healthcare Program error: {e}")


@when(u'Verify - Visit Date with input "{Date}"')
def visit_date(context, Date):
    try:
        print(Date)
        verify_element_byID(context, "visit_date", f"{Date}/05/0204")

    except Exception as e:
        print(f"Visit Date error: {e}")

@when(u'Verify - Read Comment with input "{comment}"')
def visit_date(context, comment):
    try:
        verify_element_byID(context, "comment", comment)

    except Exception as e:
        print(f"Read Comment: {e}")


@then(u'Click on Go to HomePage Button')
def homepage_button(context):
    try:
        explicit_wait_by_xpath(context, "//*[@id='summary']/div/div/div[7]/p/a")

    except Exception as e:
        print(f"Go to HomePage Button error: {e}")

