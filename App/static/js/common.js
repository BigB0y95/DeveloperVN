// permanent navbar
jQuery(document).ready(function($) {
    $(window).load(function() {
        if ($('.navbar').length > 0) {
            var _top = $('.navbar').offset().top - parseFloat($('.navbar').css('marginTop').replace(/auto/, 0));
            $(window).scroll(function(evt) {
                var _y = $(this).scrollTop();
                if (_y > _top) {
                    $('.navbar').addClass('fixed');
                    $('.main-1').css("margin-top", "30px")
                } else {
                    $('.navbar').removeClass('fixed');
                    $('.main-1').css("margin-top", "0")
                }
            })
        }
    });
});