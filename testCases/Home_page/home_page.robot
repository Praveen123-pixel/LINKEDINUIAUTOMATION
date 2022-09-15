*** Settings ***
Library     TestKeyword.test_home_page.Test_HOMEPAGE
Library     utilities.config.Test_Config
Test Setup     Launch the Application
Test Teardown  close the application
*** Test Cases ***
#TEST_CASE 01
Verify the home page UI of application
    Then launch the application and verify the tittle
    Then VERIFY THE OPTION START FREE TRIAL IS VISIBLE
    Then Verify try free option is visible
    Then verify the application scrolling feature top to bottom

Verify the main menu options on home screen
    Given verify the main menu options   leadersenger@gmail.com




