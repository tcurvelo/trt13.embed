*** Settings ***
Resource  plone/app/robotframework/selenium.robot
Library   Remote  ${PLONE_URL}/RobotRemote

Test Setup     Open test browser
Test Teardown  Close all browsers


*** Test Cases ***

Video Embarcado aparece como adicionável
    Given I'm logged in as a 'Site Administrator'
     When Open Add New Menu
     Then Element should be visible  trt13-portal-embedvideo-video

*** Keywords ***

I'm logged in as a '${ROLE}'
    Enable autologin as  ${ROLE}
    Go to  ${PLONE_URL}

Open Add New Menu
    Open menu  plone-contentmenu-factories

Open Menu
    [Arguments]  ${elementId}

    Element Should Not Be Visible  css=dl#${elementId} dd.actionMenuContent
    Click link  css=dl#${elementId} dt.actionMenuHeader a
    Wait until keyword succeeds  1  5  Element Should Be Visible  css=dl#${elementId} dd.actionMenuContent
