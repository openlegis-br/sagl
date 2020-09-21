##parameters=linkLocation, page, step, length, **extras
#########################################################################
# Script (Python) "PageListOutput_pysc"
# Randolpho St. John
# randolphothegreat@yahoo.com
#
# Parameters:
# linkLocation -- base href the page links should point to
# page -- the current page number that is being displayed
# step -- the number of items of the list that are displayed at one time
# length -- the size of the list being processed in batch form.
# **extras -- a mapping of any other parameters to include in the page links.
#
# This script is designed to be used as a Script (Python) in Zope, however it can easily be adapted
# to any python using website. Its goal is to create an indexible page system for batch results.
# Rather than a simple "Next x , Previous x" system, this script creates a list of "page numbers"
# similar to what you might find at the bottom of a Google search. It is inspired by the
# functionality of a page list I once saw on a vBullitin web forum. This script is designed
# to specifically emulate that page list system. However, the lessons learned from this script
# can be adapted to other versions, such as the Google style mentioned above.
#
# This script returns html, a series of links to various pages of batch results. If the following
# parameters (linkLocation="viewResults", page=3, step=20, length=300, sort="price") were sent
# to the script, a link output might look like this:
#
#   ...
#   <A href="viewResults?page=1&step=20&sort=price">1</A>
#   <A href="viewResults?page=2&step=20&sort=price">2</A>
#   [3]
#   <A href="viewResults?page=4&step=20&sort=price">4</A>
#   ...
#
# Rendered ouput on page 10 of a 20 page list might look like this:
#   Pages (20): First ... << 8 9 [10] 11 12 >> ... Last
#
# To use this script, simply call it using <dtml-var> at some point on the page. Note that length
# will need to be calculated ahead of time. When you iterate over your batch, use the following
# attributes for your <dtml-in> call to ensure the pages match with the values:
#
# start = (page - 1) * step + 1         
# size = step                           
# orphan = 0      -- this is necessary!!!
#
# Additional Modifications:
#   if you like, you may modify some of the rendring data... Using symbols rather than the word
#   "First" for example -- even images. Simply modify some of the variables below.
#########################################################################
#
#####################
# Use Modifications #
#####################
#
# Display options
#
DisplayAll = 0                              # set flag to 1 to display every page, rather than
                                            # a few around the current page. If true, PageRange
                                            # will be ignored. WARNING: this could cause
                                            # quite a bit of trouble if you have an excessively
                                            # large list with a comparatively low batch size!
PageRange = 2                               # number of pages before and after the current page
                                            # to display
#
# show item flags. Set to 1 to enable, set to 0 to disable.
#
showTotalPages = 0                          # show a total number of pages
showEllipses = 0                            # show a string signifying that not all pages numbers
                                            # are displayed
showNext = 1                                # show a "Next Page" link
showPrevious = 1                            # show a "Previous Page" link
showFirst = 1                               # show a link ot the first page
showLast = 1                                # show a link to the last page
#
# output strings. Modify to alter what is returned by the script.
#
TotalPagesFormatString = "<li class='page-item disabled'><a class='page-link'>Páginas (%s):</a></li>"    # String to use when showing total number of pages.
# Use %s to signify where the page number will be displayed.
EllipsesString = "<li class='page-item disabled'><a class='page-link'>...</a></li>"  # String signifying that not all pages numbers are displayed
NextString = ">>"                           # content of the "Next Page" link                 
PreviousString = "<<"                       # content of the "Previous Page" link
FirstString = "Início"                           # content of the "First Page" link
LastString = "Fim"                            # content of the "Last Page" link
CurrentPageFormatString = "<li class='page-item active'><a class='page-link'>%s</a></li>" # String to use when showing the current page (which is not a link).
# Use %s to signify where the current page number is displayed.
#
#####################
# End Modifications #
#####################
# validate parameters received
try:
    length = int(length)
    step = int(step)
    page = int(page)
    linkLocation = str(linkLocation)
    for item, value in extras.items():
        extras[item] = str(value)
       
except:
    # this may be changed to suit your needs
    return "error building page list"
# build the format string we'll be using for all page links. The only thing that will change
# is the page number and the content of the link.
linkString = '<li class="page-item"><a class="page-link" href="' + linkLocation + "?page=%s&amp;step=" + str(step)
for item, value in extras.items():
  if item == 'txt_assunto':
    value = '%22'.join(value.split('\"'))
    value = '%2B'.join(value.split('+'))
  if item == 'txt_texto':
    value = '%22'.join(value.split('\"'))
    value = '%2B'.join(value.split('+'))
  if item == 'txa_txt_assunto':
    value = '%22'.join(value.split('\"'))
    value = '%2B'.join(value.split('+'))
  if item == 'txa_txt_interessado':
    value = '%22'.join(value.split('\"'))
    value = '%2B'.join(value.split('+'))
  if item == 'txa_txt_nom_instituicao':
    value = '%22'.join(value.split('\"'))
    value = '%2B'.join(value.split('+'))
  if item == 'txt_nom_pessoa':
    value = '%22'.join(value.split('\"'))
    value = '%2B'.join(value.split('+'))
 
  linkString = linkString + ("&%s=%s" % (item, value))
linkString = linkString + '">%s</a></li>'
# Find the total number of pages we need:
numPages, remainder = divmod(length, step)
if remainder != 0:
    numPages = numPages + 1
# begin setting up the pages we'll display. This is currently hard-wired. Perhaps
# some way of making the total number dynamic later?
first = page - 2
second = page - 1
fourth = page + 1
fifth = page + 2
# build our returned output
returnString = ""
linkStringTemp = ""
if showTotalPages:
    returnString = returnString + (TotalPagesFormatString %numPages)
if showFirst:
    if page >= 2:
       linkStringTemp = 'page=1'.join(linkString.split('page=%s'))
       linkStringTemp = FirstString.join(linkStringTemp.split('%s'))
       returnString = returnString + linkStringTemp
    else:
       returnString = returnString + " " + FirstString + " "
if showEllipses:
    returnString = returnString + " " + EllipsesString + " "
if showPrevious:
    if page > 1:
        linkStringTemp = ('page=' + str(second)).join(linkString.split('page=%s'))
        linkStringTemp = PreviousString.join(linkStringTemp.split('%s'))
        returnString = returnString + linkStringTemp
    else:
        returnString = PreviousString.join(linkStringTemp.split('%s'))
if DisplayAll:
    LinkRange = range(1, numPages + 1)
else:   
    LinkRange = range(page - PageRange - max(0, (page + PageRange - numPages)), page + PageRange + 1 - min (0, (page - PageRange - 1)))
for index in LinkRange:
    if index > 0 and index < page:
        linkStringTemp = str(index).join(linkString.split('%s'))
        returnString = returnString + linkStringTemp
    if index == page:
        returnString = returnString + (CurrentPageFormatString % page) 
    if index > page and index <= numPages:
        linkStringTemp = str(index).join(linkString.split('%s'))
        returnString = returnString + linkStringTemp
   
if showNext:
    if page < numPages:
        linkStringTemp = ('page=' + str(fourth)).join(linkString.split('page=%s'))
        linkStringTemp = NextString.join(linkStringTemp.split('%s'))
        returnString = returnString + linkStringTemp
    else:
        returnString = returnString
       
if showEllipses:
    returnString = returnString + " " + EllipsesString + " "
   
if showLast:
    if page <= numPages - 1:
        linkStringTemp = ('page=' + str(numPages)).join(linkString.split('page=%s'))
        linkStringTemp = LastString.join(linkStringTemp.split('%s'))
        returnString = returnString + linkStringTemp
    else:
        returnString = returnString
return returnString
