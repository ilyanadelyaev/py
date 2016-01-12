def linear_search(k, D):
    for i in xrange(len(D)):
        d = D[i]
        if d == k:
            return i
    return None


if __name__ == '__main__':
    import random
    N = 2**10
    I = random.sample(xrange(N**2), N)
    #print I

    v = I[random.choice(range(len(I)))]
    k = linear_search(v, I)
    kk = I.index(v)
    print 'k == kk:', k == kk
