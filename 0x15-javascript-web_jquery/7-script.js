#!/usr/local/bin/node
$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', (obj) => {
  $('DIV#character').text(obj.name);
});
