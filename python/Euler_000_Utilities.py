from functools import reduce


def fibonacci(n):
    """ Computes the fibonacci(n) value """
    if n <= 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def sieve_for_primes_to(n):
    """ Generates the prime numbers up to 'n' as a list """
    size = n//2
    sieve = [1]*size
    limit = int(n**0.5)
    for i in range(1, limit):
        if sieve[i]:
            val = 2*i+1
            tmp = ((size-1) - i)//val
            sieve[i+val::val] = [0]*tmp
    return [2] + [i*2+1 for i, v in enumerate(sieve) if v and i > 0]


def divisors(n):
    """ Returns a generator giving the couples of divisors of 'n' """
    for divisor in range(1, int(n**0.5) + 1):
        if n % divisor == 0:
            yield divisor, n // divisor


def divisors_list(n):
    """ Returns a list giving the couples of divisors of 'n' """
    d = [1]
    for divisor in range(2, int(n**0.5) + 1):
        if n % divisor == 0:
            d.append(divisor)
            d.append(n // divisor)
    return d


def fact(number):
    """ Returns number! """
    return reduce(lambda x, y: x*y, range(1, number+1), 1)
