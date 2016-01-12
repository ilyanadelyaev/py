def insertion_sort(D, reverse=False):
    D = D[:]

    for j in xrange(1, len(D)):
        d = D[j]
        i = j - 1
        while i >= 0 and (D[i] < d if reverse else D[i] > d):
            D[i + 1] = D[i]
            i -= 1
        D[i + 1] = d

    return D


if __name__ == '__main__':
    import random
    N = 2**10
    I = random.sample(xrange(N**2), N)
    #print I

    D = insertion_sort(I)
    DD = sorted(I)
    print 'D == DD:', D == DD

    D = insertion_sort(I, reverse=True)
    DD = sorted(I, reverse=True)
    print 'reverse: D == DD:', D == DD
