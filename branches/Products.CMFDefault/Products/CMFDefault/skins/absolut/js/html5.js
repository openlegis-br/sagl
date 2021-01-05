// Modified fo legibility http://remysharp.com/2009/01/07/html5-enabling-script/
        
function add_elements()
    // Add HTML 5 specific elements for Internet Explorer
    {
    if(!/*@cc_on!@*/0)
       {return;
        }
    var elements = ["abbr", "article", "aside", "audio", "canvas", "datalist",
             "details", "figure", "figcaption", "footer", "header", "hgroup",
             "mark" ,"menu", "meter", "nav", "output", "progress", "section",
             "summary", "time", "video"];

    for (i in elements)
        {
        document.createElement(elements[i]);
        }
    }

add_elements();