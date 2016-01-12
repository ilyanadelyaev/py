def binary_search(v, D):
    md = len(D) / 2

    mdv = D[md]
    if v == mdv:
        return md
    elif len(D) <= 1:
        return None
    elif v < mdv:
        return binary_search(v, D[:md])
    else:
        return md + binary_search(v, D[md:])


if __name__ == '__main__':
    import random
    N = 2**10
    I = random.sample(xrange(N**2), N)
    #print I

    I = sorted(I)
    v = I[random.choice(range(len(I)))]
    k = binary_search(v, I)
    kk = I.index(v)
    print 'k == kk:', k == kk
