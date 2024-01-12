// 미쿼 네비바

$(".mNav").click(function(){
    $(".nav_menu").animate({width:"toggle"}, 400);
});

$(window).resize(function(){
    let wWidth = $(window).width();
    if(wWidth>400){
        $(".nav_menu").removeAttr("style");
    }
});