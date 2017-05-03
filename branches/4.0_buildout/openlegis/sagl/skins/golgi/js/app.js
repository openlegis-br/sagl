'use strict'

$(document).ready(function () {
    loadhtml();
    paceLoading();
    butonactions();
    hamburger();
    tabactions();
    progressactions();
    formelementactions();
    messageclosebuttonactions()
    notifyactions();
    cardhoveractions();
    colorize();
    $(".ui.accordion").accordion();//accordion trigger
    $(".ui.rating").rating();//rating trigger
    $(".ui.dropdown").dropdown();//dropdown and select trigger

    //sidebar trigger
    $("#toc").sidebar({
        dimPage: true,
        transition: "overlay",
        mobileTransition: "uncover"
    });
    //sidebar trigger

    $("body").niceScroll({ cursorcolor: "#ddd", cursorwidth: 5, cursorborderradius: 0, cursorborder: 0, scrollspeed: 50, autohidemode: true, zindex: 9999999 });//body scroll tigger by nicescroll
    
});

//Sidebar Menu Size Animaton Function
function hamburger() {
    $(".hamburger").on("click", function () {
        if ("show" == $(this).data("name")) {
            $(".toc").animate({
                width: "100px"
            }, 350);
            $(".logo").animate({
                width: "100px"
            }, 350);
            $(".logo img").transition("scale").attr("src", "img/thumblogo.png");
            if (window.location.href.indexOf("mail.html") > -1) {
                $(".toc").load("html/loadthinmailmenu.html", function () {
                    $(".ui .dropdown").dropdown({
                        transition: "fade up",
                        on: "hover"
                    });

                    $(".logoImg").transition('jiggle')
                });
            }
            else {
                $(".toc").load("html/loadthinmenu.html", function () {
                    $(".ui .dropdown").dropdown({
                        transition: "fade up",
                        on: "hover"
                    });

                    $(".logoImg").transition('jiggle')
                });
            }

            $(this).data("name", "hide");
        } else {
            $(".toc").animate({
                width: "250px"
            }, 350);
            $(".logo").animate({
                width: "250px"
            }, 350);
            $(".logo img").attr("src", "img/logo.png");
            if (window.location.href.indexOf("mail.html") > -1) {
                $(".toc").load("html/loadmailmenu.html", function () {
                    $(".ui.accordion").accordion();
                    $(".logoImg").transition("tada");
                });
                $(this).data("name", "show");
            }
            else {
                $(".toc").load("html/loadsidemenu.html", function () {
                    $(".ui.accordion").accordion();
                    $(".logoImg").transition("tada");
                });
                $(this).data("name", "show");
            }
        }
    });
}
//Sidebar Menu Size Animaton Function

//Pace Loading (On Navbar) Function
function paceLoading() {
    var paceOptions = {
        restartOnRequestAfter: false
    };

    $(document).ajaxStart(function () {
        Pace.restart();
    });
}
//Pace Loading (On Navbar) Function

//Sidebar,Navbar,Mobile Sidebar,Mobile Navbar Loading Function
function loadhtml() {
    if (window.location.href.indexOf("mail.html") > -1) {
        $(".toc").load("html/loadmailmenu.html", function () {
            $(".ui.accordion").accordion();
        });
        $(".navbarmenu").load("html/loadnavbar.html", function () {
            hamburger();
            $(".ui.dropdown").dropdown();
        });
        $("#toc").load("html/loadmobilside.html", function () { });
        $(".mobilenavbar").load("html/loadmobilnavbar.html", function () {
            $(".ui.dropdown").dropdown({
                allowCategorySelection: true
            });
            $("#toc").sidebar("attach events", ".launch.button, .view-ui, .launch.item");
        });
    }
    else {
        $(".toc").load("html/loadsidemenu.html", function () {
            $(".ui.accordion").accordion();
            $(".sidemenu").niceScroll({ cursorcolor: "#ddd", cursorwidth: 5, cursorborderradius: 0, cursorborder: 0, scrollspeed: 50, autohidemode: true, zindex: 9999999, bouncescroll: true });//sidebar scrool trigger by nicescroll
        });
        $(".navbarmenu").load("html/loadnavbar.html", function () {
            hamburger();
            $(".ui.dropdown").dropdown();
        });
        $("#toc").load("html/loadmobilside.html", function () {
            $(".ui.accordion").accordion();
        });
        $(".mobilenavbar").load("html/loadmobilnavbar.html", function () {

            $(".ui.dropdown").dropdown({
                allowCategorySelection: true
            });
            $("#toc").sidebar("attach events", ".launch.button, .view-ui, .launch.item");
        });
    }
}
//Sidebar,Navbar,Mobile Sidebar,Mobile Navbar Loading Function

//Sidebar And Navbar Coloring Function (This button on Footer)
function colorize() {
    var a;
    var b;
    $(".footer").load("html/loadfooter.html", function () {
        $(".colorlist li a").on("click", function (b) {
            var c = $(this).attr("data-addClass");
            b.preventDefault();
            $(".navmenu").removeClass(a).addClass(c);
            a = c;
        });
        $(".sidecolor li a").on("click", function (a) {
            var c = $(this).attr("data-addClass");
            a.preventDefault();
            $(".sidemenu").removeClass(b).addClass(c);
            $(".accordion").removeClass("inverted").addClass("inverted");
            b = c;
        });
        $(".colorize").popup({
            on: "click"
        });
    });
}
//Sidebar And Navbar Coloring Function (This button on Footer)

//Button page and some buttons triggers function
function butonactions() {
    $(".save-button").click(function () {
        $(".save-modal").modal("show");
        setTimeout(function () {
            $(".save-modal").modal("hide");
        }, 1500);
    });

    $(".saving").on("click", function () {
        $(this).addClass("loading").delay(1500).queue(function () {
            $(this).removeClass("loading").dequeue();
        });
    }).state({
        text: {
            inactive: "Save",
            active: "Saved"
        }
    });

    $(".loadmore").on("click", function () {
        $(this).addClass("loading").delay(300).queue(function () {
            $(this).removeClass("loading").dequeue();
        });
    }).state({
        text: {
            inactive: "Show More",
            active: "Show More"
        }
    });

    var a = $(".ui.toggle.button");
    a.state({
        text: {
            inactive: "Vote",
            active: "Voted"
        }
    });
    var a = $(".ui.follow.button");
    a.state({
        text: {
            inactive: "Follow",
            active: "Following"
        }
    });

    $(".transition.demo .button").on("click", function () {
        var a = $(this).text();
        if ("string" == typeof a) a = a.toLowerCase();
        $(".transition.demo .image").each(function (b, c) {
            var d = $(this);
            setTimeout(function () {
                d.transition(a);
            }, 100 * b);
        });
    });
    $(".custom.button").popup({
        popup: $(".custom.popup"),
        on: "click"
    });
    $(".teal.button").popup({
        on: "click"
    });

    $(".follow").on("click", function () {
        $(this).addClass("loading").delay(1500).queue(function () {
            $(this).removeClass("loading").dequeue();
        });
    }).state({
        text: {
            inactive: "Follow",
            active: "Following"
        }
    });
}
//Button page and some buttons triggers function

//Tooltip page and some tooltip trigger function
function popupactions() {
    $("input").popup({
        on: "focus"
    });

    $(".ui.button").popup({
        on: "click"
    });
    $(".ui.image").popup();
    $(".ui.card").popup();
    $(".icon.link").popup();
    $(".avt").popup({
        position: "top center"
    });
    $('.custom.button').popup({
        popup: $('.custom.popup'),
        on: 'click'
    });
}
//Tooltip page and some tooltip trigger function

//Tab page tab trigger functions
function tabactions() {
    $(".menu .item").tab();
    $("#context1 .item").tab({
        context: $("#context1")
    });
    $(".paths.example .item ").tab({
        context: ".paths.example"
    });
    $(".history.example .item").tab({
        context: ".history.example",
        history: true
    });

    $(".tabular.menu .item").tab({
        history: true,
        historyType: "hash"
    });
}
//Tab page tab trigger functions



//Progress page progress action trigger function
function progressactions() {
    $(".increment").on("click", function () {
        $(".prr").progress({
            percent: "increment"
        });
    });
    $(".attached.progress.demo").progress({
        label: false,
        value: Math.floor(5 * Math.random()) + 1
    });
    $(".basic.progress.demo").progress({
        label: false,
        value: Math.floor(5 * Math.random()) + 1,
        text: {
            active: "{percent}% Complete",
            success: "Done!"
        }
    });
    $("#example6").progress({
        label: true,
        total: 10,
        value: Math.floor(5 * Math.random()) + 1,
        text: {
            active: "{percent}% Done",
            success: "Completed!"
        }
    });
    $(".file.progress.demo").progress({
        label: false,
        text: {
            active: "Uploading {value} of {total}",
            success: "{total} Files Uploaded!"
        }
    });
    var c = function () {
        $(".demo.progress").progress("increment");
        setTimeout(c, 2e3 * Math.random() + 300);
    };
    setTimeout(c, 1e3);
    setInterval(function () {
        $(".demo.progress").progress("reset");
    }, 3e4);
}
//Progress page progress action trigger function

//Form Elements (Radio,Checkbox) trigger function
function formelementactions() {
  

    $(".list .master.checkbox").checkbox({
        onChecked: function () {
            var a = $(this).closest(".checkbox").siblings(".list").find(".checkbox");
            a.checkbox("check");
        },
        onUnchecked: function () {
            var a = $(this).closest(".checkbox").siblings(".list").find(".checkbox");
            a.checkbox("uncheck");
        }
    });

    $(".list .child.checkbox").checkbox({
        fireOnInit: true,
        onChange: function () {
            var a = $(this).closest(".list"), b = a.closest(".item").children(".checkbox"), c = a.find(".checkbox"), d = true, e = true;
            c.each(function () {
                if ($(this).checkbox("is checked")) e = false; else d = false;
            });
            if (d) b.checkbox("set checked"); else if (e) b.checkbox("set unchecked"); else b.checkbox("set indeterminate");
        }
    });

    $(".ui.check").on("click", function () {
        $(this).addClass("loading").delay(500).queue(function () {
            $(this).removeClass("loading").dequeue();
        });
    }).state({
        text: {
            inactive: "Select All",
            active: "Unselect All"
        }
    });
}
//Form Elements (Radio,Checkbox) trigger function


//Notification triggers funtcion in notification page
function notifyactions() {
    $(".not").on("click", function () {
        var a, b, c, d, e, f, g, h, i, j, k;
        d = $(this).attr("data-size");
        e = $(this).attr("data-message");
        c = $(this).attr("data-type");
        f = $(this).attr("data-icon");
        g = $(this).attr("data-title");
        h = $(this).attr("data-image");
        i = $(this).attr("data-sound");
        a = $(this).attr("data-show-animation");
        b = $(this).attr("data-hide-animation");
        j = $(this).attr("data-position");
        k = $(this).attr("data-delay");
        Lobibox.notify(c, {
            size: d,
            rounded: false,
            delayIndicator: true,
            msg: e,
            icon: f,
            title: g,
            showClass: a,
            hideClass: b,
            sound: i,
            img: h,
            delay: k
        });
    });
}
//Notification triggers funtcion in notification page

//Message element close button trigger function
function messageclosebuttonactions() {
    $(".message .close").on("click", function () {
        $(this).closest(".message").transition("fade");
    });
}
//Message element close button trigger function

//Card hover function
function cardhoveractions() {
    $(".special.cards .image").dimmer({
        on: "hover"
    });
}
//Card hover function

//Lazy Load image function (in cards page)
$('.segment .image img').visibility({
    type: 'image',
    transition: 'fade in',
    duration: 1000
});
//Lazy Load image function (in cards page)

//some tooltip function
$(".avt").popup({
    position: "top center"
});
//some tooltip function
