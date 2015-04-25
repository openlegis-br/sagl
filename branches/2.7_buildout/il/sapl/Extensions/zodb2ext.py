"""zodb2ext

Given a file or image, converts to ExtFile or ExtImage
vsbabu-removethis@vsbabu.org - 11/25/01
"""
from StringIO import StringIO
#  cStringIO doesn't work! Need to see why
__version__ = '0.0.1'

def make_stream(o):
    """makes a StringIO stream for a given zodb object o
    
    shameless copy from lib/python/OFS/Image.py , index_html
    """
    (start,end) = (0,o.getSize())
    data = o.data
    if type(data) is type(''): #StringType
        infile = StringIO(data[start:end])
    else:
        pos = 0
        infile = StringIO(data.data)
        while data is not None:
            l =  len(data.data)
            pos = pos + l
            if pos > start:
                # We are within the range
                lstart = l - (pos - start)

                if lstart < 0: lstart = 0
                
                # find the endpoint
                if end <= pos:
                    lend = l - (pos - end)
                    
                    infile.write(data[lstart:lend])
                    break

                # Not yet at the end, transmit what we have.
                infile.write(data[lstart:])

            data = data.next
    infile.seek(0)
    return infile

def zodb2ext(self,o):
    """ Given a file or image, converts to ExtFile or ExtImage """
    
    if o.meta_type == 'File':
        nid = o.getId()
        infile = make_stream(o)
        self.manage_delObjects([nid])
        self.manage_addProduct['ExtFile'].manage_addExtFile(id=nid,
                              title=o.title, descr='', file=infile)
        infile.close()
    elif o.meta_type == 'Image':
        nid = o.getId()
        infile = make_stream(o)
        self.manage_delObjects([nid])
        self.manage_addProduct['ExtFile'].manage_addExtImage(id=nid,
                              title=o.title, descr='', file=infile)
        infile.close()
    else:
        return 'Object should be File or Image'

    return ''

