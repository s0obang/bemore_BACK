$(document).ready(function () {
    $("#apply, #apply_").on('click touchstart','#apply, #apply_', function (e){
        var notDate = $('[data-not-date]').data('not-date');
        if (notDate){
            e.preventDefault();
            alert('합격자 조회 기간이 아닙니다');     
        }
    });
});

