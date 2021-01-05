##parameters=
##title=Return Title or getId
##
title = context.Title()
id = context.getId()
if title:
    return title
else:
    return id
