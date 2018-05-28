from pylatex import Document, Section, Subsection, Tabular, MultiColumn, LongTabu, Command
from pylatex import Math
from pylatex.basic import SmallText
from pylatex.position import FlushRight
from pylatex.utils import italic, bold
from random import randint

out_dir = "generated/"
pge_geom = {"tmargin" : "1cm",  "bmargin" : "1cm",  "lmargin" : "1cm",  "rmargin" : "1cm" }
cream_clr_def = "0.92 0.92 0.8"

#
# generate a single example string of columnar addition for numbers of n digits
#
def gen_example(idx, n_digits, n_nums, var_digits=0):
    assert(n_digits > 1)
    assert(var_digits < n_digits)

    sum = 0
    
    q_tab = Tabular(' c r ', row_height=1.2)
    a_tab = Tabular(' l l ', row_height=1.1)
    for n in range(0, n_nums):
        dgts_offst = randint(0, var_digits)

        min, max = pow(10, n_digits - 1 - dgts_offst), pow(10, n_digits - dgts_offst)
        assert(min < max)
        rnum = randint(min, max)
        if (n == 0) :
            q_tab.add_row(("", rnum))
        else:
            q_tab.add_row(("+", rnum))
        sum += rnum

    q_tab.add_hline()
    q_tab.add_empty_row()
    q_tab.add_empty_row()

    a_idx = bold(str(idx) + ":")
    a_tab.add_row((a_idx, sum))
        
    return (q_tab, a_tab)

#
# main generator funcion
#
def gen(f_nm, n_ex, n_digits, digit_var, n_nums, n_cols):
    print("----- START -----")

    ttl = 'Column addition - ' + str(n_nums) + ' ' + str(n_digits) + '-digit values with ' + str(digit_var) + '-digit variance'
    
    q_doc = Document(geometry_options = pge_geom, lmodern=True)
    a_doc = Document(geometry_options = pge_geom, lmodern=True)
    
    with q_doc.create(Section("Questions: " + ttl, numbering=False)):
        q_doc.append('Solve the following questions!')

    with a_doc.create(Section("Answers: " + ttl, numbering=False)):
        a_doc.append('Answers to problem sheet')

    q_doc.add_color(name="cream", model="rgb", description=cream_clr_def)
    q_doc.append(Command('fontsize', arguments = ['16', '18']))
    q_doc.append(Command('fontfamily', arguments = ['pcr']))
    q_doc.append(Command('selectfont'))
    q_doc.append(FlushRight())

    a_doc.add_color(name="cream", model="rgb", description=cream_clr_def)
    
    # Add statement table
    with a_doc.create(LongTabu("X[l] " * n_cols,  row_height=2.0)) as a_tbl:
        with q_doc.create(LongTabu("X[r] " * n_cols,  row_height=2.0)) as q_tbl:
            for i in range(round(n_ex/n_cols)):
                row = ['  ' + str(n + i*n_cols) + '.' for n in range(0, n_cols)]
                q_tbl.add_row(row, mapper=bold, color="cream")

                row = [gen_example(n + i*n_cols, n_digits, n_nums, digit_var) for n in range(0, n_cols)]
                q_tbl.add_row([r[0] for r in row])

                if i % 2 == 0:
                    #a_tbl.add_row([r[1] for r in row], color = 'lightgray')
                    a_tbl.add_row([r[1] for r in row], color = 'cream')
                else:
                    a_tbl.add_row([r[1] for r in row])

    # write the file
    q_doc.generate_pdf(out_dir + '/' + f_nm + str(n_digits) + '_digits_Q', clean_tex=False)
    a_doc.generate_pdf(out_dir + '/' + f_nm + str(n_digits) + '_digits_A', clean_tex=False)
    print("----- DONE -----")

if __name__ == '__main__' :
    # ik:>> TODO :>> do a check for out_dir
    #gen('column_addition', n_ex=20, n_digits=2, digit_var=0, n_nums=2, n_cols=9)
    #gen('column_addition', n_ex=20, n_digits=2, digit_var=0, n_nums=3, n_cols=9)
    gen('column_addition', n_ex=200, n_digits=6, digit_var=4, n_nums=3, n_cols=5)
    #gen('column_addition', n_ex=200, n_digits=10, digit_var=3, n_nums=4, n_cols=5)

