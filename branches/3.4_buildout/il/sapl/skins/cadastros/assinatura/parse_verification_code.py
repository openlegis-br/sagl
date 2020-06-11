## Script (Python) "generate_verification_code"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=formatted_code
##title=
##
import re

if formatted_code is None or len(formatted_code) == 0:
    return formatted_code
return re.sub(r'[^A-Za-z0-9]', lambda x: '', formatted_code)

