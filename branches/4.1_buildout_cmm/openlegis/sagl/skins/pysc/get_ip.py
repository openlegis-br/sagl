request=context.REQUEST

if "HTTP_X_FORWARDED_FOR" in request.environ:
    # Virtual host
    ip = request.environ["HTTP_X_FORWARDED_FOR"]
elif "HTTP_HOST" in request.environ:
    # Non-virtualhost
    ip = request.environ["REMOTE_ADDR"]
else:
    # Unit test code?
    ip = None

return ip
