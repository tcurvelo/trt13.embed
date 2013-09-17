/**
 *  Adiciona eventos de click aos links dos videos alternativos,
 *  para atualização do player com ajax.
 */

$(function(){
    $("ul#trt13_portal_embed_alternatives li a").
        click(function(e){
            e.preventDefault();
            var that = $(this);

            $('#trt13_portal_embed_player').load(
                this.href + "?ajax_load=true #trt13_portal_embed_player object",
                function(){
                    $("ul#trt13_portal_embed_alternatives li.current").removeClass("current");
                    that.parent("li").addClass("current");
                }
            );
        });
});
