# features/environment.py
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService

def before_scenario(context, scenario):
    service = FirefoxService(executable_path=r"Selenium_Drivers/geckodriver.exe")
    context.driver = webdriver.Firefox(service=service)
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)

def after_scenario(context, scenario):
    context.driver.quit()