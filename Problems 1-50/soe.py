# Sieve of Eratosthenes
# Finding Prime Numbers

def soe(n):
    '''Sieve of Eratosethenes. Finds prime numbers'''

    primes = []
    potential_primes = [True]*n

    for number in range(2, n):
        if potential_primes[number]:
            primes.append(number)

            # Eliminate multiples. They aren't prime
            for not_prime in range(number**2, n, number):
                potential_primes[not_prime] = False
    
    return primes