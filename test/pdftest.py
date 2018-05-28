from pylatex import Document, Section, Subsection, Tabular, MultiColumn, LongTabu
from pylatex import Math
from pylatex.utils import italic, bold

pge_geom = {"tmargin" : "1cm",  "bmargin" : "1cm",  "lmargin" : "1cm",  "rmargin" : "1cm" }

if __name__ == '__main__' :
    print("----- START -----")

    doc = Document(geometry_options = pge_geom)

    with doc.create(Section('The simple stuff', numbering=False)):
        doc.append('Some regular text and some')
        doc.append(italic('italic text. '))
        doc.append('\nAlso some crazy characters: $&#{}')

    # Add statement table
    with doc.create(LongTabu("X[l] X[l] X[r]",  row_height=2.0)) as data_table:
        for i in range(30):
            row = [str(i) + " :>", "2016-JUN-01", "$100"]
            if (i % 2) == 0:
                data_table.add_row(row, color="lightgray")
            else:
                data_table.add_row(row)

    doc.generate_pdf('full', clean_tex = False)
    
    print("----- DONE -----")
