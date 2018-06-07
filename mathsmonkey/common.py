from mathsmonkey import settings

from random import randint
from math import copysign

def gen_rnd(n_digits, var_digits = 0):
    """ generate a random number up to n-digits long with some variance in the number of digits
    """
    assert(n_digits >= 1)
    assert(var_digits < n_digits)

    dgts_offst = 0
    if var_digits > 0 :
        dgts_offst = randint(0, var_digits)
            
    min, max = pow(10, n_digits - 1 - dgts_offst), pow(10, n_digits - dgts_offst) - 1
    assert(min < max)
    return randint(min, max)

sign = lambda x:int(copysign(1, x))
