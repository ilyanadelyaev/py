def heap_sort(D, reverse=False):
    D = D[:]

    def __down_heap(p, lenD):
        l = p * 2 + 1
        r = p * 2 + 2
        if l >= lenD:
            return
        if r >= lenD:
            return
        m = l if (D[l] < D[r] if reverse else D[l] > D[r]) else r
        if D[m] < D[p] if reverse else D[m] > D[p]:
            t = D[p]
            D[p] = D[m]
            D[m] = t
            __down_heap(m, lenD)

    # create heap

    md = len(D) / 2
    for p in xrange(md-1, -1, -1):
        __down_heap(p, len(D))

    # sort heap

    for i in xrange(len(D)-1):
        if D[0] < D[-1-i] if reverse else D[0] > D[-1-i]:
            t = D[0]
            D[0] = D[-1-i]
            D[-1-i] = t
            __down_heap(0, len(D)-1-i)

    return D


if __name__ == '__main__':
    import random
    N = 2**10
    I = random.sample(xrange(N**2), N)
    #print I

    D = heap_sort(I)
    DD = sorted(I)
    print 'D == DD:', D == DD

    D = heap_sort(I, reverse=True)
    DD = sorted(I, reverse=True)
    print 'reverse: D == DD:', D == DD
