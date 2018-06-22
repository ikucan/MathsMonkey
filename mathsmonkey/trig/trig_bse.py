from mathsmonkey.pdf import pdf_base
from mathsmonkey.common import gen_rnd

from pylatex import Document, Section, Subsection, Tabular, MultiColumn, LongTabu, Command, Math, Alignat
from pylatex.utils import italic, bold, NoEscape, escape_latex
from random import randint
from math import ceil

import abc
import functools

class trig_bse(pdf_base):
    """
    simple addition example generation class
    """
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def gen_smpl(self, idx, n_digits, n_nums, var_digits=0):
        """abstract generator method to prvide a simple question and answer tuple for a simple problem
        """

    @abc.abstractmethod
    def init(self):
        """xxx
        """

    def __init__(self, output_directory, file_name, test_name):
        pdf_base.__init__(self)
        self.f_nm = file_name
        self.out_dir = output_directory
        self.tst_nm = test_name

    def gen(self, n_nums, n_digits, var_digits, n_ex, n_cols, n_answ_cols = 7, out_file=None):
        print('generating.... ', n_ex, ',', n_nums, ',', n_digits, ',', var_digits, ',', n_cols)
        ttl = self.tst_nm + ' - ' + str(n_nums) + (' up to' if var_digits > 0 else '') + ' numbers, ' + str(n_digits)+ ' digits'
        pdf_base.start(self, ttl, [12, 14])
        self.init()
        
        nme = self.f_nm + '_digits_' + str(n_nums) + '_' + str(n_digits)+ '_' + str(var_digits)
        q_out_file = self.out_dir + '/' + nme + '_Q'
        a_out_file = self.out_dir + '/' + nme + '_A'
        if out_file != None:
            q_out_file = out_file + '_Q'
            a_out_file = out_file + '_A'

        # round number of problems to fill all columns on the question sheet
        n_probs = int(n_ex/n_cols + 1) * n_cols
        
        questions_and_answers = [self.gen_smpl(n, n_digits, n_nums, var_digits) for n in range(n_probs)]
        questions = list(map(lambda x:x[0], questions_and_answers))
        answers   = list(map(lambda x:x[1], questions_and_answers))
        
        with self.q_doc.create(LongTabu("X[l] " * n_cols,  row_height=2.0)) as q_tbl:
            for row in range(ceil(n_probs/n_cols)):
                q_row = questions[row * n_cols:(row + 1) * n_cols]
                if row % 2 == 0:
                    q_tbl.add_row(q_row, color = "cream")
                else:
                    q_tbl.add_row(q_row)
                
        with self.a_doc.create(LongTabu("X[l] " * n_answ_cols,  row_height=2.0)) as a_tbl:
            for row in range(ceil(n_probs/n_answ_cols)):
                a_row = answers[row * n_answ_cols:(row + 1) * n_answ_cols]
                # top up missing cells with empty string
                for i in range(0, n_answ_cols - len(a_row)):
                    a_row.append("")
                if row % 2 == 0:
                    a_tbl.add_row(a_row, color = "cream")
                else:
                    a_tbl.add_row(a_row)
                    
        self.q_doc.generate_pdf(q_out_file, clean_tex=True)
        self.a_doc.generate_pdf(a_out_file, clean_tex=True)
