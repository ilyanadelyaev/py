def quick_sort(D, reverse=False):
    D = D[:]

    def __quick_sort(l, r):
        st, en = l, r
        p = D[(l + r) / 2]
        while l <= r:
            while l <= en and D[l] > p if reverse else D[l] < p:
                l += 1
            while r >= st and D[r] < p if reverse else D[r] > p:
                r -= 1
            if l <= r:
                t = D[l]
                D[l] = D[r]
                D[r] = t
                l += 1
                r -= 1
        if r > st:
            __quick_sort(st, r)
        if l < en:
            __quick_sort(l, en)

    __quick_sort(0, len(D) - 1)

    return D


if __name__ == '__main__':
    import random
    N = 2**4
    I = random.sample(xrange(N**2), N)
    #print I

    D = quick_sort(I)
    DD = sorted(I)
    print 'D == DD:', D == DD

    D = quick_sort(I, reverse=True)
    DD = sorted(I, reverse=True)
    print 'reverse: D == DD:', D == DD
