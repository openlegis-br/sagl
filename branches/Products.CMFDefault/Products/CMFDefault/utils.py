##############################################################################
#
# Copyright (c) 2001 Zope Foundation and Contributors.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
""" Utility functions. """

from __future__ import absolute_import
from email.header import make_header
from email.mime.text import MIMEText
import os
import re
try:
    import rfc822
except ImportError:
    import rfc822py3 as rfc822
from sgmllib import SGMLParser
try:
    from StringIO import StringIO 
except ImportError:
    from io import StringIO
from AccessControl.SecurityInfo import ModuleSecurityInfo
from Acquisition import aq_get
from App.Common import package_home
from pkg_resources import DistributionNotFound
from pkg_resources import get_distribution
from ZTUtils.Zope import complex_marshal
from zope.component import getUtility
from zope.component import queryUtility
from zope import i18n # disambiguation
from zope.i18n.interfaces import IUserPreferredCharsets
from zope.i18nmessageid import MessageFactory
from zope.publisher.interfaces.browser import IBrowserRequest

from Products.CMFCore.interfaces import IPropertiesTool

from Products.CMFDefault.exceptions import EmailAddressInvalid
from Products.CMFDefault.exceptions import IllegalHTML


security = ModuleSecurityInfo( 'Products.CMFDefault.utils' )

try:
    get_distribution('Products.CMFCalendar')
except DistributionNotFound:
    PRODUCTS_CMFCALENDAR_INSTALLED = False
else:
    PRODUCTS_CMFCALENDAR_INSTALLED = True

try:
    get_distribution('Products.CMFUid')
except DistributionNotFound:
    PRODUCTS_CMFUID_INSTALLED = False
else:
    PRODUCTS_CMFUID_INSTALLED = True

security.declarePrivate('_dtmldir')
_dtmldir = os.path.join( package_home( globals() ), 'dtml' )
_wwwdir = os.path.join( package_home( globals() ), 'www' )

security.declarePublic('formatRFC822Headers')
def formatRFC822Headers( headers ):

    """ Convert the key-value pairs in 'headers' to valid RFC822-style
        headers, including adding leading whitespace to elements which
        contain newlines in order to preserve continuation-line semantics.
    """
    munged = []
    linesplit = re.compile( r'[\n\r]+?' )

    for key, value in headers:

        vallines = linesplit.split( value )
        while vallines:
            if vallines[-1].rstrip() == '':
                vallines = vallines[:-1]
            else:
                break
        munged.append( '%s: %s' % ( key, '\r\n  '.join( vallines ) ) )

    return '\r\n'.join( munged )


security.declarePublic('parseHeadersBody')
def parseHeadersBody( body, headers=None, rc=re.compile( r'\n|\r\n' ) ):

    """ Parse any leading 'RFC-822'-ish headers from an uploaded
        document, returning a dictionary containing the headers
        and the stripped body.

        E.g.::

            Title: Some title
            Creator: Tres Seaver
            Format: text/plain
            X-Text-Format: structured

            Overview

            This document .....

            First Section

            ....


        would be returned as::

            { 'Title' : 'Some title'
            , 'Creator' : 'Tres Seaver'
            , 'Format' : 'text/plain'
            , 'text_format': 'structured'
            }

        as the headers, plus the body, starting with 'Overview' as
        the first line (the intervening blank line is a separator).

        Allow passing initial dictionary as headers.
    """
    buffer = StringIO.StringIO(body)
    message = rfc822.Message(buffer)

    headers = headers and headers.copy() or {}

    for key in message.keys():
        headers[key.capitalize()] = '\n'.join(message.getheaders(key))

    return headers, buffer.read()


security.declarePublic('semi_split')
def semi_split(s):

    """ Split 's' on semicolons.
    """
    return map(lambda x: x.strip(), s.split( ';' ) )

security.declarePublic('comma_split')
def comma_split(s):

    """ Split 's' on commas.
    """
    return map(lambda x: x.strip(), s.split( ',') )

security.declarePublic('seq_strip')
def seq_strip(seq, stripper=lambda x: x.strip() ):
    """ Strip a sequence of strings.
    """
    if isinstance(seq, list):
        return map( stripper, seq )

    if isinstance(seq, tuple):
        return tuple( map( stripper, seq ) )

#    raise ValueError, "%s of unsupported sequencetype %s" % ( seq, type( seq ) )
    raise ValueError("%s of unsupported sequencetype %s").with_traceback(seq, type( seq )) 


security.declarePublic('tuplize')
def tuplize( valueName, value, splitter=lambda x: x.split() ):

    if isinstance(value, tuple):
        return seq_strip( value )

    if isinstance(value, list):
        return seq_strip( tuple( value ) )

    if isinstance(value, basestring):
        return seq_strip( tuple( splitter( value ) ) )

#    raise ValueError, "%s of unsupported type" % valueName
    raise ValueError("%s of unsupported sequencetype %s").with_traceback(valueName) 

class SimpleHTMLParser( SGMLParser ):

    #from htmlentitydefs import entitydefs

    def __init__( self, verbose=0 ):

        SGMLParser.__init__( self, verbose )
        self.savedata = None
        self.title = ''
        self.metatags = {}
        self.body = ''

    def handle_data( self, data ):

        if self.savedata is not None:
            self.savedata = self.savedata + data

    def handle_charref( self, ref ):

        self.handle_data( "&#%s;" % ref )

    def handle_entityref( self, ref ):

        self.handle_data( "&%s;" % ref )

    def save_bgn( self ):

        self.savedata = ''

    def save_end( self ):

        data = self.savedata
        self.savedata = None
        return data

    def start_title( self, attrs ):

        self.save_bgn()

    def end_title( self ):

        self.title = self.save_end()

    def do_meta( self, attrs ):

        name = ''
        content = ''

        for attrname, value in attrs:

            value = value.strip()

            if attrname == "name":
                name = value.capitalize()

            if attrname == "content":
                content = value

        if name:
            self.metatags[ name ] = content

    def unknown_startag( self, tag, attrs ):

        self.setliteral()

    def unknown_endtag( self, tag ):

        self.setliteral()

#
#   HTML cleaning code
#

# These are the HTML tags that we will leave intact
VALID_TAGS = { 'a'          : 1
             , 'b'          : 1
             , 'base'       : 0
             , 'big'        : 1
             , 'blockquote' : 1
             , 'body'       : 1
             , 'br'         : 0
             , 'caption'    : 1
             , 'cite'       : 1
             , 'code'       : 1
             , 'dd'         : 1
             , 'div'        : 1
             , 'dl'         : 1
             , 'dt'         : 1
             , 'em'         : 1
             , 'h1'         : 1
             , 'h2'         : 1
             , 'h3'         : 1
             , 'h4'         : 1
             , 'h5'         : 1
             , 'h6'         : 1
             , 'head'       : 1
             , 'hr'         : 0
             , 'html'       : 1
             , 'i'          : 1
             , 'img'        : 0
             , 'kbd'        : 1
             , 'li'         : 1
           # , 'link'       : 1 type="script" hoses us
             , 'meta'       : 0
             , 'ol'         : 1
             , 'p'          : 1
             , 'pre'        : 1
             , 'small'      : 1
             , 'span'       : 1
             , 'strong'     : 1
             , 'sub'        : 1
             , 'sup'        : 1
             , 'table'      : 1
             , 'tbody'      : 1
             , 'td'         : 1
             , 'th'         : 1
             , 'title'      : 1
             , 'tr'         : 1
             , 'tt'         : 1
             , 'u'          : 1
             , 'ul'         : 1
             }

NASTY_TAGS = { 'script'     : 1
             , 'object'     : 1
             , 'embed'      : 1
             , 'applet'     : 1
             }


class StrippingParser( SGMLParser ):

    """ Pass only allowed tags;  raise exception for known-bad.
    """
    from html.htmlentitydefs import entitydefs # replace entitydefs from sgmllib

    def __init__( self, valid_tags=None, nasty_tags=None ):

        SGMLParser.__init__( self )
        self.result = ""
        self.valid_tags = valid_tags or VALID_TAGS
        self.nasty_tags = nasty_tags or NASTY_TAGS

    def handle_data( self, data ):

        if data:
            self.result = self.result + data

    def handle_charref( self, name ):

        self.result = "%s&#%s;" % ( self.result, name )

    def handle_entityref(self, name):

        if self.entitydefs.has_key(name):
            x = ';'
        else:
            # this breaks unstandard entities that end with ';'
            x = ''

        self.result = "%s&%s%s" % (self.result, name, x)

    def unknown_starttag(self, tag, attrs):
        """ Delete all tags except for legal ones.
        """
        if self.valid_tags.has_key(tag):

            self.result = self.result + '<' + tag

            for k, v in attrs:

                if k.lower().startswith('on'):
                    msg = _(u"JavaScript event '${attribute}' not allowed.",
                            mapping={'attribute': k})
                    raise IllegalHTML(msg)

                if v.lower().startswith('javascript:'):
                    msg = _(u"JavaScript URI '${value}' not allowed.",
                            mapping={'value': v})
                    raise IllegalHTML(msg)

                self.result = '%s %s="%s"' % (self.result, k, v)

            endTag = '</%s>' % tag
            if self.valid_tags.get(tag):
                self.result = self.result + '>'
            else:
                self.result = self.result + ' />'

        elif self.nasty_tags.get(tag):
            msg = _(u"Dynamic tag '${tag}' not allowed.",
                    mapping={'tag': tag})
            raise IllegalHTML(msg)

        else:
            pass    # omit tag

    def unknown_endtag(self, tag):

        if self.valid_tags.get(tag):

            self.result = "%s</%s>" % (self.result, tag)
            remTag = '</%s>' % tag


security.declarePublic('scrubHTML')
def scrubHTML( html ):

    """ Strip illegal HTML tags from string text.

    o Prefer a utility, if registered.
    """
    scrubber = queryUtility(IHTMLScrubber)

    if scrubber is not None:
        return scrubber.scrub(html)

    parser = StrippingParser()
    parser.feed( html )
    parser.close()
    return parser.result

security.declarePublic('isHTMLSafe')
def isHTMLSafe( html ):

    """ Would current HTML be permitted to be saved?
    """
    try:
        scrubHTML( html )
    except IllegalHTML:
        return 0
    else:
        return 1

security.declarePublic('bodyfinder')
def bodyfinder(text):
    """ Return body or unchanged text if no body tags found.

    Always use html_headcheck() first.
    """
    lowertext = text.lower()
    bodystart = lowertext.find('<body')
    if bodystart == -1:
        return text
    bodystart = lowertext.find('>', bodystart) + 1
    if bodystart == 0:
        return text
    bodyend = lowertext.rfind('</body>', bodystart)
    if bodyend == -1:
        return text
    return text[bodystart:bodyend]

security.declarePrivate('_htfinder')
_htfinder = re.compile(r'(\s|(<[^<>]*?>))*<html.*<body.*?>.*</body>',
                       re.DOTALL)

security.declarePublic('html_headcheck')
def html_headcheck(html):
    """ Return 'true' if document looks HTML-ish enough.

    If true bodyfinder() will be able to find the HTML body.
    """
    lowerhtml = html.lower()
    if lowerhtml.find('<html') == -1:
        return 0
    elif _htfinder.match(lowerhtml):
        return 1
    else:
        return 0

security.declarePublic('html_marshal')
def html_marshal(**kw):
    """ Marshal variables for html forms.
    """
    vars = [ (key + converter, value)
             for key, converter, value in complex_marshal(kw.items()) ]
    return tuple(vars)

security.declarePublic('toUnicode')
def toUnicode(value, charset=None):
    """ Convert value to unicode.
    """
    if isinstance(value, str):
        return charset and unicode(value, charset) or unicode(value)
    elif isinstance(value, list):
        return [ toUnicode(val, charset) for val in value ]
    elif isinstance(value, tuple):
        return tuple( [ toUnicode(val, charset) for val in value ] )
    elif isinstance(value, dict):
        for key, val in value.items():
            value[key] = toUnicode(val, charset)
        return value
    else:
        return value

security.declarePublic('decode')
def decode(value, context):
    """ Decode value using default_charset.
    """
    ptool = getUtility(IPropertiesTool)
    default_charset = ptool.getProperty('default_charset', None)
    return toUnicode(value, default_charset)

security.declarePublic('translate')
def translate(message, context):
    """ Translate i18n message.
    """
    if isinstance(message, Exception):
        try:
            message = message[0]
        except (TypeError, IndexError):
            pass
    # in Zope3, context is adapted to IUserPreferredLanguages,
    # which means context should be the request in this case.
    # Do not attempt to acquire REQUEST from the context, when we already
    # got a request as the context
    if context is not None:
        if not IBrowserRequest.providedBy(context):
            context = aq_get(context, 'REQUEST', None)

    return i18n.translate(message, domain='cmf_default', context=context)

security.declarePublic('getBrowserCharset')
def getBrowserCharset(request):
    """ Get charset preferred by the browser.
    """
    envadapter = IUserPreferredCharsets(request)
    charsets = envadapter.getPreferredCharsets() or ['utf-8']
    return charsets[0]

security.declarePublic('makeEmail')
def makeEmail(mtext, context, headers={}):
    """ Make email message.
    """
    ptool = getUtility(IPropertiesTool)
    email_charset = ptool.getProperty('email_charset', None) or 'utf-8'
    try:
        msg = MIMEText(mtext.encode('ascii'), 'plain')
    except UnicodeEncodeError:
        msg = MIMEText(mtext.encode(email_charset), 'plain', email_charset)
    for k, val in headers.items():
        if isinstance(val, str):
            val = decode(val, context)
        if isinstance(val, i18n.Message):
            val = translate(val, context)
        header = make_header([ (w, email_charset) for w in val.split(' ') ])
        msg[k] = str(header)
    return msg.as_string()

# RFC 2822 local-part: dot-atom or quoted-string
# characters allowed in atom: A-Za-z0-9!#$%&'*+-/=?^_`{|}~
# RFC 2821 domain: max 255 characters
_LOCAL_RE = re.compile(r'([A-Za-z0-9!#$%&\'*+\-/=?^_`{|}~]+'
                     r'(\.[A-Za-z0-9!#$%&\'*+\-/=?^_`{|}~]+)*|'
                     r'"[^(\|")]*")@[^@]{3,255}$')

# RFC 2821 local-part: max 64 characters
# RFC 2821 domain: sequence of dot-separated labels
# characters allowed in label: A-Za-z0-9-, first is a letter
# Even though the RFC does not allow it all-numeric domains do exist
_DOMAIN_RE = re.compile(r'[^@]{1,64}@[A-Za-z0-9][A-Za-z0-9-]*'
                                r'(\.[A-Za-z0-9][A-Za-z0-9-]*)+$')

security.declarePublic('checkEmailAddress')
def checkEmailAddress(address):
    """ Check email address.

    This should catch most invalid but no valid addresses.
    """
    if not _LOCAL_RE.match(address):
        raise EmailAddressInvalid
    if not _DOMAIN_RE.match(address):
        raise EmailAddressInvalid

security.declarePublic('Message')
Message = _ = MessageFactory('cmf_default')

security.declarePublic("thousands_commas")
def thousands_commas(value):
    """Format an integer with commas as thousand separator"""
    i = int(value)
    if sys.version_info >= (2, 7):
        warn("On Python 2.7 and higher Use {:,}.formatting",
             DeprecationWarning,
             stacklevel=2)
        return "{:,}".format(value)
    l = list(str(i))
    for idx in range(len(l) - 3, 0, -3):
        l.insert(idx, ",")
    return "".join(l)
