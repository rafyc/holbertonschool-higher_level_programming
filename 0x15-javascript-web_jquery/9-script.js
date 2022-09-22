#!/usr/local/bin/node
$(document).ready(() => {
  $.get('https://stefanbohacek.com/hellosalut/?lang=fr', (obj) => {
    $('DIV#hello').text(obj.hello);
  });
});
