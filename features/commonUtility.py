from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
import os
def explicit_wait_by_id(context, locator):
    element_locator = (By.ID, locator)
    element_locator_wait = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable(element_locator))
    element_locator_wait.click()

def explicit_wait_by_xpath(context, locator):
    element_locator = (By.XPATH, locator)
    element_locator_wait = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable(element_locator))
    element_locator_wait.click()

def explicit_wait_by_css(context, locator):
    element_locator = (By.CSS_SELECTOR, locator)
    element_locator_wait = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable(element_locator))
    element_locator_wait.click()

def verify_element_byID(context, locator, exptected_text):
    element_locator = (By.ID, locator)
    element_locator_wait = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable(element_locator))
    element_locator_fetched_text = element_locator_wait.text
    assert  element_locator_fetched_text == exptected_text
    print("Expected Elemeted: ", element_locator_fetched_text)
    print("*"*20)
    print(f"Acutual: {element_locator_fetched_text} and Expected: {exptected_text} are matched sucessfully")
    print("*" * 20)

def verify_element_byCSS(context, locator, exptected_text):
    element_locator = (By.CSS_SELECTOR, locator)
    element_locator_wait = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable(element_locator))
    element_locator_fetched_text = element_locator_wait.text
    assert  element_locator_fetched_text == exptected_text
    print("*" * 20)
    print(f"Acutual: {element_locator_fetched_text} and Expected: {exptected_text} are matched sucessfully")
    print("*" * 20)

def verify_element_byXpath(context, locator, exptected_text):
    element_locator = (By.XPATH, locator)
    element_locator_wait = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable(element_locator))
    element_locator_fetched_text = element_locator_wait.text
    assert  element_locator_fetched_text == exptected_text
    print("*" * 20)
    print(f"Acutual: {element_locator_fetched_text} and Expected: {exptected_text} are matched sucessfully")
    print("*" * 20)


def take_screenshot(driver, name):
    screenshot_dir = os.path.join(os.getcwd(), "screenshots")
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)

    screenshot_path = os.path.join(screenshot_dir, f"{name}.png")
    driver.save_screenshot(screenshot_path)
    return screenshot_path

def take_screenshot_and_attach(context, name):
    screenshot_path = take_screenshot(context.driver, name)
    allure.attach.file(screenshot_path, name=name, attachment_type=allure.attachment_type.PNG)
