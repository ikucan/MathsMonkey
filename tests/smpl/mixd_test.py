from mathsmonkey.smpl.smpl_mxd_add_sub import mix_add_sub
import random

random.seed(0)

test = mix_add_sub('../../pdfs/smpl/', 'simple_addition_subtraction')

#test.gen(4, 3, 1, 100, 3)
#test.foo()

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
            test.gen(n_nums, n_dgts, dgt_var, 100, n_cols)


