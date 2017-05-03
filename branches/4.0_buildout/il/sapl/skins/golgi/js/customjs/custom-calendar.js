//calendar page jquery settings (Fullcalendar.io)
'use strict';
$(function () {
    /* initialize the external events
     -----------------------------------------------------------------*/
    function ini_events(ele) {
        ele.each(function () {
            // create an Event Object (http://arshaw.com/fullcalendar/docs/event_data/Event_Object/)
            // it doesn't need to have a start or end
            var eventObject = {
                title: $.trim($(this).text()) // use the element's text as the event title
            };

            // store the Event Object in the DOM element so we can get to it later
            $(this).data('eventObject', eventObject);

            // make the event draggable using jQuery UI
            $(this).draggable({
                zIndex: 1070,
                revert: true, // will cause the event to go back to its
                revertDuration: 0  //  original position after the drag
            });
        });
    }

    ini_events($('#external-events .external-event'));

    /* initialize the calendar
     -----------------------------------------------------------------*/
    //Date for the calendar events (dummy data)
    var date = new Date();
    var d = date.getDate(),
        m = date.getMonth(),
        y = date.getFullYear();
    $('#calendar').fullCalendar({
        header: {
            left: 'prev,next today',
            center: 'title',
            right: 'month,agendaWeek,agendaDay'
        },
        defaultDate: '2016-01-12',
        editable: true,
        eventLimit: true, // allow "more" link when too many events
        eventRender: function (event, element) {
            element.popup({
                title: event.title,

                content: event.msg,
                transition: 'horizontal flip',
                inline: false,
                hoverable: true,
                position: 'top center',
                delay: {
                    show: 100,
                    hide: 150
                }
            });
        },
        events: [
            {
                title: 'All Day Event',
                start: '2016-01-01'
            },
            {
                title: 'Long Event',
                start: '2016-01-07',
                end: '2016-01-10',
                color: 'teal'
            },
            {
                id: 999,
                title: 'Repeating Event',
                start: '2016-01-09T16:00:00',
                color: 'red'
            },
            {
                id: 999,
                title: 'Repeating Event',
                start: '2016-01-16T16:00:00',
                color: 'brown'
            },
            {
                title: 'Conference',
                start: '2016-01-11',
                end: '2016-01-13',
                color: 'orange'
            },
            {
                title: 'Meeting',
                start: '2016-01-12T10:30:00',
                end: '2016-01-12T12:30:00',
                color: 'grey'
            },
            {
                title: 'Lunch',
                start: '2016-01-12T12:00:00',
                color: 'black'
            },
            {
                title: 'Meeting',
                start: '2016-01-12T14:30:00'
            },
            {
                title: 'Happy Hour',
                start: '2016-01-12T17:30:00'
            },
            {
                title: 'Dinner',
                start: '2016-01-12T20:00:00'
            },
            {
                title: 'Birthday Party',
                start: '2016-01-13T07:00:00', color: 'violet'
            },
            {
                title: 'Click for Google',
                url: 'http://google.com/',
                start: '2016-01-28',
                color: 'purple'
            }
        ],
        
        droppable: true, // this allows things to be dropped onto the calendar !!!
        drop: function (date, allDay) { // this function is called when something is dropped
            // retrieve the dropped element's stored Event Object
            var originalEventObject = $(this).data('eventObject');

            // we need to copy it, so that multiple events don't have a reference to the same object
            var copiedEventObject = $.extend({}, originalEventObject);

            // assign it the date that was reported
            copiedEventObject.start = date;
            copiedEventObject.allDay = allDay;
            copiedEventObject.backgroundColor = $(this).css("background-color");
            copiedEventObject.borderColor = $(this).css("border-color");

            // render the event on the calendar
            // the last `true` argument determines if the event "sticks" (http://arshaw.com/fullcalendar/docs/event_rendering/renderEvent/)
            $('#calendar').fullCalendar('renderEvent', copiedEventObject, true);

            // is the "remove after drop" checkbox checked?
            if ($('#drop-remove').is(':checked')) {
                // if so, remove the element from the "Draggable Events" list
                $(this).remove();
            }
        }
    });
    $('.fc-toolbar').find('button').addClass('ui button blue inverted calendarbtn');

    /* ADDING EVENTS */
    var currColor = "inverted red"; //Red by default
    var a;
    //Color chooser button
    //var colorChooser = $("#color-chooser-btn");
    $("#color-chooser > li > a").click(function (e) {
        e.preventDefault();
        //Save color
        var currColor = $(this).attr("data-addclass");
        //Add color effect to button
        $('#add-new-event').removeClass(a).addClass(currColor);
        a = currColor;
    });
    $("#add-new-event").click(function (e) {
        e.preventDefault();
        //Get value and make sure it is not null
        var val = $("#new-event").val();
        if (val.length == 0) {
            return;
        }

        //Create events
        var event = $("<div />");
        event.addClass("external-event ui segment inverted " + a + "");
        event.html(val);
        $('#external-events').prepend(event);

        //Add draggable funtionality
        ini_events(event);

        //Remove event from text input
        $("#new-event").val("");
    });
});