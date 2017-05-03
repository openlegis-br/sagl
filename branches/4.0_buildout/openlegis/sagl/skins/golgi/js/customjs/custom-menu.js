//Nav menu Settings
'use strict'
menu = {};

// ready event
menu.ready = function () {
    // selector cache
    var
      $menuItem = $('.menu a.item, .menu .link.item'),
      // alias
      handler = {
          activate: function () {
              $(this)
              .addClass('active')
              .closest('.ui.menu')
              .find('.item')
              .not($(this))
              .removeClass('active');
          }
      }
    ;

    $menuItem
      .on('click', handler.activate)
    ;
};

// attach ready event
$(document).ready(menu.ready);

//tooltip menu trigger on click
$(".ui.menu .ppmenu").popup({
    on: "click"
});
//tooltip menu trigger on click


$(function () {
    $(".ui.dropdown").dropdown();//dropdown triggers
    $(".ui.button").popup({ inline: true });//tooltip triggers
});