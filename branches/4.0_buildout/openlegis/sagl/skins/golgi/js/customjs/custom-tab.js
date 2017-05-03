//tab page ajax tab trigger
'use strict'
// A $( document ).ready() block.
$(document).ready(function () {
    $('.ajaxtab .item').tab({
    cache: false,
    // faking API request
    apiSettings: {
        loadingDuration: 300,
        mockResponse: function (settings) {
            var response = {
                first: '<h3 class="ui header">AJAX Tab One</h3><img class="ui wireframe image" src="img/bg/1.png">',
                second: '<h3 class="ui header">AJAX Tab Two</h3><img class="ui wireframe image" src="img/bg/2.png">',
                third: '<h3 class="ui header">AJAX Tab Three</h3><img class="ui wireframe image" src="img/bg/5.png">'
            };
            return response[settings.urlData.tab];
        }
    },
    context: 'parent',
    auto: true,
    path: '/'
});
});