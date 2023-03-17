import numpy as np


def count_primes_less_than(n: int):
    """Count the number of prime numbers less than n"""
    is_prime = np.ones(shape=n, dtype=bool)

    for base in range(2, n):
        # base is both start index and step
        # used to cross out multiples of base
        if not is_prime[base]:
            # Already filtered out, skip
            continue

        # Mark all multiples of base as non prime, starting from the next multiple after base
        is_prime[base + base :: base] = False

    return np.count_nonzero(is_prime[2:])
