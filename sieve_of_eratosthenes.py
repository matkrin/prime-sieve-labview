import timeit


def sieve_of_eratosthenes_timed(n):
    t_start = timeit.default_timer()

    sieve = [True for i in range(n + 1)]
    p = 2

    while (p * p <= n):
        if (sieve[p] == True):
            for i in range(p ** 2, n + 1, p):
                sieve[i] = False
        p += 1

    t_delta = timeit.default_timer() - t_start

    sieve[0]= False
    sieve[1]= False

    primes = []
    for p in range(n + 1):
        if sieve[p]:
            primes.append(p)

    return primes, t_delta


if __name__ == '__main__':
    n = int(input("Calculate primes up to: "))
    primes, t_delta = sieve_of_eratosthenes_timed(n)
    print(f"There are {len(primes)} primes up to {n}")
    print(f"Took: {t_delta * 1000} ms")
