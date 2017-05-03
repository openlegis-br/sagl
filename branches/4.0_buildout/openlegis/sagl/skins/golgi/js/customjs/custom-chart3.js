//chart page 3 charts settings
'use strict'
window.onload = function () {
    var chart = new CanvasJS.Chart("chartContainer",
    {
        title: {
            text: "Music Album Sales by Year"
        },
        animationEnabled: true,
        axisY: {
            title: "Units Sold",
            valueFormatString: "#0,,.",
            suffix: " m"
        },
        data: [
        {
            toolTipContent: "{y} units",
            type: "splineArea",
            markerSize: 5,
            color: "rgba(54,158,173,.7)",
            dataPoints: [
            { x: new Date(1992, 0), y: 2506000 },
            { x: new Date(1993, 0), y: 2798000 },
            { x: new Date(1994, 0), y: 3386000 },
            { x: new Date(1995, 0), y: 6944000 },
            { x: new Date(1996, 0), y: 6026000 },
            { x: new Date(1997, 0), y: 2394000 },
            { x: new Date(1998, 0), y: 1872000 },
            { x: new Date(1999, 0), y: 2140000 },
            { x: new Date(2000, 0), y: 7289000 },
            { x: new Date(2001, 0), y: 4830000 },
            { x: new Date(2002, 0), y: 2009000 },
            { x: new Date(2003, 0), y: 2840000 },
            { x: new Date(2004, 0), y: 2396000 },
            { x: new Date(2005, 0), y: 1613000 },
            { x: new Date(2006, 0), y: 2821000 },
            { x: new Date(2007, 0), y: 2000000 },
            { x: new Date(2008, 0), y: 1397000 }
            ]
        }
        ]
    });

    chart.render();

    var chart1 = new CanvasJS.Chart("chartContainer1",
    {
        title: {
            text: "Multi-Series Spline Area Chart"
        },
        animationEnabled: true,
        data: [
        {
            type: "splineArea",
            color: "rgba(54,158,173,.7)",

            dataPoints: [
            { y: 1 },
            { y: 8 },
            { y: 18 },
            { y: 28 },
            { y: 31 },
            { y: 14 },
            { y: 26 },
            { y: 9 },
            { y: 18 },
            { y: 11 },
            { y: 7 },
            { y: 1 }
            ]
        },
        {
            type: "splineArea",
            color: "rgba(194,70,66,.7)",
            dataPoints: [
            { y: 14 },
            { y: 23 },
            { y: 21 },
            { y: 16 },
            { y: 12 },
            { y: 14 },
            { y: 18 },
            { y: 14 },
            { y: null },
            { y: 12 },
            { y: 17 },
            { y: 14 }
            ]
        }

        ]
    });

    chart1.render();

    var chart2 = new CanvasJS.Chart("chartContainer2",
{
    title: {
        text: "Growth of Gangnam Style on YouTube"
    },
    animationEnabled: true,
    axisX: {
        valueFormatString: "DD-MMM",
        interval: 10,
        intervalType: "day",
        labelAngle: -50,
        labelFontColor: "rgb(0,75,141)",
        minimum: new Date(2012, 6, 10)
    },
    axisY: {
        title: "Views on YouTube",
        interlacedColor: "#F0FFFF",
        tickColor: "azure",
        titleFontColor: "rgb(0,75,141)",
        valueFormatString: "#M,,.",
        interval: 100000000
    },
    data: [
    {
        indexLabelFontColor: "darkSlateGray",
        name: 'views',
        type: "area",
        color: "rgba(0,75,141,0.7)",
        markerSize: 8,
        dataPoints: [
        { x: new Date(2012, 6, 15), y: 0, indexLabel: "Release", indexLabelOrientation: "vertical", indexLabelFontColor: "orangered", markerColor: "orangered" },
        { x: new Date(2012, 6, 18), y: 2000000 },
        { x: new Date(2012, 6, 23), y: 6000000 },
        { x: new Date(2012, 7, 1), y: 10000000, indexLabel: "10m" },
        { x: new Date(2012, 7, 11), y: 21000000 },
        { x: new Date(2012, 7, 23), y: 50000000 },
        { x: new Date(2012, 7, 31), y: 75000000 },
        { x: new Date(2012, 08, 4), y: 100000000, indexLabel: "100m" },
        { x: new Date(2012, 08, 10), y: 125000000 },
        { x: new Date(2012, 08, 13), y: 150000000 },
        { x: new Date(2012, 08, 16), y: 175000000 },
        { x: new Date(2012, 08, 18), y: 200000000, indexLabel: "200m" },
        { x: new Date(2012, 08, 21), y: 225000000 },
        { x: new Date(2012, 08, 24), y: 250000000 },
        { x: new Date(2012, 08, 26), y: 275000000 },
        { x: new Date(2012, 08, 28), y: 302000000, indexLabel: "300m" }
        ]
    }

    ]
});

    chart2.render();

    var chart3 = new CanvasJS.Chart("chartContainer3", {
        animationEnabled: true,
        zoomEnabled: true,
        title: {
            text: "Monthly Average Crude Oil Prices"
        },
        legend: {
            verticalAlign: "bottom",
            horizontalAlign: "center"
        },
        axisY: {
            includeZero: false,
            prefix: "$",
            title: "inflation adjusted price",
            maximum: 110
        },
        data: [
        {
            type: "stepLine",
            markerSize: 0,
            toolTipContent: "{x} <strong>${y} <strong>",
            dataPoints: [
            { x: new Date(2011, 0), y: 89.28 },
            { x: new Date(2011, 1), y: 85.53 },
            { x: new Date(2011, 2), y: 98.66 },
            { x: new Date(2011, 3), y: 105.72 },
            { x: new Date(2011, 4), y: 95.72 },
            { x: new Date(2011, 5), y: 90.67 },
            { x: new Date(2011, 6), y: 91.51 },
            { x: new Date(2011, 7), y: 79.86 },
            { x: new Date(2011, 8), y: 79.31 },
            { x: new Date(2011, 9), y: 80.19 },
            { x: new Date(2011, 10), y: 91.34 },
            { x: new Date(2011, 11), y: 93.14 },
            { x: new Date(2012, 0), y: 94.18 },
            { x: new Date(2012, 1), y: 96.17 },
            { x: new Date(2012, 2), y: 99.49 },
            { x: new Date(2012, 3), y: 96.22 },
            { x: new Date(2012, 4), y: 87.31 },
            { x: new Date(2012, 5), y: 75.40 },
            { x: new Date(2012, 6), y: 80.93 },
            { x: new Date(2012, 7), y: 88.04 },
            { x: new Date(2012, 8), y: 88.41 },
            { x: new Date(2012, 9), y: 83.06 },
            { x: new Date(2012, 10), y: 80.55 },
            { x: new Date(2012, 11), y: 82.35 },
            { x: new Date(2013, 0), y: 88.60 },
            { x: new Date(2013, 1), y: 86.48 },
            { x: new Date(2013, 2), y: 87.50 }
            ]
        }
        ]
    });
    chart3.render();

    var chart4 = new CanvasJS.Chart("chartContainer4",
{
    title: {
        text: "Gold Won in Olympics"
    },
    animationEnabled: true,
    axisY: {
        titleFontFamily: "arial",
        titleFontSize: 12,
        includeZero: false
    },
    toolTip: {
        shared: true
    },
    data: [
    {
        type: "spline",
        name: "US",
        showInLegend: true,
        dataPoints: [
        { label: "Atlanta 1996", y: 44 },
        { label: "Sydney 2000", y: 37 },
        { label: "Athens 2004", y: 34 },
        { label: "Beijing 2008", y: 36 },
        { label: "London 2012", y: 46 }
        ]
    },
    {
        type: "spline",
        name: "China",
        showInLegend: true,
        dataPoints: [
        { label: "Atlanta 1996", y: 16 },
        { label: "Sydney 2000", y: 28 },
        { label: "Athens 2004", y: 32 },
        { label: "Beijing 2008", y: 51 },
        { label: "London 2012", y: 38 }
        ]
    },
    {
        type: "spline",
        name: "Britain",
        showInLegend: true,
        dataPoints: [
        { label: "Atlanta 1996", y: 1 },
        { label: "Sydney 2000", y: 11 },
        { label: "Athens 2004", y: 9 },
        { label: "Beijing 2008", y: 19 },
        { label: "London 2012", y: 29 }
        ]
    },
    {
        type: "spline",
        name: "Russia",
        showInLegend: true,
        dataPoints: [
        { label: "Atlanta 1996", y: 26 },
        { label: "Sydney 2000", y: 32 },
        { label: "Athens 2004", y: 28 },
        { label: "Beijing 2008", y: 23 },
        { label: "London 2012", y: 24 }
        ]
    },
    {
        type: "spline",
        name: "S Korea",
        showInLegend: true,
        dataPoints: [
        { label: "Atlanta 1996", y: 7 },
        { label: "Sydney 2000", y: 8 },
        { label: "Athens 2004", y: 9 },
        { label: "Beijing 2008", y: 13 },
        { label: "London 2012", y: 13 }
        ]
    },
    {
        type: "spline",
        name: "Germany",
        showInLegend: true,
        dataPoints: [
        { label: "Atlanta 1996", y: 20 },
        { label: "Sydney 2000", y: 13 },
        { label: "Athens 2004", y: 13 },
        { label: "Beijing 2008", y: 16 },
        { label: "London 2012", y: 11 }
        ]
    }
    ],
    legend: {
        cursor: "pointer",
        itemclick: function (e) {
            if (typeof (e.dataSeries.visible) === "undefined" || e.dataSeries.visible) {
                e.dataSeries.visible = false;
            }
            else {
                e.dataSeries.visible = true;
            }
            chart.render();
        }
    }
});

    chart4.render();

    var chart5 = new CanvasJS.Chart("chartContainer5",
{
    title: {
        text: "Email Categories",
        verticalAlign: 'top',
        horizontalAlign: 'left'
    },
    animationEnabled: true,
    data: [
    {
        type: "doughnut",
        startAngle: 20,
        toolTipContent: "{label}: {y} - <strong>#percent%</strong>",
        indexLabel: "{label} #percent%",
        dataPoints: [
            { y: 67, label: "Inbox" },
            { y: 28, label: "Archives" },
            { y: 10, label: "Labels" },
            { y: 7, label: "Drafts" },
            { y: 4, label: "Trash" }
        ]
    }
    ]
});
    chart5.render();

    var chart6 = new CanvasJS.Chart("chartContainer6",
{
    title: {
        text: "Top Categories of New Year's Resolution"
    },
    exportFileName: "Pie Chart",
    exportEnabled: true,
    animationEnabled: true,
    legend: {
        verticalAlign: "bottom",
        horizontalAlign: "center"
    },
    data: [
    {
        type: "pie",
        showInLegend: true,
        toolTipContent: "{legendText}: <strong>{y}%</strong>",
        indexLabel: "{label} {y}%",
        dataPoints: [
            { y: 35, legendText: "Health", exploded: true, label: "Health" },
            { y: 20, legendText: "Finance", label: "Finance" },
            { y: 18, legendText: "Career", label: "Career" },
            { y: 15, legendText: "Education", label: "Education" },
            { y: 5, legendText: "Family", label: "Family" },
            { y: 7, legendText: "Real Estate", label: "Real Estate" }
        ]
    }
    ]
});
    chart6.render();

    var chart7 = new CanvasJS.Chart("chartContainer7",
{
    theme: 'theme2',
    title: {
        text: "Time Spent in Holiday Season"
    },
    animationEnabled: true,
    axisY: {
        title: "percent"
    },
    legend: {
        horizontalAlign: 'center',
        verticalAlign: 'bottom'
    },
    toolTip: {
        shared: true
    },
    data: [
    {
        type: "stackedBar100",
        showInLegend: true,
        name: "With Friends",
        dataPoints: [
        { y: 350, label: "George" },
        { y: 350, label: "Alex" },
        { y: 350, label: "Mike" },
        { y: 374, label: "Jake" },
        { y: 320, label: "Shah" },
        { y: 300, label: "Joe" },
        { y: 400, label: "Fin" },
        { y: 220, label: "Larry" }

        ]
    },

    {
        type: "stackedBar100",
        showInLegend: true,
        name: "Eating Out",
        dataPoints: [
        { y: 250, label: "George" },
        { y: 280, label: "Alex" },
        { y: 350, label: "Mike" },
        { y: 274, label: "Jake" },
        { y: 320, label: "Shah" },
        { y: 320, label: "Joe" },
        { y: 280, label: "Fin" },
        { y: 420, label: "Larry" }

        ]
    },
    {
        type: "stackedBar100",
        showInLegend: true,
        name: "Reading",
        dataPoints: [
        { y: 350, label: "George" },
        { y: 350, label: "Alex" },
        { y: 350, label: "Mike" },
        { y: 374, label: "Jake" },
        { y: 120, label: "Shah" },
        { y: 120, label: "Joe" },
        { y: 400, label: "Fin" },
        { y: 120, label: "Larry" }

        ]
    },

    {
        type: "stackedBar100",
        showInLegend: true,
        name: "Shopping",
        dataPoints: [
        { y: 250, label: "George" },
        { y: 250, label: "Alex" },
        { y: 250, label: "Mike" },
        { y: 274, label: "Jake" },
        { y: 320, label: "Shah" },
        { y: 220, label: "Joe" },
        { y: 100, label: "Fin" },
        { y: 420, label: "Larry" }

        ]
    },
    {
        type: "stackedBar100",
        showInLegend: true,
        name: "Fitness",
        dataPoints: [
        { y: 150, label: "George" },
        { y: 30, label: "Alex" },
        { y: 45, label: "Mike" },
        { y: 74, label: "Jake" },
        { y: 64, label: "Shah" },
        { y: 40, label: "Joe" },
        { y: 50, label: "Fin" },
        { y: 40, label: "Larry" }

        ]
    },

    {
        type: "stackedBar100",
        showInLegend: true,
        name: "Travel",
        dataPoints: [
        { y: 150, label: "George" },
        { y: 170, label: "Alex" },
        { y: 150, label: "Mike" },
        { y: 174, label: "Jake" },
        { y: 120, label: "Shah" },
        { y: 160, label: "Joe" },
        { y: 100, label: "Fin" },
        { y: 80, label: "Larry" }

        ]
    },

    {
        type: "stackedBar100",
        showInLegend: true,
        name: "Internet",
        dataPoints: [
        { y: 160, label: "George" },
        { y: 170, label: "Alex" },
        { y: 50, label: "Mike" },
        { y: 174, label: "Jake" },
        { y: 104, label: "Shah" },
        { y: 120, label: "Joe" },
        { y: 300, label: "Fin" },
        { y: 420, label: "Larry" }

        ]
    },

    {
        type: "stackedBar100",
        showInLegend: true,
        name: "Hobbies",
        dataPoints: [
        { y: 80, label: "George" },
        { y: 150, label: "Alex" },
        { y: 50, label: "Mike" },
        { y: 74, label: "Jake" },
        { y: 40, label: "Shah" },
        { y: 120, label: "Joe" },
        { y: 100, label: "Fin" },
        { y: 120, label: "Larry" }

        ]
    }

    ]
});

    chart7.render();

    var chart8 = new CanvasJS.Chart("chartContainer8",
{
    title: {
        text: "Number of Students in Each Room"
    },
    animationEnabled: true,
    axisX: {
        title: "Rooms"
    },
    axisY: {
        title: "percentage"
    },
    data: [
    {
        type: "stackedColumn100",
        name: "Boys",
        showInLegend: "true",
        dataPoints: [
        { y: 40, label: "Cafeteria" },
        { y: 10, label: "Lounge" },
        { y: 72, label: "Games Room" },
        { y: 30, label: "Lecture Hall" },
        { y: 21, label: "Library" }
        ]
    }, {
        type: "stackedColumn100",
        name: "Girls",
        showInLegend: "true",
        dataPoints: [
        { y: 20, label: "Cafeteria" },
        { y: 14, label: "Lounge" },
        { y: 40, label: "Games Room" },
        { y: 43, label: "Lecture Hall" },
        { y: 17, label: "Library" }
        ]
    }

    ]
});

    chart8.render();

    var dps = []; // dataPoints

    var chart9 = new CanvasJS.Chart("chartContainer9", {
        title: {
            text: "Live Random Data"
        },
        data: [{
            type: "line",
            dataPoints: dps
        }]
    });

    var xVal = 0;
    var yVal = 100;
    var updateInterval = 100;
    var dataLength = 500; // number of dataPoints visible at any point

    var updateChart = function (count) {
        count = count || 1;
        // count is number of times loop runs to generate random dataPoints.

        for (var j = 0; j < count; j++) {
            yVal = yVal + Math.round(5 + Math.random() * (-5 - 5));
            dps.push({
                x: xVal,
                y: yVal
            });
            xVal++;
        };
        if (dps.length > dataLength) {
            dps.shift();
        }

        chart9.render();
    };

    // generates first set of dataPoints
    updateChart(dataLength);

    // update chart after specified time.
    setInterval(function () { updateChart() }, updateInterval);
}