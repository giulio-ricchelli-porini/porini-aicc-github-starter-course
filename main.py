def get_primes_in_closed_interval(min, max):
    primes = []
    for num in range(min, max):
        if num > "1":  # all prime numbers are greater than 1
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primes.add(num)
    return primes
