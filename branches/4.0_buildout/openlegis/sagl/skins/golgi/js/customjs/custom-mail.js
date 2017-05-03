//mail page settings
'use strict'
$.fn.random = function () {
    return this.eq(Math.floor(Math.random() * this.length));//Get random mail
}
//append random mail function
function infinite() {
    $('.message-list').visibility({
        once: false,

        offset: 5, // Only works on Chrome with a healthy offset.
        // Value required seems to depend on how deeply
        // the DOM element is nested.

        // update size when new content loads
        observeChanges: true,

        // load content on bottom edge visible
        onBottomVisible: function () {
            var loadli = $(".message-list li").random();
            console.log("infiniateScroll ... called.");
            //alert("infiniateScroll ... called.");
            $(".message-list").append(loadli)
        }
    });
};
//append random mail function


//mail page load more button
$(".ui.button.loadmore").on("click", function () {
    infinite();
});
//mail page load more button

// using context
$('.ui.sidebar.mess')
  .sidebar({
      context: $('.message-list')
  }).sidebar('attach events', '.message-list li .col-2');