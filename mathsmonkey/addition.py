from mathsmonkey.pdf import pdf_base

class addition(pdf_base):
    """
    simple addition example generation class
    """

    def __init__(self):
        print('simple addition class created.')
        pdf_base.__init__(self)

    def gen(self, n_nums, n_digits, var_digits, n_cols):
        print('generating.... ', n_nums, ',', n_digits, ',', var_digits)
        pdf_base.start(self, 'xxxxxxxxx')
        self.n_nums = n_nums
        self.n_digits = n_digits
        self.var_digits = var_digits
        
