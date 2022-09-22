#!/usr/local/bin/node
$.get('https://swapi-api.hbtn.io/api/films/?format=json', (obj) => {
  $.each(obj.results, (key, val) => {
    $('UL#list_movies').append(`<li>${val.title}</li>`);
  });
});
