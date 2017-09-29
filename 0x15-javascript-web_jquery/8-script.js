$.get('https://swapi.co/api/films/?format=json', function(data) {
  let movieList = data['results'];
  for (let i = 0; i < movieList.length; i++) {
    titles = movieList[i]['title'];
    $('#list_movies').append(titles + '<br/>');
    }
});
