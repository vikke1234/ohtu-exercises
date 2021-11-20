*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Register User  validuser  validpass1  validpass1
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Register User  a  bbbb1234  bbbb1234
    Registration Should Fail With Message  Username should be longer than 3 characters and only contain a-z

Register With Valid Username And Too Short Password
    Register User  aaaa  b  b
    Registration Should Fail With Message  Password should be longer than 8 characters and contain both letters and numbers

Register With Nonmatching Password And Password Confirmation
    Register User  aaaa  aoeu1234  ueao1234
    Registration Should Fail With Message  Passwords do not match

Login After Register
    Register User  aaaa  validpass1  validpass1
    Go To Login Page
    Set Username  aaaa
    Set Password  validpass1
    Click Button  Login
    Main Page Should Be Open

Login After Failed Register
    Register User  aaaa  notvalidpass  notvalidpass
    Go To Login Page
    Set Username  aaaa
    Set Password  notvalidpass
    Click Button  Login
    Login Page Should Be Open
    Page should Contain  Invalid username or password

*** Keywords ***
Register User
    [Arguments]  ${username}  ${password}  ${confirm_pass}
    Set Username  ${username}
    Set Password And Confirm  ${password}  ${confirm_pass}

Set Password And Confirm
    [Arguments]  ${password}  ${confirm_pass}
    Set Password  ${password}
    Set Confirm Password  ${confirm_pass}
    Confirm Credentials

Set Confirm Password
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Confirm Credentials
    Click Button  Register

Registration Should Succeed
    Welcome Page Should Be Open

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}
