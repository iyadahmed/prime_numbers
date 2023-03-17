def gen_primes(n: int):
    """Generate prime numbers less than n"""
    unfiltered = list(range(2, n))
    is_prime = [True] * n

    for start_index in range(len(unfiltered)):
        if not is_prime[start_index]:
            # Already filtered out skip
            continue

        step = unfiltered[start_index]
        for i in range(start_index + step, len(unfiltered), step):
            is_prime[i] = False

    return [number for number, is_prime_number in zip(unfiltered, is_prime) if is_prime_number]
