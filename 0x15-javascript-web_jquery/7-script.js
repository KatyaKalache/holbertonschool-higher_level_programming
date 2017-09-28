$.get('https://swapi.co/api/people/5/?format=json', function(json){
  $('div').text(json['name']);
});
