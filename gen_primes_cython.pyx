import numpy as np


cpdef int count_primes_less_than(int n):
    """Count the number of prime numbers less than n"""
    is_prime = np.ones(shape=n, dtype=bool)

    cdef int base

    for base in range(2, n):
        # base is both start index and step
        # used to cross out multiples of base
        if not is_prime[base]:
            # Already filtered out, skip
            continue

        is_prime[base + base :: base] = False

    return np.count_nonzero(is_prime[2:])
