/**
 *  Adiciona eventos de click aos links dos videos alternativos,
 *  para atualização do player com ajax.
 */

$(function(){
    $("ul#trt13_portal_embedvideo_alternatives li a").
        click(function(e){
            e.preventDefault();
            var that = $(this);

            $('#trt13_portal_embedvideo_player').load(
                this.href + "?ajax_load=true #trt13_portal_embedvideo_player object",
                function(){
                    $("ul#trt13_portal_embedvideo_alternatives li a.current").
                        button("enable").removeClass("current");
                    that.button("disable").addClass("current");;
                }
            );

        }).
        button().
        filter(".current").button("disable");
});
