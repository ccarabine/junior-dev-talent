/*global bootstrap:false*/
/*jshint esversion:6*/

// Message variables
const messages = document.getElementById('msg');
const alert = new bootstrap.Alert(messages);

// vote variables

if (messages)
  setTimeout(function () {
    alert.close();
  }, 5500);


$('.toast').toast('show');
