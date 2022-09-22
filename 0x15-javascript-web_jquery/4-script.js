#!/usr/local/bin/node
$('DIV#toggle_header').click(() => {
  $('header').toggleClass('green red');
});
