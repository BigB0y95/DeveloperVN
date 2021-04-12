// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    $('#topBtn').css('display' ,'block');
  } else {
    $('#topBtn').css('display' ,'none');
  }
}

$(document).ready(function() {
    // When the user clicks on the button, scroll to the top of the document
    $("#topBtn").click(function(event) {
        event.preventDefault();
        $("html, body").animate({ scrollTop: 0 }, "slow");
        return false;
    }); 
});
$(document).ready(function() {
  var url = window.location.href;
  if(url.indexOf('trangchu') > -1){
      $('#about').removeClass('active');
      $('#course').removeClass('active');
      $('#contact').removeClass('active');
      $('#sponsorship').removeClass('active');
      $('#home').addClass('active');
  }
  else if(url.indexOf('gioithieu') > -1){
      $('#home').removeClass('active');
      $('#course').removeClass('active');
      $('#contact').removeClass('active');
      $('#sponsorship').removeClass('active');
      $('#share').removeClass('active');
      $('#about').addClass('active');
  }
  else if(url.indexOf('khoahoc') > -1){
      $('#home').removeClass('active');
      $('#about').removeClass('active');
      $('#contact').removeClass('active');
      $('#sponsorship').removeClass('active');
      $('#share').removeClass('active');
      $('#course').addClass('active');
  }
  else if(url.indexOf('lienhe') > -1){
    $('#home').removeClass('active');
    $('#about').removeClass('active');
    $('#course').removeClass('active');
    $('#sponsorship').removeClass('active');
    $('#share').removeClass('active');
    $('#contact').addClass('active');
  }
  else if(url.indexOf('taitro') > -1){
    $('#home').removeClass('active');
    $('#about').removeClass('active');
    $('#course').removeClass('active');
    $('#contact').removeClass('active');
    $('#share').removeClass('active');
    $('#sponsorship').addClass('active');
  }
  else if(url.indexOf('chiase') > -1){
    $('#home').removeClass('active');
    $('#about').removeClass('active');
    $('#course').removeClass('active');
    $('#contact').removeClass('active');
    $('#sponsorship').removeClass('active');
    $('#share').addClass('active');
  }
});
