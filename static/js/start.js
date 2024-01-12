// 페이지 실행 후 1초 뒤 메시지 바뀌기
setTimeout(function() {
    document.querySelector('.eng').style.opacity = '0';
    document.querySelector('.ko').style.opacity = '1';
  }, 1000); 

  // 스크롤 동작 하면 네비바 나타나기
  $(document).ready(function() {
      var $html = $("html, body");
      var page = 0;
      var lastPage = $("section").length - 1;
  
      $(window).on("wheel", function(e) {
          if ($html.is(":animated")) return;
  
          if (e.originalEvent.deltaY > 0) {
              if (page == lastPage) return;
              page++;
          } else if (e.originalEvent.deltaY < 0) {
              if (page == 0) return;
              page--;
          }
  
          var posTop = page * $(window).height();
  
          $html.animate({ scrollTop: posTop }, 800);
      });
  });
