Feature: To Book an appointment for checkup


  @allure.label.owner:Prabhat
  @allure.link:https://katalon-demo-cura.herokuapp.com/#appointment
  @allure.issue:UI-1
  @allure.tms:TMS-456
  Scenario Outline: Booking an appointment for checkup with multiple parameters
    Given Open the cura health application in browser tab
    When Click on appointment button
    And Verify the appointment webpage url
    And Enter the username with "John Doe"
    And Enter the password with "ThisIsNotAPassword"
    And Click on login button
    And Click on faclity which you want to choose "<Facility>"
    And Check on yes for hospital re-addmission
    And Click on any health program "<HealthCareProgram>"
    And Choose the date to book and appointment "<Date>"
    And Wirte a comment as why need an appointment "<Comment>"
    And Click on book appointment button
    And Verify the booked appointment url
    And Verify booked appointment header
    And Verify booked appointment sub header
    And Verify Facility Name with input "<Facility>"
    And Verify - Apply for hospital readmission
    And Verify - Healthcare Program with input "<HealthCareProgram>"
    And Verify - Visit Date with input "<Date>"
    And Verify - Read Comment with input "<Comment>"
    Then Click on Go to HomePage Button

    Examples:
      | Facility | HealthCareProgram |  Date  | Comment |
      | Tokyo CURA Healthcare Center | medicaid | 22  | Diabetes Checkup |
      | Hongkong CURA Healthcare Center | medicare | 23  | High Blood Pressure Checkup |
      | Seoul CURA Healthcare Center | none | 24  | Low Blodd Pressure Checkup |

