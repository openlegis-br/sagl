## Script (Python) "generate_verification_code"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
import binascii
import os

VERIFICATION_CODE_SIZE = 16
VERIFICATION_CODE_GROUPS = 4
rnd_value = os.urandom(int(VERIFICATION_CODE_SIZE / 2))
hex_value = binascii.hexlify(rnd_value).upper()
return hex_value.decode('ascii')


