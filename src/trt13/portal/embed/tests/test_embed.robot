*** Settings ***
Resource  plone/app/robotframework/selenium.robot
Library   Remote  ${PLONE_URL}/RobotRemote

Test Setup     Open test browser
Test Teardown  Close all browsers


*** Test Cases ***

Conteudo Embarcado aparece como adicionável
    I'm logged in as a 'Site Administrator'
    Open Add New Menu
    Element should be visible  trt13-portal-embed-embed


Checa os campos do formulário de Conteudo Embarcado
    Abre formulário de criação de conteudo embarcado
    Page should contain  Title
    Page should contain  Description
    Page should contain  Height
    Page should contain  Width
    Page should contain  URL
    Page should contain  Mimetype
    Page should contain  Please upload an image
    Page should contain  Please inform a caption for the image
    Element should be visible  css=#formfield-form-widgets-width>label>span.required
    Element should be visible  css=#formfield-form-widgets-height>label>span.required
    Element should be visible  css=#formfield-form-widgets-url>label>span.required
    Element should be visible  css=#formfield-form-widgets-mimetype>label>span.required


Conteudo Embarcado e Arquivo aparecem como adicionáveis em um embarcado
    Criei um video embarcado
    Open Add New Menu
    Page should contain link  link=File
    Page should contain link  link=Conteudo Embarcado
    Page should not contain link  link=Page


#É mostrado um thumbnail numa listagem contendo um Embarcado


#Conteudo Embarcado alternativo é carregado via ajax


*** Keywords ***

Abre formulário de criação de conteudo embarcado
    I'm logged in as a 'Site Administrator'
    Open Add New Menu
    Click link  trt13-portal-embed-embed

Criei um video embarcado
    I'm logged in as a 'Site Administrator'
    Open Add New Menu
    Click link  link=Conteudo Embarcado
    Input Text  form-widgets-IBasic-title  Video
    Input Text  form-widgets-IBasic-description  Um video
    Input Text  form.widgets.height  480
    Input Text  form.widgets.width  640
    Input Text  form.widgets.url  meu_video.flv
    Input Text  form.widgets.mimetype  video/x-flv
    Click Button  Save
    Page Should Contain  Item created


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
