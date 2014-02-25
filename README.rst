trt13.embed
************************************************************************

Provê o tipo de conteúdo **Conteúdo Embacardo** para o Plone, que
permite incluir *streams*, *applets*, animações e outros conteúdos
através das tags ``<object />`` ou ``<embed />``.
Os itens a serem embarcados pode ser externos ao site (ex: um *stream*
via ``mms://``) ou internos (ex: arquivo ``.swf``).
Adicionalmente, um *Conteúdo Embacardo* pode conter "versões
alternativas" (ex: qualidade alta, baixa, câmera #2, apenas áudio, etc.)
representada por outra instância do tipo, com parâmetros diferentes.


Instalação e configuração
=========================

Para instalar, basta incluir o pacote no buildout do Plone::

    [buildout]
    ...
    eggs +=
        trt13.embed
    ...
    [sources]
    trt13.embed = git https://github.com/tcurvelo/trt13.embed.git


Utilização
==========

* Adicione um **Conteúdo Embacardo** normalmente, através do menu
  *Adicionar Item*

* Informe título, Descrição, URL, Altura, Largura e mimetype do
  conteúdo que você deseja embarcar.

* Dentro de um item é possível adicionar outros como ele: como "versões
  alternativas". Na criação do item interno, as propriedades do item
  superior serão sugeridas como valores padrão, mas é permitido
  variá-las (ex: mudar a URL).

  * Na visualização de um **Conteúdo Embarcado** as alternativas serão
    apresentados links, e seus dados carregados via javascript.

* É possível também adicionar arquivos dentro de um conteúdo embarcado
  e referênciá-lo na propriedade URL deste (pode-se usar endereço
  relativo).
