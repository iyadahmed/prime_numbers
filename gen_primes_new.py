import numpy as np
from time import perf_counter_ns


def main():
    n = 10_000_000
    # Assume all numbers are prime at first
    is_prime = np.ones(shape=n, dtype=bool)
    result = 1 # Include the number 2 in the count by initializing result to 1

    # Odd only sieve
    for base in range(3, n, 2):
        if not is_prime[base]:
            continue

        # Mark all multiples of base as non prime, starting from the next multiple after base
        for i in range(base + base, n, base):
            is_prime[i] = False
        
        result += 1
    
    print(result)


if __name__ == "__main__":
    t1 = perf_counter_ns()
    main()
    t2 = perf_counter_ns()
    d = t2 - t1
    print(f"Program took {d} ns, or {d // 1000_000} ms")
