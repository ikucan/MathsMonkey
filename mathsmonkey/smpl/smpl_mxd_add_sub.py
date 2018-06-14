#import abc

from mathsmonkey.smpl.smpl_bse import smpl_bse
from mathsmonkey.common import gen_rnd, sign

from pylatex import Tabular, Math
from pylatex.utils import bold, NoEscape
from random import randint

from numpy import multiply

import functools

class mix_add_sub(smpl_bse):
    def __init__(self, out_dir, fnm):
        smpl_bse.__init__(self, out_dir, fnm, "Mixed simple addition and subtraction")

    def gen_smpl(self, idx, n_digits, n_nums, var_digits=0):
        """ generate an example of a simple addition 
        """
        assert(n_digits >= 1)
        assert(var_digits < n_digits)
        q_tab = Tabular(' c r ', row_height=1.2)

        # contents...
        nums = [gen_rnd(n_digits, var_digits) for n in range(0, n_nums)]
        sgns = [sign(randint(-1000000, 1000000)) for n in range(0, n_nums)]

        sign_syms = list(map(lambda x: '+' if x == 1 else '-', sgns))

        sum_str = ''.join([sign_syms[n] + str(nums[n]) for n in range(0, n_nums)])
        if sum_str[0] == '+':
            sum_str = sum_str[1:] # tail if leading with a '+'

        mth = Math(escape=False, inline=True)
        mth.append(NoEscape(sum_str + '='))
        q_tab.add_row((bold(str(idx) + ':'), mth))
        
        a_tab = Tabular(' l l ', row_height=1.1)
        a_idx = bold(str(idx) + ":")
        res = sum(multiply(nums, sgns))
        a_tab.add_row((a_idx, res))

        #print(sum_str, '=', res)
        return (q_tab, a_tab)
