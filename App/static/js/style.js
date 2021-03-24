// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    $('#topBtn').css('display' ,'block');
  } else {
    $('#topBtn').css('display' ,'none');
  }
}

// When the user clicks on the button, scroll to the top of the document
$(document).ready(function() {
    $("#topBtn").click(function(event) {
        event.preventDefault();
        $("html, body").animate({ scrollTop: 0 }, "slow");
        return false;
    });
});