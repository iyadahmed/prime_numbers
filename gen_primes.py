import numpy as np


def gen_primes(n: int):
    """Generate prime numbers less than n"""
    unfiltered = np.arange(2, n, dtype=int)
    is_prime = np.ones(shape=n - 2, dtype=bool)

    for start_index in range(len(unfiltered)):
        if not is_prime[start_index]:
            # Already filtered out skip
            continue

        step = unfiltered[start_index]
        is_prime[start_index + step :: step] = False

    return unfiltered[is_prime]
