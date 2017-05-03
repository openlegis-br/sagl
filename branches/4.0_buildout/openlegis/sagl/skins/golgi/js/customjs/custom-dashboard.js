//Sparkline chart settings
var sparker = function () {
    $("#sparkline1").sparkline([5, 2, 4, 9, 3, 4, 7, 2, 6, 4], { type: 'bar', barColor: 'rgba(255,255,255,0.5)', height: '58px', width: '100%', barWidth: 3, barSpacing: 4, spotRadius: 4, chartRangeMin: 1 });
    $("#sparkline2").sparkline([2, 5, 4, 9, 6, 3, 7, 1, 5, 1], { type: 'bar', barColor: 'rgba(255,255,255,0.5)', height: '58px', width: '100%', barWidth: 3, barSpacing: 4, spotRadius: 4, chartRangeMin: 1 });
    $("#sparkline3").sparkline([1, 3, 2, 9, 1, 6, 5, 2, 6, 9], { type: 'bar', barColor: 'rgba(255,255,255,0.5)', height: '58px', width: '100%', barWidth: 3, barSpacing: 4, spotRadius: 4, chartRangeMin: 1 });
    $("#sparkline4").sparkline([5, 3, 1, 4, 3, 4, 7, 8, 2, 3], { type: 'bar', barColor: 'rgba(255,255,255,0.5)', height: '58px', width: '100%', barWidth: 3, barSpacing: 4, spotRadius: 4, chartRangeMin: 1 });
}
var sparkResize;

$(window).resize(function (e) {
    clearTimeout(sparkResize);
    sparkResize = setTimeout(sparker, 500);
});
sparker();
//Sparkline chart settings

//Morris Chart settings
Morris.Donut({
    element: 'graph1',
    data: [
      { value: 70, label: 'Chrome' },
      { value: 15, label: 'Firefox' },
      { value: 10, label: 'Yandex' },
      { value: 5, label: 'Explorer' }
    ],
    backgroundColor: '#EDF2F4',
    labelColor: '#50514F',
    colors: [
      '#FFE066',
      '#FF5714',
      '#50514F',
      '#247BA0'
    ],
    resize: true, //defaulted to true
    formatter: function (x) { return x + "%" }
});

Morris.Area({
    element: 'graph2',
    data: [
      { y: '2008', a: 90, b: 0 },
      { y: '2009', a: 75, b: 50 },
      { y: '2010', a: 30, b: 80 },
      { y: '2011', a: 50, b: 50 },
      { y: '2012', a: 75, b: 10 },
      { y: '2013', a: 50, b: 40 },
      { y: '2014', a: 90, b: 50 },
      { y: '2015', a: 95, b: 20 }
    ],
    xkey: 'y',
    ykeys: ['a', 'b'],
    labels: ['Apple', 'Samsung'],
    fillOpacity: '1',
    pointFillColors: '#fff',
    pointStrokeColors: '#999999',
    behaveLikeLine: true,
    gridLineColor: '#eef0f2',
    hideHover: 'auto',
    resize: true, //defaulted to true
    pointSize: 0,
    lineColors: ['#0B62A4', '#32936F'],
    axes:false

});

Morris.Bar({
    element: 'graph3',
    data: [
       { y: '2006', a: 100, b: 90 },
       { y: '2007', a: 75,  b: 65 },
       { y: '2008', a: 50,  b: 40 },
       { y: '2009', a: 75,  b: 65 },
       { y: '2010', a: 50,  b: 40 },
       { y: '2011', a: 75,  b: 65 },
       { y: '2012', a: 100, b: 90 }
    ],
    xkey: 'y',
    ykeys: ['a', 'b'],
    labels: ['Series A', 'Series B'],
    barColors: ['#FF5714', '#50514F'],
    hideHover: 'auto',
    resize: true, //defaulted to true
});
//Morris Chart settings


//dashboard page calendar trigger
$('#calendar').datepicker({
    forceParse: false,
    calendarWeeks: true,
    todayHighlight: true
});
//dashboard page calendar trigger

//dashboard page loading segment trigger
$(".refresh").on("click", function () {
    $(".dimmer").addClass("active").delay(1500).queue(function () {
        $(".dimmer").removeClass("active").dequeue();
    });
});
//dashboard page loading segment trigger
