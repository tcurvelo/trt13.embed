trt13.portal.embedvideo
*********************************************************************

Provê tipo de conteúdo para incluir Vídeos Embarcados (ex: mms://)
em um site Plone. Um vídeo pode conter alternativas (ex: qualidade alta, baixa,
camera 02, apenas audio, etc) representada por parâmetros diferentes.

.. contents:: Sumário
   :depth: 2


Instalação e configuração
===================

Para instalar, basta incluir o pacote no buildout do Plone::

    [buildout]
    ...
    eggs +=
        trt13.portal.embedvideo


Funcionalidades
===================

Em breve...


TODO
===================
v0.1

 ✔ Criar conteudo Video Embarcado @done (13-05-14 19:37)
     ✔ Propriedades: title, description, width, height, mimetype, url @done (13-05-14 19:38)

 ✔ Criar template básico para Vídeo Embarcado @done (13-05-14 19:41)

 ✔ Um video pode conter videos alternativos dentro dele @done (13-05-15 11:01)

 ✔ Os videos alternativos devem pegar a propriedades de seus pais e permitir sobrescrita @done (13-05-16 16:08)
     ✔ Utiliza `default_value` sugerir  valores dos pais na criação @done (13-05-16 16:08)

 ✔ O template do video lista os videos alternativos e os linka @done (13-05-20 10:52)

 ☐ Carregar alternativos via ajax

 ☐ Deixar a visao **apresentável** (aka. bells & whistles™)


v0.2

 ☐ Como tornar parametros obrigatorios apenas se não houver um video pai?

 ☐ Utilizar Aquisição ao invés de `default_value` (eg. implementar __getattr__ em Video)

 ☐ Separa `URL` em `URL` e `parametros`

 ☐ O que são as propriedades `pluginspage` e `designtimesp` de embed. São importantes?

