from mathsmonkey.smpl.smpl_addition import addition

a = addition('../../pdfs/smpl/', 'simple_addition')

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
            a.gen(n_nums, n_dgts, dgt_var, 100, n_cols)

