def selection_sort(D, reverse=False):
    D = D[:]
    DD = []

    for i in xrange(len(D)):
        m = D[0]
        mi = 0
        for j in xrange(1, len(D)):
            if D[j] > m if reverse else D[j] < m:
                m = D[j]
                mi = j
        del D[mi]
        DD.append(m)

    return DD


if __name__ == '__main__':
    import random
    N = 2**10
    I = random.sample(xrange(N**2), N)
    #print I

    D = selection_sort(I)
    DD = sorted(I)
    print 'D == DD:', D == DD

    D = selection_sort(I, reverse=True)
    DD = sorted(I, reverse=True)
    print 'reverse: D == DD:', D == DD
