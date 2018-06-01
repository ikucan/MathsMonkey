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
    #doc.append(Command('usepackage', arguments = ['multicol']))
    #doc.append(Command('mutlicols', arguments = ['3']))
    
    with doc.create(Section('Some numbers to add', numbering=False)):
        doc.append('some blurb')

    for i in range(0, 100):
        doc.append('abcdefg ')
        
    doc.generate_pdf('sympy2_tst', clean_tex=False)
    print("----- DONE -----")

if __name__ == '__main__' :
    tst()
