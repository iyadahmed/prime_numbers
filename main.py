import sys
from time import perf_counter

# Check if "cython" appears in command-line arguments that come after the Python file name
if "cython" in sys.argv[1:]:
    print("Using Cython version")
    from gen_primes_cython import count_primes_less_than
else:
    from gen_primes import count_primes_less_than

if __name__ == "__main__":
    t1 = perf_counter()
    print(count_primes_less_than(10000000))
    t2 = perf_counter()
    print(f"Calculation took {t2 - t1} seconds.")
