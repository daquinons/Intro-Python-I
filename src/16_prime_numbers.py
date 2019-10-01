import sys
import math


def is_prime_number(number):
    for n in range(1, number - 1):
        to_test = number - n
        if number % to_test is 0:
            return False

    return True


def sieve_of_erasthotenes(number):
    primes = []
    not_primes = []
    for n_searching_primes in range(2, number + 1):
        if n_searching_primes not in primes and n_searching_primes not in not_primes:
            primes.append(n_searching_primes)
            for n_searching_multiples in range(n_searching_primes + 1, number + 1):
                if n_searching_multiples % n_searching_primes is 0:
                    not_primes.append(n_searching_multiples)

    return primes


print(sieve_of_erasthotenes(100))

if __name__ == "__main__":
    try:
        number = int(sys.argv[1])
        if number > 1:
            if is_prime_number(number):
                print("Is prime!")
            else:
                print("Is not prime")
        else:
            raise Exception
    except Exception:
        print("Enter a number bigger than 1 as a first argument")
