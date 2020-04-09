*** Settings ***
Library  Selenium2Library

*** Variables ***

*** Keywords ***

*** Test Cases ***
1. open browser 'chorme'
    Open Browser  http://temis.nl/airpollution/no2col/no2regioomi_v2.php  chrome
2. Select Option Southeast Asia
    Select From List by Value    xpath=//select[@name="Region"]    6
3. Select Year
   Select From List by Value    xpath=//select[@name="Year"]    2019
4. Select Month
    Select From List by Value    xpath=//select[@name="Month"]    03
5. Select day
    Select From List by Value    xpath=//select[@name="Day"]    01
6. submit
    Click Element  (//input[@value="submit"])
7. wait
    Sleep    2s
8. Click Link
   Click Link   (//a[@href="data/omi/data_v2/2019/omi_no2_he5_20190301.tar"])
