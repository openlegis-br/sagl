"""
TRML support of printing barcodes.
"""
# reportlab
from reportlab.platypus.flowables import Flowable
from reportlab.graphics import renderPDF
from reportlab.graphics.barcode import createBarcodeDrawing, getCodes
# trml
from . import utils, color


class BarCode(Flowable):
    """
    Origin (x, y) is the 'left bottom corner' of boundary border
    at <pageGraphics>.

    Code types:
        Standard39
        Extended39
        EAN13
        FIM
        EAN8
        Extended93
        USPS_4State
        Codabar
        MSI
        POSTNET
        Code11
        Standard93
        I2of5
        Code128 (default)

    Attributes:
        * fontName
        * strokeWidth
        * barFillColor
        * humanReadable
        * height
        * debug
        * lquiet
        * background
        * barWidth
        * strokeColor
        * barStrokeWidth
        * barStrokeColor
        * rquiet
        * quiet
        * barHeight
        * width
        * fontSize
        * fillColor
        * textColor
        * showBoundary
    """
    XPOS, YPOS, WIDTH, HEIGHT = range(4)

    def __init__(self, node, styles, value, encoding):
        Flowable.__init__(self)

        self.node = node
        self.styles = styles
        self.value = value
        self.encoding = encoding
        self.xpos = utils.unit_get(node.getAttribute('x'))
        self.ypos = utils.unit_get(node.getAttribute('y'))
        self.width = utils.unit_get(node.getAttribute('width'))
        self.height = utils.unit_get(node.getAttribute('height'))
        self.code_name = node.getAttribute('code')
        self.codes = getCodes()

        from trml2pdf.parser import ParserError
        try:
            self.codes[self.code_name]
        except KeyError as msg:
            raise ParserError("Unknown barcode name '%s'." % self.code_name)


    def get_default_bounds(self):
        "Get default size of barcode"
        bcc = self.codes[self.code_name]
        barcode = bcc(value=self.value)
        return barcode.getBounds() # x, y, width, height

    def wrap(self, *args):
        x, y, width, height = self.get_default_bounds()
        if self.width:
            width = self.width
        if self.height:
            height = self.height
        return (width, height)


    def draw(self):
        "Read attribs and draw barcode"

        units = ("strokeWidth", "barWidth", "barStrokeWidth", "barHeight",
                 "fontSize", "isoScale")
        colors = ("barFillColor", "background", "strokeColor", "barStrokeColor",
                  "fillColor", "textColor")
        bools = ("humanReadable", "debug", "lquiet", "rquiet", "quiet",
                 "checksum")
        names = ("fontName", "routing")

        kwargs = utils.attr_get(self.node, units,
                                self.encoding,
                                dict(zip(names, ["str"] * len(names)) +
                                     zip(colors, ["color"] * len(colors)) +
                                     zip(bools, ["bool"] * len(bools))),
                                {"barStrokeWidth": 0.00001} # defaults
                    )
        bcd = createBarcodeDrawing(self.code_name, value=self.value,
                                   width=self.width, height=self.height,
                                   **kwargs)
        renderPDF.draw(bcd, self.canv, self.xpos, self.ypos,
                       showBoundary=self.node.getAttribute("showBoundary"))
