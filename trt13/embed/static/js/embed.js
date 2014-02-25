/**
 *  Adiciona eventos de click aos links dos conteudos embarcados
 *  alternativos, para atualização com ajax.
 */

$(function(){
    $("ul#trt13_embed_alternatives li a").
        click(function(e){
            e.preventDefault();
            var that = $(this);

            $('#trt13_embed').load(
                this.href + "?ajax_load=true #trt13_embed object",
                function(){
                    $("ul#trt13_embed_alternatives li.current").removeClass("current");
                    that.parent("li").addClass("current");
                }
            );
        });
});
