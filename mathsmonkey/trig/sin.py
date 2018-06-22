import abc

from mathsmonkey.trig.trig_bse import trig_bse
from mathsmonkey.common import gen_rnd

from pylatex import Tabular, Math
from pylatex.utils import bold, NoEscape

import functools

from sympy import *
from pylatex import (Document, TikZ, TikZNode, TikZDraw, TikZCoordinate, TikZUserPath, TikZOptions)

class xxsin(trig_bse):

    def __init__(self, out_dir, fnm):
        trig_bse.__init__(self, out_dir, fnm, "Sinus")
        
    def dud(self):
        with self.q_doc.create(TikZ()) as pic:
            
            # options for our node
            node_kwargs = {'align': 'center',
                           'minimum size': '100pt',
                           'fill': 'black!20'}

            # create our test node
            box = TikZNode(text='My block',
                           handle='box',
                           options=TikZOptions('draw',
                                               'rounded corners',
                                               **node_kwargs))

            # add to tikzpicture
            pic.append(box)

            # draw a few paths
            pic.append(TikZDraw([TikZCoordinate(0, -6),
                                 'rectangle',
                                 TikZCoordinate(2, -8)],
                                options=TikZOptions(fill='red')))

            # show use of anchor, relative coordinate
            pic.append(TikZDraw([box.west,
                                 '--',
                                 '++(-1,0)']))

            # demonstrate the use of the with syntax
            with pic.create(TikZDraw()) as path:
                
                # start at an anchor of the node
                path.append(box.east)
                
                # necessary here because 'in' is a python keyword
                path_options = {'in': 90, 'out': 0}
                path.append(TikZUserPath('edge',
                                         TikZOptions('-latex', **path_options)))

                path.append(TikZCoordinate(1, 0, relative=True))

    def init(self):
        self.q_doc
        self.dud()
        
    def gen_smpl(self, idx, n_digits, n_nums, var_digits=0):
        """ generate an example of a simple addition 
        """
        #self.dud()
        assert(n_digits >= 1)
        assert(var_digits < n_digits)
        q_tab = Tabular(' c r ', row_height=1.2)
        nums = [gen_rnd(n_digits, var_digits) for n in range(0, n_nums)]
        sum_str = functools.reduce(lambda x,y:str(x) + '+' + str(y), nums)
        mth = Math(escape=False, inline=True)
        #mth.append(NoEscape(sum_str + '='))
        #mth.append(NoEscape('sin(x)      + cos(y)           ='))
        x,y = symbols('x y')
        f=sin(x)**2 + cos(x)**2
        mth.append(latex(f))
        
        q_tab.add_row((bold(str(idx) + ':'), mth))
        a_tab = Tabular(' l l ', row_height=1.1)
        a_idx = bold(str(idx) + ":")
        a_tab.add_row((a_idx, sum(nums)))
        return (q_tab, a_tab)
