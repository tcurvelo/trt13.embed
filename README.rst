trt13.portal.embedvideo
=======================

Provê conteúdo para vídeos embarcados (ex: mms://)

.. contents:: Sumário
   :depth: 2


Instalação e configuração
=========================

Para instalação, basta incluir o pacote no buildout do Plone::

    [buildout]
    ...
    eggs +=
        trt13.portal.embedvideo


Funcionalidades
===============

Em breve...


BUG's conhecidos
================

...


TODO
====
v0.1
 ✔ Criar conteudo Video Embarcado @done (13-05-14 19:37)
     ✔ Propriedades: title, description, width, height, mimetype, url @done (13-05-14 19:38)
 ✔ Criar template básico para Vídeo Embarcado @done (13-05-14 19:41)
 ✔ Um video pode conter videos alternativos dentro dele @done (13-05-15 11:01)
 ☐ Os videos alternativos devem sobrescrever propriedades de seus pais e herdas as demais
 ☐ O template do video permite mudar a visão para alguma dos alternativos
 ☐ Carregar alternativos via ajax

v0.2
 ☐ Como tornar parametros obrigatorios apenas se ão houver um video pai?
 ☐ Separa `URL` em `URL` e `parametros`
 ☐ O que são as propriedades `pluginspage` e `designtimesp` de embed. São importantes?
