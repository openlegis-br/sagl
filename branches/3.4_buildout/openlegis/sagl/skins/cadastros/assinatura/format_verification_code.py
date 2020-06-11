## Script (Python) "generate_verification_code"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=code
##title=
##

VERIFICATION_CODE_SIZE = 16
VERIFICATION_CODE_GROUPS = 4

chars_per_group = VERIFICATION_CODE_SIZE / VERIFICATION_CODE_GROUPS
groups = []

for i in range(VERIFICATION_CODE_GROUPS):
    groups.append(code[int(i * chars_per_group):int((i + 1) * chars_per_group)])

return '-'.join(groups)

