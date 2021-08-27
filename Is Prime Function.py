# Is Prime function
# Resources: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#:~:text=To%20find%20all%20the%20prime%20numbers%20less%20than,let%20p%20equal%202%2C%20the%20smallest%20prime%20number.
#

import math


def prime_less_than(n):
    if n <= 2:
        return []
    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False
    number = math.sqrt(n)
    number = round(number)
    for i in range(2, number):
        if is_prime[i]:
            for x in range(i * i, n, i):
                is_prime[x] = False

    return [i for i in range(n) if is_prime[i]]


print(prime_less_than(10000))
