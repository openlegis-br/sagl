//sidebar page sidebar trigger
//$('sidebar selector').first().sidebar('attach events', 'button selector', 'event name');
'use strict'
$('.sidebar1').first().sidebar('attach events', '.lefticon', 'show');
$('.sidebar2').first().sidebar('attach events', '.rightsidebar', 'show');
$('.sidebar3').first().sidebar('attach events', '.leftnormal', 'show');
$('.sidebar4').first().sidebar('attach events', '.topbsidebar', 'show');
$('.sidebar5').first().sidebar('attach events', '.sidebar5', 'show');

$('.sidebar2').first().sidebar('attach events', '.sidebar2', 'show');
$('.sizedsidebar1').first().sidebar('attach events', '.verythinsidebar', 'show');
$('.sizedsidebar2').first().sidebar('attach events', '.thinsidebar', 'show');
$('.sizedsidebar3').first().sidebar('attach events', '.normalsidebar', 'show');
$('.sizedsidebar4').first().sidebar('attach events', '.widesidebar', 'show');
$('.sizedsidebar5').first().sidebar('attach events', '.verywidesidebar', 'show');