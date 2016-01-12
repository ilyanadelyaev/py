def check_prime__naive(num):
    if num < 2:
        return False
    for i in xrange(2, num+1 - 1):
        if num % i == 0:
            return False
    return True


def eratosthenes(max_val):
    if max_val < 2:
        return
    sequence = range(2, max_val+1)
    index = 0
    while True:
        val = sequence[index]
        mult = val
        while True:
            if val * mult <= max_val:
                try:
                    del sequence[sequence.index(val * mult)]
                except ValueError:
                    pass
            else:
                break
            mult += 1
        index += 1
        if index >= len(sequence):
            break
    return sequence


def factorization(num):
    if num < 2:
        return
    prime_sequence = eratosthenes(num)
    factors = []
    for prime in prime_sequence:
        power = 0
        val = num
        while True:
            if val % prime == 0:
                val /= prime
                power += 1
            else:
                break
        factors.append(power)
    return [v for v in zip(prime_sequence, factors) if v[1]]


if __name__ == '__main__':
    import random

    # naive check prime
    assert check_prime__naive(2)
    assert check_prime__naive(7)
    assert check_prime__naive(29)
    assert check_prime__naive(97)
    assert check_prime__naive(109)

    # eratosthenes
    for i in eratosthenes(10000):
        assert check_prime__naive(i)

    # factorization
    for _ in xrange(10):
        num = random.randint(0, 10000)
        fact = factorization(num)
        assert reduce(lambda acc, val: acc * pow(val[0], val[1]), fact, 1) == num
