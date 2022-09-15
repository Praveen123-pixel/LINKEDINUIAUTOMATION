*** Settings ***
Library     utilities.config.Test_Config
Library     TestKeyword.login_page.Login_page
#Library     DataDriver  ..RobotframeworkUiAutomation/TestKeyword/TestData.csv
Test Setup     Launch the Application
#Test Template  Try to login application by invalid creaddentail
Test Teardown  close the application
*** Variables ***
${USER_NAME1} =  leadersenger@gmail.com
${PASS_WORD1} =  Praveen@123



*** Test Cases ***
Verify and login feature of app by right username and right password
   # ${USER_NAME1}    ${PASS_WORD1}
    When enter the username on username place holder   ${USER_NAME1}
    And enter the password on password place holder    ${PASS_WORD1}
    Then verify the home page of application
    Then click on sign in button
    Then verify the app is scrolling top to bottom to top



Verify and login feature with invalid credeantials

     Try to login application by invalid creaddentail     wfwefwefg     fwegwergergerg
     Then verify the home page of application


*** Keywords ***
Try to login application by invalid creaddentail
    [Arguments]                                  ${USER_NAME}           ${PASS_WORD}
    enter the username on username place holder   ${USER_NAME}
    enter the password on password place holder    ${PASS_WORD}
    click on sign in button


