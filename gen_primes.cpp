#include <algorithm>
#include <iostream>
#include <vector>

// NOTE: static inlining is important for speed here, removing "static" makes it slower!
// also -O2 G++ options is faster than -O3 for some reason for this specific program
static size_t count_primes_lt(int n)
{
    // Assume all numbers are prime at first
    std::vector<bool> is_prime(n, true);

    size_t result = 1; // Include the number 2 in the count by initializing result to 1

    // Odd only sieve
    for (int base = 3; base < n; base += 2)
    {
        if (!is_prime[base])
            // Already filtered out, skip
            continue;

        // Mark all multiples of base as non prime, starting from the next multiple after base
        for (int i = base + base; i < n; i += base)
        {
            is_prime[i] = false;
        }

        result++;
    }

    return result;
}

int main(int argc, char **argv)
{
    int n = 10'000'000;
    size_t result = count_primes_lt(n);
    std::cout << "Number of primes less than " << n << " equals " << result << std::endl;
    return 0;
}
