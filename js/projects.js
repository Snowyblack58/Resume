define([
    'jquery'
], function($){
    $(document).ready(function(){
        initProjectLinks();
        initProjectMouseListeners();
    })

    function initProjectLinks(){
        $('.project-card').click(function(event){
            var link = $(this).parent().attr('data-href');
            window.open(link, '_blank');
        });
    }

    function initProjectMouseListeners(){
        $('.project-card').mouseenter(function(){
            $(this).find('img').stop(true).animate({
                'max-width': '90%',
                'max-height': '90%'
            }, 200);
        })
        $('.project-card').mouseleave(function(){
            $(this).find('img').animate({
                'max-width': '80%',
                'max-height': '80%'
            }, 200);
        })
    }
})
