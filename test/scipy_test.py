from pylatex import Document, Section, Subsection, Tabular, MultiColumn, LongTabu, Command, NoEscape
from pylatex import Math, Alignat
from pylatex.basic import SmallText
from pylatex.position import FlushRight
from pylatex.utils import italic, bold
from random import randint
from sympy import *

out_dir = "generated/"

pge_geom = {"tmargin" : "1cm",  "bmargin" : "1cm",  "lmargin" : "1cm",  "rmargin" : "1cm" }

def tst():
    print("----- START -----")

    doc = Document(geometry_options = pge_geom, lmodern=True)

    with doc.create(Section('The simple stuff', numbering=False)):
        doc.append('Some regular text and some')
        doc.append(italic('italic text. '))
        doc.append('\nAlso some crazy characters: $&#{}')
        
    x,y = symbols("x y")
    expr1 = sqrt(x/y) + cos(y)
    tex1 = latex(expr1)
    print(tex1)

    expr2 = x/y
    tex2 = latex(expr2)
    print(tex2)


    with doc.create(Subsection('Alignat math environment')):
        with doc.create(Alignat(numbering=False, escape=False)) as agn:
            agn.append(r'\frac{a}{b} &= 0 \\')
            agn.append(NoEscape(tex2 + ' \\'))
            agn.append(NoEscape(tex1 + ' \\'))
        

    doc.generate_pdf('scipy_tst', clean_tex=False)
    print("----- DONE -----")
    
if __name__ == '__main__' :
    tst()
