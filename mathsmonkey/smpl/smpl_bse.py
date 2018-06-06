from mathsmonkey.pdf import pdf_base
from mathsmonkey.common import gen_rnd

from pylatex import Document, Section, Subsection, Tabular, MultiColumn, LongTabu, Command, Math, Alignat
from pylatex.utils import italic, bold, NoEscape, escape_latex
from random import randint

import abc
import functools

class smpl_bse(pdf_base):
    """
    simple addition example generation class
    """
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def gen_smpl(self, idx, n_digits, n_nums, var_digits=0):
        """abstract generator method to prvide a simple question and answer tuple for a simple problem
        """

    def __init__(self, output_directory, file_name):
        pdf_base.__init__(self)
        self.f_nm = file_name
        self.out_dir = output_directory

    def gen(self, n_nums, n_digits, var_digits, n_ex, n_cols, out_file=None):
        print('generating.... ', n_ex, ',', n_nums, ',', n_digits, ',', var_digits, ',', n_cols)
        ttl = 'Simple addition - ' + str(n_nums) + ' numbers, ' + str(n_digits)+ ' digits'
        pdf_base.start(self, ttl, [12, 14])

        nme = self.f_nm + '_digits_' + str(n_nums) + '_' + str(n_digits)+ '_' + str(var_digits)
        q_out_file = self.out_dir + '/' + nme + '_Q'
        a_out_file = self.out_dir + '/' + nme + '_A'
        if out_file != None:
            q_out_file = out_file + '_Q'
            a_out_file = out_file + '_A'
            
        with self.a_doc.create(LongTabu("X[l] " * n_cols,  row_height=2.0)) as a_tbl:
            with self.q_doc.create(LongTabu("X[l] " * n_cols,  row_height=2.0)) as q_tbl:
                for i in range(round(n_ex/n_cols)):
                    row = [self.gen_smpl(n + i*n_cols, n_digits, n_nums, var_digits) for n in range(0, n_cols)]
                    if i % 2 == 0:
                        q_tbl.add_row([r[0] for r in row], color = "cream")
                        a_tbl.add_row([r[1] for r in row], color = 'cream')
                    else:
                        q_tbl.add_row([r[0] for r in row])
                        a_tbl.add_row([r[1] for r in row])
                    
        self.q_doc.generate_pdf(q_out_file, clean_tex=True)
        self.a_doc.generate_pdf(a_out_file, clean_tex=True)
