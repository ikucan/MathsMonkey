from mathsmonkey import settings
from random import randint

class num_hlpr:
    """  helper class for common numeric tasks
    """
    def gen_rnd(self, n_digits, var_digits = 0):
        """ generate a random number up to n-digits long with some variance in the number of digits
        """
        assert(n_digits >= 1)
        assert(var_digits < n_digits)

        dgts_offst = 0
        if var_digits > 0 :
            dgts_offst = randint(0, var_digits)
            
        min, max = pow(10, n_digits - 1 - dgts_offst), pow(10, n_digits - dgts_offst)
        assert(min < max)
        return randint(min, max)
