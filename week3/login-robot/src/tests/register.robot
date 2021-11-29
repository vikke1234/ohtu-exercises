*** Settings ***
Resource  resource.robot

*** Test Cases ***
Register With Valid Username And Password
    Create New User  test  test1234
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Create New User  test  test1234
    Create New User  test  test1234
    Output Should Contain  User with username test already exists

Register With Too Short Username And Valid Password
    Create New User  a  a2345678
    Output Should Contain  Username is too short

Register With Valid Username And Too Short Password
    Create New User  aaaa  b
    Output Should Contain  Password should be longer than 8 characters

*** Keywords ***
Create New User
    [Arguments]  ${username}  ${password}
    Input New Command
    Input Credentials  ${username}  ${password}
