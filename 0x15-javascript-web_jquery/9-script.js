$(document).ready(function () {
  $.getJSON('https://hellosalut.stefanbohacek.dev/?lang=fr',
    function (data) {
      $('DIV#hello').text(data.hello);
    });
});
