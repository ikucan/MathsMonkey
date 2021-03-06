from pylatex import Document, Section, Subsection, Tabular, MultiColumn, LongTabu, Command
from pylatex import Math
from pylatex.basic import SmallText
from pylatex.position import FlushRight, FlushLeft
from pylatex.utils import italic, bold
from pylatex.package import Package

class pdf_base:
    """
    base class for all pdf generating classes
    """

    cream_clr_def = "0.92 0.92 0.8"
    pge_geom = {"tmargin" : "1cm",  "bmargin" : "1.5cm",  "lmargin" : "1cm",  "rmargin" : "1cm" }

    def __init__(self):
        a=1

    def start(self, ttl, fnt_sz = [16, 18]):
        q_doc = Document(geometry_options = self.pge_geom, lmodern = True)
        a_doc = Document(geometry_options = self.pge_geom, lmodern = True)
        
        q_doc.add_color(name="cream", model="rgb", description = self.cream_clr_def)
        q_doc.append(Command('fontsize', arguments = fnt_sz))
        #q_doc.append(Command('fontfamily', arguments = ['pcr']))
        q_doc.append(Command('selectfont'))
        q_doc.append(FlushLeft())
        
        with q_doc.create(Section("Questions: " + ttl, numbering = False)):
            q_doc.append('Solve questions below:')
            
        with a_doc.create(Section("Answers: " + ttl, numbering = False)):
            a_doc.append('Answers to problem sheet')

        a_doc.add_color(name = "cream", model = "rgb", description = self.cream_clr_def)

        self.q_doc = q_doc
        self.a_doc = a_doc
    
    def out_dir(self):
        return settings.pdf_out_root

