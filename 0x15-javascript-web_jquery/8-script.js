$(document).ready(function () {
  $.getJSON('https://swapi-api.alx-tools.com/api/people/5/?format=json',
    function (data) {
      $.each(data, function () {
        $('UL#list_movies').append(<li>data.title</li>);
      });
    });
});
