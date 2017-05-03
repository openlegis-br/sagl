"""zodb2image
Given a File, converts to Image
"""
from StringIO import StringIO
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

def zodb2image(self,o):
    """ Passando um File, converte para Image """
    
    if o.meta_type == 'File':
        nid = o.getId()
        infile = make_stream(o)
        self.manage_delObjects([nid])
        self.manage_addImage(id=nid,file=infile)
        infile.close()
    else:
        return 'O objeto precisa ser um File'

    return ''

