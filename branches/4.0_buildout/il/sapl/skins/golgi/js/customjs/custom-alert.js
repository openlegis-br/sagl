//alert page triggers
'use strict'
$(".swtalrt").on("click", function () {
    var a = $(this).attr("data-type");
    swal({
        title: "Are you sure?",
        text: "You will not be able to recover this imaginary file!",
        type: a,
        showCancelButton: true,
        confirmButtonColor: "#DD6B55",
        confirmButtonText: "Yes, delete it!",
        cancelButtonText: "No, cancel plx!",
        closeOnConfirm: false,
        closeOnCancel: false
    }, function (a) {
        if (a) swal("Deleted!", "Your imaginary file has been deleted.", "success"); else swal("Cancelled", "Your imaginary file is safe :)", "error");
    });
});

$(".swtalrt1").on("click", function () {
    swal("I Love Semantic!");
});
$(".swtalrt2").on("click", function () {
    swal("I Love Semantic!", "It's pretty, isn't it?")
});
$(".swtalrt3").on("click", function () {
    swal("Good job!", "You clicked the button!", "success")
});
$(".swtalrt4").on("click", function () {
    swal({ title: "Are you sure?", text: "You will not be able to recover this imaginary file!", type: "warning", showCancelButton: true, confirmButtonColor: "#DD6B55", confirmButtonText: "Yes, delete it!", closeOnConfirm: false }, function () { swal("Deleted!", "Your imaginary file has been deleted.", "success"); });
});
$(".swtalrt5").on("click", function () {
    swal({ title: "Sweet!", text: "Here's a custom image.", imageUrl: "img/avatar/animals/panda_128px.png" });
});
$(".swtalrt6").on("click", function () {
    swal({ title: 'HTML <small>Title</small>!', text: 'A custom <span style="color:#F8BB86">html<span> message.', html: true });
});
$(".swtalrt7").on("click", function () {
    swal({ title: "Auto close alert!", text: "I will close in 2 seconds.", timer: 2000, showConfirmButton: false });
});
$(".swtalrt8").on("click", function () {
    swal({ title: "An input!", text: "Write something interesting:", type: "input", showCancelButton: true, closeOnConfirm: false, animation: "slide-from-top", inputPlaceholder: "Write something" }, function (inputValue) { if (inputValue === false) return false; if (inputValue === "") { swal.showInputError("You need to write something!"); return false } swal("Nice!", "You wrote: " + inputValue, "success"); });
});
$(".swtalrt9").on("click", function () {
    swal({ title: "Ajax request example", text: "Submit to run ajax request", type: "info", showCancelButton: true, closeOnConfirm: false, showLoaderOnConfirm: true, }, function () { setTimeout(function () { swal("Ajax request finished!"); }, 2000); });
});