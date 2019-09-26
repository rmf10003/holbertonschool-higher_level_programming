$.getJSON('https://swapi.co/api/films/?format=json', function (data) {
  for (film of data['results']) {
    $('ul#list_movies').append($("<li></li>").text(film['title']))
  }
})
