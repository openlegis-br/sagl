# -*- coding: utf-8 -*-

from StringIO import StringIO
import urlparse
import re
import AccessControl

def xhtml2rml(self,chaineHtml,chaineStyle):

 obj_url = self.absolute_url()

 def replace_url(match):
       """Compute local url
       """
       url = str(match.group('url'))
       if match.group('protocol') is not None:
           url = '%s%s' % (match.group('protocol'), url)
       else:
         try:
            url=urlparse.urljoin (obj_url, url)
         except:
            pass 
       return 'src="%s"' % url 
       return match.group(0) 


 def replace_entites(match):

       entite = str(match.group(1))

       dEnt = {"agrave":"à", "Agrave":"À", "aacute":"á", "Aacute":"Á", "acirc":"â", "Acirc":"Â",\
 "atilde":"ã", "Atilde":"Ã", "auml":"ä", "Auml":"Ä", "aring":"å", "Aring":"Å", "aelig":"æ", "AElig":"Æ",\
 "egrave":"è", "Egrave":"È", "eacute":"é", "Eacute":"É", "ecirc":"ê", "Ecirc":"Ê", "euml":"ë", "Euml":"Ë",\
 "igrave":"ì", "Igrave":"Ì", "iacute":"í", "Iacute":"Í", "icirc":"î", "Icirc":"Î", "iuml":"ï", "Iuml":"Ï",\
 "ograve":"ò", "Ograve":"Ò", "oacute":"ó", "Oacute":"Ó", "ocirc":"ô", "Ocirc":"Ô", "ouml":"ö", "Ouml":"Ö",\
 "Otilde":"Õ", "otilde":"õ", "ugrave":"ù", "Ugrave":"Ù", "uacute":"ú", "ordm":"º",  "ordf":"ª", \
 "Uacute":"Ú", "ucirc":"û", "Ucirc":"Û", "uuml":"ü", "Uuml":"Ü", "ntilde":"ñ", "Ntilde":"Ñ", "ccedil":"ç",\
 "Ccedil":"Ç", "yacute":"ý", "Yacute":"Ý", "szlig":"ß", "laquo":"«", "raqo":"»", "para":"§", "copy":"©",\
 "nbsp":" ", "quot": "'" }
       if dEnt.has_key(entite):
         return dEnt[entite]
       else:
         return '&' + entite + ';'
       return match.group(0) 

 def replace_ecom(match):

       Letter = ''
       if match.group(1) is not None: 
        Letter= str(match.group(1))
        return '&' + Letter
       else:
        return '&' +'amp;'
       return match.group(0) 


 def replace_tag(match):

       debutTag = str(match.group('debutTag'))
       finTag = str(match.group('finTag'))
       attrTag=''
       contentTag=''

       if match.group('attrTag') is not None:
         attrTag = str(match.group('attrTag'))
       if match.group('contentTag') is not None:
         contentTag = str(match.group('contentTag'))

       reEntites = re.compile('&([a-zA-Z]+);')
  

       if debutTag.lower()=='p':
          contentTag = reEntites.sub(replace_entites, contentTag)
          debutTag='para' + ' style="' + chaineStyle + '"'
          attrTag = ''
          finTag='</para><para style="P5"><font color="white">-</font></para>'
          return '\r\n' + finTag + '\r\n' + '<'+ debutTag + attrTag +'>\r\n'+ contentTag + '\r\n'

       if debutTag.lower() in ('pre','code'):
          debutTag='xpre'
          finTag='</xpre>'
          attrTag = ''
          entete ='\r\n</para>\r\n'
          fin='\r\n<para' + ' style="' + chaineStyle + '">\r\n'
          return entete + '<'+ debutTag + attrTag + '>\r\n <![CDATA[ \r\n'+ contentTag + '\r\n ]]'\
 + '> \r\n' + finTag + '\r\n' + fin

       elif match.group('hNumber') is not None:
          contentTag = reEntites.sub(replace_entites, contentTag)
          debutTag='para'
          finTag='</para>'
          attrTag = ' style="title' + str(match.group('hNumber')) + '"'
          return '\r\n' + finTag + '\r\n' + '<'+ debutTag + attrTag +'>\r\n'+ contentTag + '\r\n'

       elif debutTag.lower()=='table':
          contentTag = reEntites.sub(replace_entites, contentTag)
          debutTag='blockTable'
          finTag='</blockTable>'
          attrTag = ''
          entete ='\r\n</para>\r\n'
          fin='\r\n<para' + ' style="' + chaineStyle + '">\r\n'
          return entete + '<'+ debutTag + attrTag +'>\r\n'+ contentTag + '\r\n' + finTag + fin      
       
       return match.group(0) 

 def replace_tag_img(match):
        
       newWidth=''
       newHeight=''
       if match.group('contentTagImg') is not None:
         contentTagImg = str(match.group('contentTagImg'))
         reSrc = re.compile ('src\s*=\s*([\'\"])([^\"\']*)\\1', re.IGNORECASE)
         matchs = reSrc.search( contentTagImg )
         srcImg = '%s' % matchs.group(2)
         reWidth = re.compile ('width\s*=\s*([\'\"])([0-9]+)(px)?\\1', re.IGNORECASE)
         matchs = reWidth.search( contentTagImg )
         if matchs is not None:
           newWidth= str(int(int(matchs.group(2))/1.43))
 
         reHeight = re.compile ('height\s*=\s*([\'\"])([0-9]+)(px)?\\1', re.IGNORECASE)
         matchs = reHeight.search( contentTagImg )
         if matchs is not None:
           newHeight = str(int(int(matchs.group(2))/1.43))

       if newWidth and newHeight:
           tailleImage = ' width="' + newWidth + '" height="' + newHeight + '"'
       else:
           tailleImage =''
       

       entete = '</para>\r\n'
       fin='\r\n<para' + ' style="' + chaineStyle + '">\r\n'
       tagImg='\r\n<illustration' + tailleImage + '>\r\n<image file="' + srcImg + '" x="0" y="0"'\
 + tailleImage + ' />\r\n</illustration>\r\n'
       
       return entete + tagImg + fin       
       return match.group(0) 

 def replace_tag_br(match):

       entete = '</para>\r\n'
       fin='<para' + ' style="' + chaineStyle + '">\r\n'      

       return entete + fin       

 chaineRml = chaineHtml

 abs_url = re.compile('src\s*=\s*([\'\"])(?P<protocol>(ht|f)tps?)?(?P<url>[^\"\']*)\\1', re.IGNORECASE)
 chaineRml = abs_url.sub(replace_url, chaineRml) 


 reTag  = re.compile('<(?P<debutTag>(p|pre|code|table|h(?P<hNumber>[1-7])))(?P<attrTag>\s+[^>]*\s*)?>\
(?P<contentTag>([^<]|<(?!/\\1))*)(?P<finTag></(\\1)\s*>)', re.IGNORECASE |re.DOTALL)
 chaineRml = reTag.sub(replace_tag, chaineRml) 


 reTagImg = re.compile('<img(?P<contentTagImg>[^>]*)/?\s*>', re.IGNORECASE |re.DOTALL)
 chaineRml = reTagImg.sub(replace_tag_img, chaineRml) 

 reTagBr = re.compile('<br[^>]*/?\s*>', re.IGNORECASE |re.DOTALL)
 chaineRml = reTagBr.sub(replace_tag_br, chaineRml) 

 reTagInutiles = re.compile('<a\s[^>]*>|</a\s*>|</?span[^>]*>|</?div[^>]*>', re.IGNORECASE |re.DOTALL)
 chaineRml = reTagInutiles.sub('', chaineRml) 

 reEcom = re.compile('&([^a-zA-Z])|&\s')
 chaineRml = reEcom.sub(replace_ecom, chaineRml) 
       

 return chaineRml

