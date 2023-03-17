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

    std::cout << "Number of primes less than " << n << " equals " << std::count(is_prime.begin() + 2, is_prime.end(), true) << std::endl;

    return 0;
}
