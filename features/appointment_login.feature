Feature: For appointment, requires login

  Scenario: For appointment login is required
    Given Open the cura health application in browser tab
    When  Click on appointment button
    And Verify the appointment webpage url
    And Enter the username with "John Doe"
    And Enter the password with "ThisIsNotAPassword"
    And Click on login button
    Then Verify the after login page

  Scenario Outline: For appointment login check with multisets of datas
    Given Open the cura health application in browser tab
    When  Click on appointment button
    And Enter the username with "<username>"
    And Enter the password with "<password>"
    And Click on login button
    Then Verify login error message

    Examples:
      | username | password |
      |  Joh | ThisIsNotAPassword |
      | John Doe | Password |
      | 12345 | NotInter |