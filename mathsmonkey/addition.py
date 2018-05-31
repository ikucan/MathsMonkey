from mathsmonkey.pdf import pdf_base
from mathsmonkey.common import gen_rnd

from pylatex import Document, Section, Subsection, Tabular, MultiColumn, LongTabu, Command
from pylatex.utils import italic, bold
from random import randint

import functools

#
# generate a single example string of columnar addition for numbers of n digits
#
def gen_example(idx, n_digits, n_nums, var_digits=0):
    assert(n_digits > 1)
    assert(var_digits < n_digits)

    sum = 0    
    q_tab = Tabular(' c r ', row_height=1.2)

    nums = [gen_rnd(n_digits, var_digits) for n in range(0, n_nums)]
    sum_str = functools.reduce(lambda x,y:str(x) + '+' + str(y), nums)

    q_tab.add_row((bold(str(idx) + ':'), sum_str))

    a_tab = Tabular(' l l ', row_height=1.1)
    a_idx = bold(str(idx) + ":")
    a_tab.add_row((a_idx, sum))

    return (q_tab, a_tab)

class addition(pdf_base):
    """
    simple addition example generation class
    """

    def __init__(self):
        print('simple addition class created.')
        pdf_base.__init__(self)

    def gen(self, n_ex, n_digits, var_digits, n_nums, n_cols):
        print('generating.... ', n_ex, ',', n_digits, ',', var_digits, ',', n_cols)
        pdf_base.start(self, 'Simple Addition', [12, 14])
        self.n_ex = n_ex
        self.n_digits = n_digits
        self.var_digits = var_digits
        self.n_cols = n_cols

        with self.q_doc.create(LongTabu("X[r] " * n_cols,  row_height=2.0)) as q_tbl:
            for i in range(round(n_ex/n_cols)):
                row = [gen_example(n + i*n_cols, n_digits, n_nums, var_digits) for n in range(0, n_cols)]
                if i % 2 == 0:
                    q_tbl.add_row([r[0] for r in row], color="cream")
                else:
                    q_tbl.add_row([r[0] for r in row])
                    
        #self.q_doc.generate_pdf(out_dir + '/' + f_nm + str(n_digits) + '_digits_Q', clean_tex=False)
        self.q_doc.generate_pdf('xxxxxxxxxxx_digits_Q', clean_tex=False)
