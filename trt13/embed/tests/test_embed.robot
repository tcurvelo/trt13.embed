*** Settings ***
Resource  plone/app/robotframework/selenium.robot
Library   Remote  ${PLONE_URL}/RobotRemote
Variables  trt13/embed/tests/variables.py

Test Setup     Open test browser
Test Teardown  Close all browsers


*** Test Cases ***

Conteudo Embarcado aparece como adicionável
    I'm logged in as a 'Site Administrator'
    Open Add New Menu
    Element should be visible  trt13-embed


Checa os campos do formulário de Conteudo Embarcado
    Abre formulário de criação de conteudo embarcado
    Page should contain  Title
    Page should contain  Summary
    Page should contain  Height
    Page should contain  Width
    Page should contain  URL
    Page should contain  Mimetype
    Page should contain  Parameters
    Page should contain  Lead Image Caption
    Element should be visible  css=#formfield-form-widgets-width>label>span.required
    Element should be visible  css=#formfield-form-widgets-height>label>span.required
    Element should be visible  css=#formfield-form-widgets-url>label>span.required
    Element should be visible  css=#formfield-form-widgets-mimetype>label>span.required


Conteudo Embarcado e Arquivo aparecem como adicionáveis em um embarcado
    Criei um conteudo embarcado 'Video'
    Open Add New Menu
    Page should contain link  link=File
    Page should contain link  link=Conteudo Embarcado
    Page should not contain link  link=Page


É mostrado uma miniatura numa listagem contendo um Embarcado
    Criei um conteudo embarcado 'Video'
    Click link  link=Edit
    Choose File  id=form-widgets-ILeadImage-image-input  ${PKG_ROOT}/static/img/embed.png
    Click Button  Save
    Page Should Contain  Changes saved
    Go to  ${PLONE_URL}/selectViewTemplate?templateId=summary_view
    Page should contain image  css=img[alt=Video]


*** Keywords ***

Criei um conteudo embarcado '${Title}'
    Abre formulário de criação de conteudo embarcado
    Input Text  form-widgets-IBasic-title  ${Title}
    Input Text  form-widgets-IBasic-description  Descricao de ${Title}
    Input Text  form.widgets.height  480
    Input Text  form.widgets.width  640
    Input Text  form.widgets.url  meu_video.flv
    Input Text  form.widgets.mimetype  video/x-flv
    Click Button  Save
    Page Should Contain  Item created

Abre formulário de criação de conteudo embarcado
    I'm logged in as a 'Site Administrator'
    Open Add New Menu
    Click link  link=Conteudo Embarcado

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
