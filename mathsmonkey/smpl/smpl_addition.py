import abc

from mathsmonkey.smpl.smpl_bse import smpl_bse
from mathsmonkey.common import gen_rnd

from pylatex import Tabular, Math
from pylatex.utils import bold, NoEscape

import functools


class addition(smpl_bse):
    def __init__(self, out_dir, fnm):
        smpl_bse.__init__(self, out_dir, fnm)

    def gen_smpl(self, idx, n_digits, n_nums, var_digits=0):
        """ generate an example of a simple addition 
        """
        assert(n_digits >= 1)
        assert(var_digits < n_digits)
        q_tab = Tabular(' c r ', row_height=1.2)
        nums = [gen_rnd(n_digits, var_digits) for n in range(0, n_nums)]
        sum_str = functools.reduce(lambda x,y:str(x) + '+' + str(y), nums)
        mth = Math(escape=False, inline=True)
        mth.append(NoEscape(sum_str + '='))
        q_tab.add_row((bold(str(idx) + ':'), mth))
        a_tab = Tabular(' l l ', row_height=1.1)
        a_idx = bold(str(idx) + ":")
        a_tab.add_row((a_idx, sum(nums)))
        return (q_tab, a_tab)
