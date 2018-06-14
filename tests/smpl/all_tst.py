from mathsmonkey.smpl.smpl_mxd_add_sub import mix_add_sub
from mathsmonkey.smpl.smpl_addition import addition
from mathsmonkey.smpl.smpl_subtraction import subtraction
from mathsmonkey.smpl.smpl_multiplication import multiplication
import random

#
# for the same seed value (e.g. 0) an identical set of tests can be generated
# change this value if you want to generate a 'new' set of tests
#
random.seed(0)

mult = multiplication('../../pdfs/smpl/', 'simple_mutliplication')


all_tests = [ addition('../../pdfs/smpl/', 'simple_addition'),
              subtraction('../../pdfs/smpl/', 'simple_subtracion'),
              mix_add_sub('../../pdfs/smpl/', 'simple_addition_subtraction'),
              multiplication('../../pdfs/smpl/', 'simple_mutliplication') ]

for n_nums in range(2, 6):
    for n_dgts in range (1, 4):
        for dgt_var in range (0, n_dgts):
            n_cols = 2
            if n_nums * n_dgts < 15:
                n_cols += 1
            if n_nums * n_dgts < 10:
                n_cols += 1
            if n_nums * n_dgts < 5:
                n_cols += 1

            for test in all_tests:
                test.gen(n_nums, n_dgts, dgt_var, 100, n_cols)


