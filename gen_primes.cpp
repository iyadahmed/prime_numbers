#include <algorithm>
#include <iostream>
#include <vector>

int main(int argc, char **argv)
{
    int n = 10000000;

    // Assume all numbers are prime at first
    std::vector<bool> is_prime(n, true);

    for (int base = 2; base < n; base++)
    {
        if (!is_prime[base])
            // Already filtered out, skip
            continue;

        // Mark all multiples of base as non prime, starting from the next multiple after base
        for (int i = base + base; i < n; i += base)
        {
            is_prime[i] = false;
        }
    }

    // Skip first two is_prime entries as we started eliminating primes from base=2
    // we don't want to include base=0 and base=1 in the count
    std::cout << "Number of primes less than " << n << " equals " << std::count(is_prime.begin() + 2, is_prime.end(), true) << std::endl;

    return 0;
}
