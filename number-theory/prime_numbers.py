# naive algorithm to return if a number is prime or not
# O(N)
def is_prime_naive(number):
    for i in range(2, number):
        if number%i == 0:
            return False
    return True


# little optimized
# O(sqrt(N))
import math
def is_prime_optimized(number):
    for i in range(2, int(math.sqrt(number))):
        if number%i == 0:
            return False
    return True


# seive of eratosthenes
# T = N/2 + N/3 + N/4 + ...
# T = O(Nlog(logN))
def seive(number):
    """This returns all primes <= number"""
    primes = [True]*(number+1)
    primes[0] = False
    primes[1] = False

    for i in range(2, int(math.sqrt(number))+1):
        for j in range(i*2, number, i):
            primes[j] = False
    return [index for index, is_prime in enumerate(primes) if is_prime]


if __name__ == '__main__':
    n = 100
    print('{} is prime'.format(n)) if is_prime_naive(n) else print('{} is not a prime'.format(n))
    print('{} is prime'.format(n)) if is_prime_optimized(n) else print('{} is not a prime'.format(n))
    print('All primes from 1 to {} = {}'.format(n, seive(n)))
